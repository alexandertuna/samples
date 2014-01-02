"""
metaroot.file

Module for retrieving histograms and graphs saved to ROOT files,
and will properly add them if retrieving from several files.
Also has methods from inspecting ROOT files like getting as list
of existing histograms or directories.

Part of the metaroot package.
"""

__author__ = 'Ryan Reece'
__email__ = 'ryan.reece@cern.ch'
__created__ = '2008-05-01'
__copyright__ = 'Copyright 2008-2011 Ryan Reece'
__license__ = 'GPL http://www.gnu.org/licenses/gpl.html'

#------------------------------------------------------------------------------

import glob
import os
import sys
import ROOT
verbosity = 0

#______________________________________________________________________________
def write(obj, filename, dir=''):
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    f = ROOT.gROOT.GetListOfFiles().FindObject(filename)
    if not f:
        f = ROOT.TFile.Open(filename, 'RECREATE')
    d = f.GetDirectory(dir)
    if not d:
        d = make_root_dir(f, dir)
    d.cd()
    if verbosity >= 1:
        print 'metaroot: writing %s:%s/%s' % (filename, dir, obj.GetName())
        sys.stdout.flush()
    obj.Write()

#______________________________________________________________________________
def make_root_dir(f, dir):
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    dir.rstrip('/')
    dir_split = dir.split('/')
    lead_dir = dir_split[0]
    sub_dirs = dir_split[1:]

    d = f.GetDirectory(lead_dir)
    if not d:
        d = f.mkdir(lead_dir)
    
    if sub_dirs:
        return make_root_dir(d, '/'.join(sub_dirs))
    else:
        return d

#______________________________________________________________________________
def walk(top, topdown=True):
    """
    os.path.walk like function for TDirectories.
    Return 4-tuple: (dirpath, dirnames, filenames, top)
        dirpath = '/some/path' for some file_name.root:/some/path
        dirnames = ['list', 'of' 'TDirectory', 'keys']
        filenames = ['list', 'of' 'object', 'keys']
        top = this level's TDirectory
    """
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    assert isinstance(top, ROOT.TDirectory)
    names = [k.GetName() for k in top.GetListOfKeys()]
    dirpath = top.GetPath()
    dirnames = []
    filenames = []
    ## filter names for directories
    for k in names:
        d = top.Get(k)
        if isinstance(d, ROOT.TDirectory):
            dirnames.append(k)
        else:
            filenames.append(k)
    ## sort
    dirnames.sort()
    filenames.sort()
    ## yield
    if topdown:
        yield dirpath, dirnames, filenames, top
    for dn in dirnames:
        d = top.Get(dn)
        for x in walk(d, topdown):
            yield x
    if not topdown:
        yield dirpath, dirnames, filenames, top

#______________________________________________________________________________
def glob_list(li):
    file_names = []
    for fn in li:
        if fn.count('*'):
            file_names.extend(glob.glob(fn))
        else:
            file_names.append(fn)
    return file_names

#------------------------------------------------------------------------------
# HistGetter Class
#------------------------------------------------------------------------------
class HistGetter(object):
    _unique_index = 0 # static class data 
#______________________________________________________________________________
    def __init__(self, files):
        """
        Initializes an instance of HistGetter with some input files given
        by files.  files can be a single file or a list.
        """
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        if not isinstance(files, list):
            files = [files]
        self.file_names = glob_list(files) # glob paths
        if not self.file_names:
            print 
            print " Warning: No file found with glob path(s):"
            for file in files:
                print file
            print 
        self.files = [ ROOT.TFile.Open(fn, 'READ') for fn in self.file_names ]
        self.dirs = self.files
#______________________________________________________________________________
    def __iadd__(self, other):
        self.files += other.files
        self.dirs = self.files
#______________________________________________________________________________
    def __add__(self, other):
        hg = HistGetter()
        hg += self
        hg += other
        return hg
#______________________________________________________________________________
    def __len__(self):
        return len(self.files)
