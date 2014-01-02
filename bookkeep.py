"""
bookkeep.py -- For bookkeeping skims/ntuples.

-i, --input
    The directory of datasets.

-m, --metadata
    The name of the metadata hist.
    Examples:
        Michels skims:     'cutflow'
        Melbourne ntuples: 'TotalEvents'
        Penn TNTs:         'h_cut_flow_preselection'

-o, --output
    The name of the output file where the twiki-formatted
    table is dumped.

Authors: Alex Tuna <tuna@cern.ch>
Created: 2012-11-27 <tuna>
Updated: 2013-01-18 <tuna>
"""
import argparse
import os
import glob
import ROOT
import sys
import time
import warnings

time = time.strftime('%Y-%m-%d-%Hh%Mm%Ss')
warnings.filterwarnings(action="ignore", category=RuntimeWarning)

def fatal(message):
    sys.exit("Fatal error in %s: %s" % (__file__, message))

# args
parser = argparse.ArgumentParser()
parser.add_argument('--input'    , default=None                  , help="path to directory of datasets" )
parser.add_argument('--metadata' , default='h_cut_flow_raw_tnt'  , help="name of metadata histogram"    )
parser.add_argument('--ptag'     , default=None                  , help="production tag of tau d3pds"   )
parser.add_argument('--output'   , default='table.%s.txt' % time , help="name of output file"           )
parser.add_argument('--samples'  , default=None                  , help="samples to bookkeep"           )
parser.add_argument('--tags'     , default=""                    , help="tags to search input directory")
parser.add_argument("--rucio", action="store_true")
ops = parser.parse_args()

# check requirements
if not ops.input and not ops.rucio  : fatal("Need --input directory to retrieve datasets or --rucio option.")
if not ops.ptag                     : fatal("Need --ptag (eg, p1130) to retrieve samples.")
if not ops.samples                  : fatal("Need --sample to bookkeep.")

# samples
try:
    import samples
except ImportError:
    if os.path.basename(os.path.abspath(os.path.curdir)) == "samples":
        import __init__ as samples
    else:
        fatal("Need samples in path.")
samples = samples.get(ops.ptag, ops.samples)

#______________________________________________________________________________
def main():

    # create output
    output = open(ops.output, 'w')
    head = '| *sample* | *# observed events* | *# expected events* | *agree* | *obs/exp* |\n'
    output.write(head)

    # for string formatting
    digits = len(str(len(samples)))
    chars = max([len(sample.d3pd) for sample in samples])

    # create period summaries
    periodsObs = {}
    periodsExp = {}

    # loop over samples
    for sample in samples:

        # dont bookkeep multi-d3pd samples
        if len(sample.d3pds) > 1:
            fatal("Only designed to bookkeep single d3pds. This sample (%s) has %s d3pds." % (sample.d3pd, len(sample.d3pds)))

        # get number of observed and expected events
        eventsExp = sample.events
        eventsObs = 0.0
        if ops.rucio:
            ruciostring = "user.tuna.*%s*%s*/" % (sample.dsid, "*".join(ops.tags.split(",")))
            input = sample.search_rucio(ruciostring)
        else:
            input = sample.search(ops.input)
        for inp in input:
            for inpglob in glob.glob(inp):
                if "/xrootd/" in inpglob:
                    inpglob = inpglob.replace("/xrootd/", "root://hn.at3f//")
                tfile = ROOT.TFile.Open(inpglob)
                metadataTH1 = tfile.Get(ops.metadata)
                if metadataTH1:
                    eventsObs += metadataTH1.GetBinContent(1)
                else:
                    print
                    print "Warning, metadata %s not retrieved for file %s" % (ops.metadata, inpglob)
                    print
                tfile.Close()

        # fill table
        output.write(row(sample.d3pd, eventsObs, eventsExp))

        # squawk
        result = "AGREE" if eventsExp == eventsObs else "DISAGREE"
        print "[%-*s / %-*s] %-*s %12s %12s %12s" % (digits, samples.index(sample),
                                                     digits, len(samples)-1,
                                                     chars, sample.d3pd,
                                                     int(eventsObs),
                                                     int(eventsExp),
                                                     result)

        # bookkeep periods, too
        if sample.lumi:
            if period(sample) in periodsObs:
                periodsObs[period(sample)] += eventsObs
                periodsExp[period(sample)] += eventsExp
            else:
                periodsObs[period(sample)]  = eventsObs
                periodsExp[period(sample)]  = eventsExp

    # check for periods
    for per in sorted(periodsObs):
        output.write(row(per, periodsObs[per], periodsExp[per]))

    # make sum of periods
    if len(periodsObs) > 1:
        per1, per2 = sorted(periodsObs)[0], sorted(periodsObs)[-1]
        stream = per1.split(".")[0]
        per1   = per1.split(".")[1].replace("period", "")
        per2   = per2.split(".")[1].replace("period", "")
        name   = "%s.period%sto%s" % (stream, per1, per2)
        output.write(row(name, sum(periodsObs.values()), sum(periodsExp.values())))

    # close
    output.close()

#______________________________________________________________________________
def row(name, obs, exp):
    name = "=%s=" % name
    agree = "%ICON{choice-yes}%" if obs == exp else "%ICON{choice-no}%"
    if exp != 0:
        fraction = obs / exp
    elif exp == obs == 0:
        fraction = 1.0
    else:
        fraction = 0.0
    return "| %s | %i | %i | %s | %.3f |\n" % (name, obs, exp, agree, fraction)

#______________________________________________________________________________
def period(sample):
    if not sample:
        fatal("No sample given to period().")
    if "period" in sample.d3pd:
        return sample.d3pd
    else:
        dsid = int(sample.dsid)
        if 200804 <= dsid <= 201556: return name+".periodA"
        if 202660 <= dsid <= 205113: return name+".periodB"
        if 206248 <= dsid <= 207397: return name+".periodC"
        if 207447 <= dsid <= 209025: return name+".periodD"
        if 209074 <= dsid <= 210308: return name+".periodE"
        if 211522 <= dsid <= 212272: return name+".periodG"
        if 212619 <= dsid <= 213359: return name+".periodH"
        if 213431 <= dsid <= 213819: return name+".periodI"
        if 213900 <= dsid <= 215091: return name+".periodJ"
        if 215414 <= dsid <= 215643: return name+".periodL"
        if 216399 <= dsid <= 216432: return name+".periodM"
    fatal("Unable to match dsid to period.")

#______________________________________________________________________________
if __name__ == "__main__": main()
