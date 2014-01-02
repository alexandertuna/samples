import Sample
from Sample import Sample2

# -----------------------------------------------------------------------------
# Notes:
#       xsec in 1/pb. lumi in pb.
# -----------------------------------------------------------------------------
class Object(): pass
embedding   = Object()
embeddingUP = Object()
embeddingDN = Object()

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
# data samples
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# MC samples
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Embedding samples
# -----------------------------------------------------------------------------

# nominal
embedding.periodA = Sample2(events =  455398, lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodA.physics_Muons.PhysCont.NTUP_EMBLHIM.grp14_v02_r4697_p1462/"])
embedding.periodB = Sample2(events = 3054800, lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodB.physics_Muons.PhysCont.NTUP_EMBLHIM.grp14_v02_r4697_p1462/"])
embedding.periodC = Sample2(events =  837026, lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodC.physics_Muons.PhysCont.NTUP_EMBLHIM.grp14_v02_r4697_p1462/"])
embedding.periodD = Sample2(events = 1946864, lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodD.physics_Muons.PhysCont.NTUP_EMBLHIM.grp14_v02_r4697_p1462/"])
embedding.periodE = Sample2(events = 1542591, lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodE.physics_Muons.PhysCont.NTUP_EMBLHIM.grp14_v02_r4697_p1462/"])
embedding.periodG = Sample2(events =  773817, lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodG.physics_Muons.PhysCont.NTUP_EMBLHIM.grp14_v02_r4697_p1462/"])
embedding.periodH = Sample2(events =  898006, lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodH.physics_Muons.PhysCont.NTUP_EMBLHIM.grp14_v02_r4697_p1462/"])
embedding.periodI = Sample2(events =  627090, lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodI.physics_Muons.PhysCont.NTUP_EMBLHIM.grp14_v02_r4697_p1462/"])
embedding.periodJ = Sample2(events = 1596347, lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodJ.physics_Muons.PhysCont.NTUP_EMBLHIM.grp14_v02_r4697_p1462/"])
embedding.periodL = Sample2(events =  523619, lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodL.physics_Muons.PhysCont.NTUP_EMBLHIM.grp14_v02_r4697_p1462/"])
                            
embedding.periodAtoLs = [embedding.periodA,
                         embedding.periodB,
                         embedding.periodC,
                         embedding.periodD,
                         embedding.periodE,
                         embedding.periodG,
                         embedding.periodH,
                         embedding.periodI,
                         embedding.periodJ,
                         embedding.periodL,
                         ]
embedding.periodAtoL = Sample2(label = "Z^{emb.}->#tau#tau", lumi = lumiAtoL, d3pds = ["data12_8TeV.periodAtoL.embedding.merge"])

# mfsup
embeddingUP.periodA = Sample2(lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodA.physics_Muons.PhysCont.NTUP_EMBLHUP.grp14_v02_r4697_p1462/"])
embeddingUP.periodB = Sample2(lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodB.physics_Muons.PhysCont.NTUP_EMBLHUP.grp14_v02_r4697_p1462/"])
embeddingUP.periodC = Sample2(lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodC.physics_Muons.PhysCont.NTUP_EMBLHUP.grp14_v02_r4697_p1462/"])
embeddingUP.periodD = Sample2(lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodD.physics_Muons.PhysCont.NTUP_EMBLHUP.grp14_v02_r4697_p1462/"])
embeddingUP.periodE = Sample2(lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodE.physics_Muons.PhysCont.NTUP_EMBLHUP.grp14_v02_r4697_p1462/"])
embeddingUP.periodG = Sample2(lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodG.physics_Muons.PhysCont.NTUP_EMBLHUP.grp14_v02_r4697_p1462/"])
embeddingUP.periodH = Sample2(lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodH.physics_Muons.PhysCont.NTUP_EMBLHUP.grp14_v02_r4697_p1462/"])
embeddingUP.periodI = Sample2(lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodI.physics_Muons.PhysCont.NTUP_EMBLHUP.grp14_v02_r4697_p1462/"])
embeddingUP.periodJ = Sample2(lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodJ.physics_Muons.PhysCont.NTUP_EMBLHUP.grp14_v02_r4697_p1462/"])
embeddingUP.periodL = Sample2(lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodL.physics_Muons.PhysCont.NTUP_EMBLHUP.grp14_v02_r4697_p1462/"])

# mfsdn
embeddingDN.periodA = Sample2(lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodA.physics_Muons.PhysCont.NTUP_EMBLHDN.grp14_v02_r4697_p1462/"])
embeddingDN.periodB = Sample2(lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodB.physics_Muons.PhysCont.NTUP_EMBLHDN.grp14_v02_r4697_p1462/"])
embeddingDN.periodC = Sample2(lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodC.physics_Muons.PhysCont.NTUP_EMBLHDN.grp14_v02_r4697_p1462/"])
embeddingDN.periodD = Sample2(lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodD.physics_Muons.PhysCont.NTUP_EMBLHDN.grp14_v02_r4697_p1462/"])
embeddingDN.periodE = Sample2(lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodE.physics_Muons.PhysCont.NTUP_EMBLHDN.grp14_v02_r4697_p1462/"])
embeddingDN.periodG = Sample2(lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodG.physics_Muons.PhysCont.NTUP_EMBLHDN.grp14_v02_r4697_p1462/"])
embeddingDN.periodH = Sample2(lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodH.physics_Muons.PhysCont.NTUP_EMBLHDN.grp14_v02_r4697_p1462/"])
embeddingDN.periodI = Sample2(lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodI.physics_Muons.PhysCont.NTUP_EMBLHDN.grp14_v02_r4697_p1462/"])
embeddingDN.periodJ = Sample2(lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodJ.physics_Muons.PhysCont.NTUP_EMBLHDN.grp14_v02_r4697_p1462/"])
embeddingDN.periodL = Sample2(lumi = -1.0, site = "IN2P3-CC_PHYS-HIGGS", d3pds = ["data12_8TeV.periodL.physics_Muons.PhysCont.NTUP_EMBLHDN.grp14_v02_r4697_p1462/"])

# OS-SS
embedding.OSminusSS_periodAtoL = Sample2(d3pds = ["data12_8TeV.periodAtoL.embedding.OSminusSS"])

for _samp in embedding.__dict__.values():
    Sample.set_type(_samp, "embedding12")
for _samp in embeddingUP.__dict__.values():
    Sample.set_type(_samp, "embedding12-UP")
for _samp in embeddingDN.__dict__.values():
    Sample.set_type(_samp, "embedding12-DN")

# EOF