#______________________________________________________________________________
    def get(self, name, rename=''):
        """
        Returns a copy of the ROOT object with name.
        """
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        ## for absoulte paths, dont use current directory.
        ## cd to that path, then get.
        ## WARNING: this changes the cwd
        if name.startswith('/'):
            self.cd()
            name = name[1:]
        hadd = None
        for f in self.dirs:
            f.cd()  # ROOT cd(), not metaroot cd()
            hist = f.Get(name)
            if hist:
                if not isinstance(hist, ROOT.TH1):
                    print 'ERROR: HistGetter.get(name) only supports TH1'
                    return None
                hist = self.make_copy(hist)
                if not hadd:
                    hadd = self.make_copy(hist)
                else:
                    hadd.Add(hist)
            elif verbosity > 1:
                print 'WARNING: %s not found in file: %s' % (name, f.GetName())
        if not hadd and verbosity > 1:
            print 'WARNING: %s not found in any file.' % name
        ## rename hist
        if hadd and rename:
            hadd.SetName( rename )

        return hadd
#______________________________________________________________________________
    def walk(self, top='/', topdown=True):
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.cd(top)
        dirpath = top
        dirnames = self.lsd()
        objnames = self.ls_objects()
        if topdown:
            yield dirpath, dirnames, objnames
        for dn in dirnames:
            for x in self.walk(os.path.join(top, dn), topdown):
                yield x
        if not topdown:
            self.cd(dirpath)
            yield dirpath, dirnames, objnames
#______________________________________________________________________________
    def ls(self):
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        dir = self.dirs[0]
        if dir:
            keys = [ k.GetName() for k in dir.GetListOfKeys() ]
            keys.sort()
            return keys
        else:
            return []
#______________________________________________________________________________
    def lsd(self):
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        return filter( lambda key: isinstance(self.dirs[0].Get(key), ROOT.TDirectory), self.ls() )
#______________________________________________________________________________
    def ls_objects(self):
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        return filter( lambda key: not isinstance(self.dirs[0].Get(key), ROOT.TDirectory), self.ls() )
#______________________________________________________________________________
    def ls_hists(self):
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        return filter( lambda key: isinstance(self.dirs[0].Get(key), ROOT.TH1) or isinstance(self.dirs[0].Get(key), ROOT.TH2), self.ls() )
#______________________________________________________________________________
    def ls_TH1(self):
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        return filter( lambda key: isinstance(self.dirs[0].Get(key), ROOT.TH1) and not isinstance(self.dirs[0].Get(key), ROOT.TH2), self.ls() )
#______________________________________________________________________________
    def ls_TH2(self):
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        return filter( lambda key: isinstance(self.dirs[0].Get(key), ROOT.TH2), self.ls() )
#______________________________________________________________________________
    def ls_graphs(self):
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        return filter( lambda key: isinstance(self.dirs[0].Get(key), ROOT.TGraph)
                                or isinstance(self.dirs[0].Get(key), ROOT.TGraphErrors)
                                or isinstance(self.dirs[0].Get(key), ROOT.TGraphAsymmErrors), self.ls() )
#______________________________________________________________________________
    def cd(self, path=None):
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        if path:
            if path.startswith('/'):
                self.dirs = self.files
                path = path[1:]
            self.dirs = [ d.GetDirectory(path) for d in self.dirs ]
        else:
            self.dirs = self.files
#______________________________________________________________________________
    def close(self):
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        for f in self.files:
            f.Close()
        self.dirs = None
        self.files = None
#______________________________________________________________________________
    def make_copy(self, obj): 
        """
        A helper function to create copy of an object
        """
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        newobj = obj.__class__(obj) # bug?: doesn't have unique name
        HistGetter._unique_index += 1
        return newobj
#______________________________________________________________________________
    def get_type(self, name):
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        if name.startswith('/'):
            self.cd()
            name = name[1:]
        dir = self.dirs[0]
        obj = dir.Get(name)
        return type(obj)

