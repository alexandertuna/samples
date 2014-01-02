"""
samples:
    A collection of samples, grouped by production.
"""
# import p1130
# import p1286
import p1344
import p1443
import p1462

import copy
import sys

def fatal(message):
    sys.exit("Fatal error in %s: %s" % (__file__, message))

def get(ptag, inputs):
    """
    Function to convert string to list of samples.
    Example string: data.Muons.periodA,mc.ZeeNpXs,mc.ttbar,embedding.periodB
    """
    if not ptag   : fatal("Need production tag.")
    if not inputs : fatal("Need list of inputs.")
    if not isinstance(inputs, list):
        inputs = inputs.split(',') # now a list
    
    # build list of samples
    samples = []
    for inp in inputs:
        # retrieve sample
        try:
            sample = eval("%s.%s" % (ptag, inp))
        except:
            try:
                # check for runs
                stream = '.'.join(inp.split('.')[:-1])
                run = inp.split('.')[-1]
                sample = eval("%s.%s.runs['%s']" % (ptag, stream, run))
            except:
                fatal("Unrecognized sample '%s'" % inp)
        # add sample
        if isinstance(sample, list):
            samples.extend(copy.copy(sample))
        else:
            samples.append(copy.copy(sample))
    return samples

def find_replicas(d3pd):
    import os
    os.system("dq2-list-dataset-replicas-container %s" % d3pd)

def size(dataset):
    import subprocess
    cmd = "rucio-ls -pfL UPENN_LOCALGROUPDISK %s" % dataset
    print "> %s" % cmd
    print
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    stdout,stderr = proc.communicate()
    firstline = True
    for line in stdout.split("\n"):
        line = line.strip()
        if line and firstline:
            # first line contains DSname
            print line
            firstline = False
        if line.startswith("total files:"):
            print line
        if line.startswith("local files:"):
            print line
        if line.startswith("total size:" ):
            bytesize = float(line.split("total size:")[1])
            print "total size: %15i  B" % (bytesize)
            print "total size: %15.2f GB" % (bytesize/pow(1024, 3))
            print "total size: %15.2f TB" % (bytesize/pow(1024, 4))
    print

def eventsAMI(d3pd, usr=None, pw=None):
    import pyAMI.pyAMI as AMI
    if not usr:
        usr = raw_input(" AMI username: ")
    if not pw:
        import getpass
        pw = getpass.getpass(" AMI password: ")
    client = AMI.AMI(False)
    cmd  = []
    cmd += ['getDatasetInfo']
    cmd += ['logicalDatasetName=%s' % d3pd]
    cmd += ['AMIUser=%s'            %  usr]
    cmd += ['AMIPass=%s'            %   pw]
    exe = client.execute(cmd)
    outdict = exe.getDict()
    return int(outdict['Element_Info']['row_1']['totalEvents'])

# EOF
