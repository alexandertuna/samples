import Sample
from Sample import Sample2

# -----------------------------------------------------------------------------
# Notes:
#       xsec in 1/pb. lumi in pb.
# -----------------------------------------------------------------------------
class Object(): pass

data              = Object()
data.Muons        = Object()
data.Egamma       = Object()
data.JetTauEtmiss = Object()
embedding         = Object()
mc                = Object()

# -----------------------------------------------------------------------------
# Lumis
# -----------------------------------------------------------------------------

lumiA = 794.017
lumiB = 5094.68
lumiC = 1406.02
lumiD = 3288.39
lumiE = 2526.28
lumiG = 1274.81
lumiH = 1444.93
lumiI = 1016.26
lumiJ = 2596.34
lumiL = 839.765

lumiAtoL = 20281.4

# -----------------------------------------------------------------------------
# Data samples
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Muons
# -----------------------------------------------------------------------------

data.Muons.periodA = Sample2(events =  43661420, lumi = lumiA, site = "MWT2_UC_PERF-TAU",     d3pds = ["data12_8TeV.periodA.physics_Muons.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.Muons.periodB = Sample2(events = 163295105, lumi = lumiB, site = "MWT2_UC_PERF-TAU",     d3pds = ["data12_8TeV.periodB.physics_Muons.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.Muons.periodC = Sample2(events =  80935368, lumi = lumiC, site = "MWT2_UC_PERF-TAU",     d3pds = ["data12_8TeV.periodC.physics_Muons.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.Muons.periodD = Sample2(events = 112743915, lumi = lumiD, site = "MWT2_UC_PERF-TAU",     d3pds = ["data12_8TeV.periodD.physics_Muons.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.Muons.periodE = Sample2(events =  81667914, lumi = lumiE, site = "MWT2_UC_PERF-TAU",     d3pds = ["data12_8TeV.periodE.physics_Muons.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.Muons.periodG = Sample2(events =  41182058, lumi = lumiG, site = "MWT2_UC_PERF-TAU",     d3pds = ["data12_8TeV.periodG.physics_Muons.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.Muons.periodH = Sample2(events =  49412952, lumi = lumiH, site = "MWT2_UC_PERF-TAU",     d3pds = ["data12_8TeV.periodH.physics_Muons.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.Muons.periodI = Sample2(events =  34765048, lumi = lumiI, site = "TAIWAN-LCG2_PERF-TAU", d3pds = ["data12_8TeV.periodI.physics_Muons.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.Muons.periodJ = Sample2(events =  88410196, lumi = lumiJ, site = "TAIWAN-LCG2_PERF-TAU", d3pds = ["data12_8TeV.periodJ.physics_Muons.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.Muons.periodL = Sample2(events =  29040147, lumi = lumiL, site = "TAIWAN-LCG2_PERF-TAU", d3pds = ["data12_8TeV.periodL.physics_Muons.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.Muons.periodAtoLs = [data.Muons.periodA,
                          data.Muons.periodB,
                          data.Muons.periodC,
                          data.Muons.periodD,
                          data.Muons.periodE,
                          data.Muons.periodG,
                          data.Muons.periodH,
                          data.Muons.periodI,
                          data.Muons.periodJ,
                          data.Muons.periodL,
                          ]
data.Muons.periodAtoL = Sample2(label = "Data 2012", lumi = lumiAtoL, d3pds = ["data12_8TeV.periodAtoL.Muons.merge"])

# -----------------------------------------------------------------------------
# Egamma
# -----------------------------------------------------------------------------

data.Egamma.periodA = Sample2(events =  43229382, lumi = lumiA, site = "MWT2_UC_PERF-TAU",     d3pds = ["data12_8TeV.periodA.physics_Egamma.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.Egamma.periodB = Sample2(events = 177514740, lumi = lumiB, site = "MWT2_UC_PERF-TAU",     d3pds = ["data12_8TeV.periodB.physics_Egamma.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.Egamma.periodC = Sample2(events =  51322976, lumi = lumiC, site = "MWT2_UC_PERF-TAU",     d3pds = ["data12_8TeV.periodC.physics_Egamma.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.Egamma.periodD = Sample2(events = 113174461, lumi = lumiD, site = "MWT2_UC_PERF-TAU",     d3pds = ["data12_8TeV.periodD.physics_Egamma.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.Egamma.periodE = Sample2(events =  86652109, lumi = lumiE, site = "MWT2_UC_PERF-TAU",     d3pds = ["data12_8TeV.periodE.physics_Egamma.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.Egamma.periodG = Sample2(events =  43857431, lumi = lumiG, site = "MWT2_UC_PERF-TAU",     d3pds = ["data12_8TeV.periodG.physics_Egamma.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.Egamma.periodH = Sample2(events =  53569883, lumi = lumiH, site = "MWT2_UC_PERF-TAU",     d3pds = ["data12_8TeV.periodH.physics_Egamma.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.Egamma.periodI = Sample2(events =  36739595, lumi = lumiI, site = "TAIWAN-LCG2_PERF-TAU", d3pds = ["data12_8TeV.periodI.physics_Egamma.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.Egamma.periodJ = Sample2(events =  95315250, lumi = lumiJ, site = "TAIWAN-LCG2_PERF-TAU", d3pds = ["data12_8TeV.periodJ.physics_Egamma.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.Egamma.periodL = Sample2(events =  30668107, lumi = lumiL, site = "TAIWAN-LCG2_PERF-TAU", d3pds = ["data12_8TeV.periodL.physics_Egamma.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
                              
data.Egamma.periodAtoLs = [data.Egamma.periodA,
                           data.Egamma.periodB,
                           data.Egamma.periodC,
                           data.Egamma.periodD,
                           data.Egamma.periodE,
                           data.Egamma.periodG,
                           data.Egamma.periodH,
                           data.Egamma.periodI,
                           data.Egamma.periodJ,
                           data.Egamma.periodL,
                           ]
data.Egamma.periodAtoL = Sample2(label = "Data 2012", lumi = lumiAtoL, d3pds = ["data12_8TeV.periodAtoL.Egamma.merge"])
        
# -----------------------------------------------------------------------------
# JetTauEtmiss
# -----------------------------------------------------------------------------

data.JetTauEtmiss.periodA = Sample2(events =  64589804, lumi = lumiA, site = "MWT2_UC_PERF-TAU",     d3pds = ["data12_8TeV.periodA.physics_JetTauEtmiss.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.JetTauEtmiss.periodB = Sample2(events = 188983092, lumi = lumiB, site = "MWT2_UC_PERF-TAU",     d3pds = ["data12_8TeV.periodB.physics_JetTauEtmiss.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.JetTauEtmiss.periodC = Sample2(events =  53772444, lumi = lumiC, site = "MWT2_UC_PERF-TAU",     d3pds = ["data12_8TeV.periodC.physics_JetTauEtmiss.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.JetTauEtmiss.periodD = Sample2(events = 121415972, lumi = lumiD, site = "MWT2_UC_PERF-TAU",     d3pds = ["data12_8TeV.periodD.physics_JetTauEtmiss.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.JetTauEtmiss.periodE = Sample2(events = 111745415, lumi = lumiE, site = "MWT2_UC_PERF-TAU",     d3pds = ["data12_8TeV.periodE.physics_JetTauEtmiss.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.JetTauEtmiss.periodG = Sample2(events =  57091146, lumi = lumiG, site = "MWT2_UC_PERF-TAU",     d3pds = ["data12_8TeV.periodG.physics_JetTauEtmiss.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.JetTauEtmiss.periodH = Sample2(events =  66760398, lumi = lumiH, site = "MWT2_UC_PERF-TAU",     d3pds = ["data12_8TeV.periodH.physics_JetTauEtmiss.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.JetTauEtmiss.periodI = Sample2(events =  48321892, lumi = lumiI, site = "TAIWAN-LCG2_PERF-TAU", d3pds = ["data12_8TeV.periodI.physics_JetTauEtmiss.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.JetTauEtmiss.periodJ = Sample2(events = 117709273, lumi = lumiJ, site = "TAIWAN-LCG2_PERF-TAU", d3pds = ["data12_8TeV.periodJ.physics_JetTauEtmiss.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
data.JetTauEtmiss.periodL = Sample2(events =  39979657, lumi = lumiL, site = "TAIWAN-LCG2_PERF-TAU", d3pds = ["data12_8TeV.periodL.physics_JetTauEtmiss.PhysCont.NTUP_TAU.grp14_v01_p1443/"])
                                    
data.JetTauEtmiss.periodAtoLs = [data.JetTauEtmiss.periodA,
                                 data.JetTauEtmiss.periodB,
                                 data.JetTauEtmiss.periodC,
                                 data.JetTauEtmiss.periodD,
                                 data.JetTauEtmiss.periodE,
                                 data.JetTauEtmiss.periodG,
                                 data.JetTauEtmiss.periodH,
                                 data.JetTauEtmiss.periodI,
                                 data.JetTauEtmiss.periodJ,
                                 data.JetTauEtmiss.periodL,
                                 ]
data.JetTauEtmiss.periodAtoL = Sample2(label = "Data 2012", lumi = lumiAtoL, d3pds = ["data12_8TeV.periodAtoL.JetTauEtmiss.merge"])

# -----------------------------------------------------------------------------
# Dummy samples 
# -----------------------------------------------------------------------------

data.multijet           = Sample2(label = "multi-j",                              d3pds = ["data12_8TeV.multijet.merge"])
data.samesign           = Sample2(label = "Data 2012 (SS)",                       d3pds = ["data12_8TeV.samesign.merge"])
data.faketaus           = Sample2(label = "jet->#tau#lower[0.4]{#scale[0.6]{h}}", d3pds = ["data12_8TeV.faketaus.merge"])
data.OSminusSS_faketaus = Sample2(label = "jet->#tau#lower[0.4]{#scale[0.6]{h}}", d3pds = ["data12_8TeV.faketaus.OSminusSS"])
data.fakeleps           = Sample2(label = "jet->l",                               d3pds = ["data12_8TeV.fakeleps.merge"])
data.OSminusSS_fakeleps = Sample2(label = "jet->l",                               d3pds = ["data12_8TeV.fakeleps.OSminusSS"])

# -----------------------------------------------------------------------------
# Embedding samples -- None for p1443.
# -----------------------------------------------------------------------------

# Set sample types.
for _samp in data.Muons.__dict__.values():
    Sample.set_type(_samp, "data12-Muons")
for _samp in data.Egamma.__dict__.values():
    Sample.set_type(_samp, "data12-Egamma")
for _samp in data.JetTauEtmiss.__dict__.values():
    Sample.set_type(_samp, "data12-JetTauEtmiss")
for _samp in mc.__dict__.values():
    Sample.set_type(_samp, "mc12")
for _samp in embedding.__dict__.values():
    Sample.set_type(_samp, "embedding")

# EOF