#------------------------------------------------------------------------------
# Sample Class
#------------------------------------------------------------------------------
class Sample2(object):
    """
    Sample2: A class for managing datasets.

    The class is designed to handle two types of samples.
        (1) Datasets. These are data or MC, and they have associated d3pds. Data can have a list of d3pds. MC should have one d3pd.
        (2) Pseudo-datasets. These are data or MC, and they are combinations of datasets.

    Data (pseudo-)datasets should have a lumi. MC datasets should have a xsec. MC pseudo-datasets should have neither.
                         
    D3PD format (bracketed quantities are optional): [user/group.USER/GROUP.]ProjectTag.DSID.FullName.merge.DATATYPE.ProductionTags/
    """
    #__________________________________________________________________________
    def __init__(self, label="", events=0, xsec=0.0, lumi=0.0, d3pds=[], site="", **kw):
        
        # attach attributes
        # -------------------------------------------------------
        self.events = events
        self.xsec   = xsec
        self.lumi   = lumi
        self.d3pds  = d3pds
        self.site   = site
        self.label  = label
        self.dsids  = [self._dsid(d3pd) for d3pd in self.d3pds]
        
        # check for proper input
        # -------------------------------------------------------
        bullet = "\n * "
        if not d3pds:                                  fatal("Sample needs d3pds for dataset navigation.")
        if len(d3pds) != len(list(set(d3pds))):        fatal("Duplicate d3pds exist. %s" % (bullet+bullet.join(filter(lambda d3pd: d3pds.count(d3pd) > 1, list(set(d3pds))))))
        if not xsec and not lumi and not d3pds:        fatal("Need to provide <xsec>, <lumi>, or <d3pds> when creating a Sample2")
        if not lumi and not len(self.d3pds) in [0, 1]: fatal("MC sample has %s d3pds. Should have 1 or 0. %s" % (len(self.d3pds), bullet+bullet.join(self.d3pds)))
        
        # create shortcut for samples with exactly 1 d3pd
        # -------------------------------------------------------
        if len(self.d3pds) == 1:
            self.d3pd = self.d3pds[0]
            self.dsid = self.dsids[0]
        else:
            self.d3pd = None
            self.dsid = None

        # set additional key-word args
        # -------------------------------------------------------
        for k,w in kw.iteritems():
            setattr(self, k, w)

    #__________________________________________________________________________
    def search(self, parentdir, filetag="*.root*"):
        """
        Case 1: Not a rucio filesystem.

        Return a list of strings which look in parentdir for dirs like *d3pd*, and then look in those for filetag.
        Eg: search('/xrootd/', '*tnt.root*') returns ['/xrootd/*sample.d3pd*/*tnt.root*']
        """
        return [os.path.join(parentdir, "*%s*" % d3pd.rstrip("/"), filetag) for d3pd in self.d3pds]

    #__________________________________________________________________________
    def search_rucio(self, datasets, filetag=".root", local="UPENN_LOCALGROUPDISK"):
        """
        Case 2: A rucio filesystem (srm/atlaslocalgroupdisk).

        Return a list of filenames parsed from rucio-ls output. local defines where to look for files.

        Eg: search('user.tuna.*Muons*periodB*v00/', 'skim.root') returns a list of files.

        NB: The Penn prefix for reverse-lookup is srm://srm.hep.upenn.edu:8443/srm/v2/server?SFN=/disk/space00/srm/atlaslocalgroupdisk/rucio/user/tuna/
        """
        import subprocess
        files = []
        srm = "srm/atlaslocalgroupdisk/"
        if not isinstance(datasets, list):
            datasets = [datasets]
        for dataset in datasets:
            cmd = "rucio-ls -pfL %s %s" % (local, dataset)
            proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            stdout,stderr = proc.communicate()
            for line in stdout.split("\n"):
                if line.startswith("srm://") and filetag in line:
                    line = line.strip()
                    if not srm in line:
                        fatal("Only configured for filesystems like srm/atlaslocalgroupdisk/. Blame DAST.")
                    file = os.path.join("/xrootd/", srm, line.split(srm)[1])
                    files.append(file)
        # remove duplicates and sort
        files = list(set(files))
        files_rucio    = sorted(filter(lambda fi:     "/rucio/" in fi, files), key=os.path.basename)
        files_notrucio = sorted(filter(lambda fi: not "/rucio/" in fi, files))

        return files_rucio+files_notrucio
    #__________________________________________________________________________
    def load(self, files):
        """ Create a hist-getter for retrieving histograms. """
        self.hist_getter = HistGetter(files)
    #__________________________________________________________________________
    def get(self, name, rename=''):
        """ Retrieve histograms via hist-getter. """
        h = self.hist_getter.get(name, rename)
        if h:
            if not h.GetSumw2N():
                h.Sumw2()
        else:
            pass # some samples wont pass cuts. no histogram is okay.
        return h
    #__________________________________________________________________________
    def _dsid(self, d3pd):
        """ Return dsid from a d3pd. """
        prefixes = d3pd.count('group.') + d3pd.count('user.')
        return d3pd.split('.')[1 + 2*prefixes]
    #__________________________________________________________________________
    def walk(self, top='/', topdown=True):
        """ Walk through the directories of a hist-getter. """
        self.cd(top)
        dirpath = top
        dirnames = self.lsd()
        objnames = self.ls_objects()
        if topdown:
            yield dirpath, dirnames, objnames
        for dn in dirnames:
            for x in self.walk(os.path.join(top, dn), topdown):
                yield x
        if not topdown:
            self.cd(dirpath)
            yield dirpath, dirnames, objnames
    #__________________________________________________________________________
    def ls(self):
        return self.hist_getter.ls()
    #__________________________________________________________________________
    def lsd(self):
        return self.hist_getter.lsd()
    #__________________________________________________________________________
    def ls_objects(self):
        return self.hist_getter.ls_objects()
    #__________________________________________________________________________
    def ls_hists(self):
        return self.hist_getter.ls_hists()
    #__________________________________________________________________________
    def ls_TH1(self):
        return self.hist_getter.ls_TH1()
    #__________________________________________________________________________
    def ls_TH2(self):
        return self.hist_getter.ls_TH2()
    #__________________________________________________________________________
    def ls_graphs(self):
        return self.hist_getter.ls_graphs()
    #__________________________________________________________________________
    def cd(self, path=None):
        self.hist_getter.cd(path)
    #__________________________________________________________________________
    def close(self):
        self.hist_getter.close()

# -----------------------------------------------------------------
def shortenD3PD(d3pd, generators=False, underscores=False):
    """
    Function to convert d3pd string to smaller string.
    """
    _d3pd = d3pd
    # tunes
    _d3pd = _d3pd.replace('Auto'         , '')
    _d3pd = _d3pd.replace('A2CTEQ6L1'    , '')
    _d3pd = _d3pd.replace('AUET2BCTEQ6L1', '')
    _d3pd = _d3pd.replace('AUET2CTEQ6L1' , '')
    _d3pd = _d3pd.replace('AUET2CT10'    , '')
    _d3pd = _d3pd.replace('AUET3CTEQ6L1' , '')
    _d3pd = _d3pd.replace('AU2CTEQ6L1'   , '')
    _d3pd = _d3pd.replace('AU2MSTW2008LO', '')
    _d3pd = _d3pd.replace('AU2'          , '')
    _d3pd = _d3pd.replace('CT10'         , '')
    _d3pd = _d3pd.replace('P2011C'       , '')
    _d3pd = _d3pd.replace('P2012'        , '')
    # physics
    _d3pd = _d3pd.replace('LeptonFilter'  , '')
    _d3pd = _d3pd.replace('pt20'          , '')
    _d3pd = _d3pd.replace('Mll150to250'   , '150M250')
    _d3pd = _d3pd.replace('Mll250to400'   , '250M400')
    _d3pd = _d3pd.replace('Mll400'        , 'M400')
    _d3pd = _d3pd.replace('Excl_Mll10to60', 'M10to60')
    _d3pd = _d3pd.replace('Incl_Mll10to60', 'M10to60')
    # misc
    _d3pd = _d3pd.replace('jetjet'    , '')
    _d3pd = _d3pd.replace('.merge.'   , '.')
    _d3pd = _d3pd.replace('physics_'  , '')
    _d3pd = _d3pd.replace('_tautau_'  , '')
    _d3pd = _d3pd.replace('tautaulh'  , '')
    _d3pd = _d3pd.replace('unfiltered', '')
    _d3pd = _d3pd.replace('ATau'      , '')
    # sample-specific
    _d3pd = _d3pd.replace('Ztoee2JetsEW1JetQCD15GeVM40_min_n_tchannels', 'ZeeEW'    )
    _d3pd = _d3pd.replace('Ztomm2JetsEW1JetQCD15GeVM40_min_n_tchannels', 'ZmumuEW'  )
    _d3pd = _d3pd.replace('Ztott2JetsEW1JetQCD15GeVM40_min_n_tchannels', 'ZtautauEW')
    _d3pd = _d3pd.replace('Wenu2JetsEW1JetQCD15GeV_min_n_tchannels'    , 'WenuEW'   )
    _d3pd = _d3pd.replace('Wmunu2JetsEW1JetQCD15GeV_min_n_tchannels'   , 'WmunuEW'  )
    _d3pd = _d3pd.replace('Wtaunu2JetsEW1JetQCD15GeV_min_n_tchannels'  , 'WtaunuEW' )
    _d3pd = _d3pd.replace('WpWm', 'WW')
    _d3pd = _d3pd.replace('SingleTop', 'top')
    _d3pd = _d3pd.replace('singletop', 'top')
    _d3pd = _d3pd.replace('_tchan_'    , 'T'   )
    _d3pd = _d3pd.replace('SChanWenu'  , 'Se'  )
    _d3pd = _d3pd.replace('SChanWmunu' , 'Smu' )
    _d3pd = _d3pd.replace('SChanWtaunu', 'Stau')
    _d3pd = _d3pd.replace('WtChanIncl' , 'W'   )
    # generators
    if not generators:
        _d3pd = _d3pd.replace('AcerMC'   , '')
        _d3pd = _d3pd.replace('Alpgen'   , '')
        _d3pd = _d3pd.replace('gg2WW0240', '')
        _d3pd = _d3pd.replace('Herwig'   , '')
        _d3pd = _d3pd.replace('Jimmy'    , '')
        _d3pd = _d3pd.replace('JIMMY'    , '')
        _d3pd = _d3pd.replace('McAtNlo'  , '')
        _d3pd = _d3pd.replace('PowHeg'   , '')
        _d3pd = _d3pd.replace('Powheg'   , '')
        _d3pd = _d3pd.replace('Pythia8'  , '')
        _d3pd = _d3pd.replace('Pythia6'  , '')
        _d3pd = _d3pd.replace('Pythia'   , '')
        _d3pd = _d3pd.replace('pythia'   , '')
        _d3pd = _d3pd.replace('Sherpa'   , '')
        _d3pd = _d3pd.replace('gg2WW0240_JIMMY_WW_', 'gg2WW_')
    # punctuation
    _d3pd = _d3pd.replace('.....', '.')
    _d3pd = _d3pd.replace('....' , '.')
    _d3pd = _d3pd.replace('...'  , '.')
    _d3pd = _d3pd.replace('..'   , '.')
    _d3pd = _d3pd.replace('____' , '_' )
    _d3pd = _d3pd.replace('___'  , '_' )
    _d3pd = _d3pd.replace('__'   , '_' )
    _d3pd = _d3pd.replace('._'   , '.')
    _d3pd = _d3pd.replace('_.'   , '.')
    if not underscores:
        _d3pd = _d3pd.replace('_', '')

    return _d3pd

#______________________________________________________________________________
def set_type(samp, samptype):
    if isinstance(samp, Sample2):
        samp.type = samptype
    elif isinstance(samp, list):
        for sampitem in samp:
            if isinstance(sampitem, Sample2):
                sampitem.type = samptype
    elif isinstance(samp, dict):
        for sampitem in samp.values():
            if isinstance(sampitem, Sample2):
                sampitem.type = samptype
    else:
        pass
#______________________________________________________________________________
def fatal(message):
    sys.exit("Fatal error in %s: %s" % (__file__, message))

# EOF
