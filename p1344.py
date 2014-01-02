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
# data samples (none)
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# embedding samples (none)
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# MC samples
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Wenu
# -----------------------------------------------------------------------------

mc.WenuAHNp0 = Sample2(events = 499899, xsec = 8037.100*1.19, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107680.AlpgenJimmy_AUET2CTEQ6L1_WenuNp0.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.WenuAHNp1 = Sample2(events = 199900, xsec = 1579.200*1.19, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107681.AlpgenJimmy_AUET2CTEQ6L1_WenuNp1.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.WenuAHNp2 = Sample2(events =  99900, xsec =  477.200*1.19, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107682.AlpgenJimmy_AUET2CTEQ6L1_WenuNp2.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.WenuAHNp3 = Sample2(events =  50000, xsec =  133.930*1.19, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107683.AlpgenJimmy_AUET2CTEQ6L1_WenuNp3.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.WenuAHNp4 = Sample2(events =  20000, xsec =   35.622*1.19, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107684.AlpgenJimmy_AUET2CTEQ6L1_WenuNp4.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.WenuAHNp5 = Sample2(events =  10000, xsec =   10.553*1.19, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107685.AlpgenJimmy_AUET2CTEQ6L1_WenuNp5.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.WenuAHNpXs = [mc.WenuAHNp0, mc.WenuAHNp1, mc.WenuAHNp2, mc.WenuAHNp3, mc.WenuAHNp4, mc.WenuAHNp5]

mc.WenuAHVBFNp3 = Sample2(events = 1569697, xsec = 133.930*1.19*0.13969, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.169553.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_WenuNp3.merge.NTUP_TAU.e1747_s1581_s1586_r3658_r3549_p1344/'])
mc.WenuAHVBFNp4 = Sample2(events =  968998, xsec =  35.622*1.19*0.27346, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.169554.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_WenuNp4.merge.NTUP_TAU.e1747_s1581_s1586_r3658_r3549_p1344/'])
mc.WenuAHVBFNp5 = Sample2(events =  549436, xsec =  10.553*1.19*0.46258, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.169555.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_WenuNp5.merge.NTUP_TAU.e1747_s1581_s1586_r3658_r3549_p1344/'])
mc.WenuAHVBFNpXs = [mc.WenuAHVBFNp3, mc.WenuAHVBFNp4, mc.WenuAHVBFNp5]

mc.WenuAPNp0 = Sample2(events =  9494882, xsec = 8136.800*1.15, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147025.AlpgenPythia_Auto_P2011C_WenuNp0.merge.NTUP_TAU.e1879_s1581_s1586_r3658_r3549_p1344/'])
mc.WenuAPNp1 = Sample2(events = 26298052, xsec = 1791.500*1.15, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147026.AlpgenPythia_Auto_P2011C_WenuNp1.merge.NTUP_TAU.e1879_s1581_s1586_r3658_r3549_p1344/'])
mc.WenuAPNp2 = Sample2(events = 17569347, xsec =  541.600*1.15, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147027.AlpgenPythia_Auto_P2011C_WenuNp2.merge.NTUP_TAU.e1879_s1581_s1586_r3658_r3549_p1344/'])
mc.WenuAPNp3 = Sample2(events =  4985287, xsec =  146.650*1.15, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147028.AlpgenPythia_Auto_P2011C_WenuNp3.merge.NTUP_TAU.e1879_s1581_s1586_r3658_r3549_p1344/'])
mc.WenuAPNp4 = Sample2(events =  2553792, xsec =   37.295*1.15, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147029.AlpgenPythia_Auto_P2011C_WenuNp4.merge.NTUP_TAU.e1879_s1581_s1586_r3658_r3549_p1344/'])
mc.WenuAPNp5 = Sample2(events =   799192, xsec =   11.369*1.15, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147030.AlpgenPythia_Auto_P2011C_WenuNp5incl.merge.NTUP_TAU.e1879_s1581_s1586_r3658_r3549_p1344/'])
mc.WenuAPNpXs = [mc.WenuAPNp0, mc.WenuAPNp1, mc.WenuAPNp2, mc.WenuAPNp3, mc.WenuAPNp4, mc.WenuAPNp5]

mc.WenuEW = Sample2(label = "W^{EW}->e#nu", events = 1997790, xsec = 4.2114, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.129915.Sherpa_CT10_Wenu2JetsEW1JetQCD15GeV_min_n_tchannels.merge.NTUP_TAU.e1557_s1499_s1504_r3658_r3549_p1344/'])

# -----------------------------------------------------------------------------
# Wmunu
# NB: AlpgenHerwig Np0,Np4 are missing datasets.
# -----------------------------------------------------------------------------

mc.WmunuAHNp0 = Sample2(events = 499800, xsec = 8040.000*1.19, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107690.AlpgenJimmy_AUET2CTEQ6L1_WmunuNp0.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.WmunuAHNp1 = Sample2(events = 200000, xsec = 1580.300*1.19, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107691.AlpgenJimmy_AUET2CTEQ6L1_WmunuNp1.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.WmunuAHNp2 = Sample2(events = 100000, xsec =  477.500*1.19, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107692.AlpgenJimmy_AUET2CTEQ6L1_WmunuNp2.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.WmunuAHNp3 = Sample2(events =  50000, xsec =  133.940*1.19, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107693.AlpgenJimmy_AUET2CTEQ6L1_WmunuNp3.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.WmunuAHNp4 = Sample2(events =  20000, xsec =   35.636*1.19, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107694.AlpgenJimmy_AUET2CTEQ6L1_WmunuNp4.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.WmunuAHNp5 = Sample2(events =  10000, xsec =   10.571*1.19, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107695.AlpgenJimmy_AUET2CTEQ6L1_WmunuNp5.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.WmunuAHNpXs = [mc.WmunuAHNp0, mc.WmunuAHNp1, mc.WmunuAHNp2, mc.WmunuAHNp3, mc.WmunuAHNp4, mc.WmunuAHNp5]

mc.WmunuAHVBFNp3 = Sample2(events = 1545794, xsec = 133.940*1.19*0.10451, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.169563.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_WmunuNp3.merge.NTUP_TAU.e1747_s1581_s1586_r3658_r3549_p1344/'])
mc.WmunuAHVBFNp4 = Sample2(events =  935298, xsec =  35.636*1.19*0.22895, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.169564.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_WmunuNp4.merge.NTUP_TAU.e1747_s1581_s1586_r3658_r3549_p1344/'])
mc.WmunuAHVBFNp5 = Sample2(events =  548298, xsec =  10.571*1.19*0.41934, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.169565.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_WmunuNp5.merge.NTUP_TAU.e1747_s1581_s1586_r3658_r3549_p1344/'])
mc.WmunuAHVBFNpXs = [mc.WmunuAHVBFNp3, mc.WmunuAHVBFNp4, mc.WmunuAHVBFNp5]

mc.WmunuAPNp0 = Sample2(events = 11999285, xsec = 8133.400*1.15, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147033.AlpgenPythia_Auto_P2011C_WmunuNp0.merge.NTUP_TAU.e1880_s1581_s1586_r3658_r3549_p1344/'])
mc.WmunuAPNp1 = Sample2(events = 26291747, xsec = 1792.700*1.15, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147034.AlpgenPythia_Auto_P2011C_WmunuNp1.merge.NTUP_TAU.e1880_s1581_s1586_r3658_r3549_p1344/'])
mc.WmunuAPNp2 = Sample2(events = 17611454, xsec =  541.270*1.15, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147035.AlpgenPythia_Auto_P2011C_WmunuNp2.merge.NTUP_TAU.e1880_s1581_s1586_r3658_r3549_p1344/'])
mc.WmunuAPNp3 = Sample2(events =  4986077, xsec =  146.490*1.15, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147036.AlpgenPythia_Auto_P2011C_WmunuNp3.merge.NTUP_TAU.e1880_s1581_s1586_r3658_r3549_p1344/'])
mc.WmunuAPNp4 = Sample2(events =  2556595, xsec =   37.334*1.15, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147037.AlpgenPythia_Auto_P2011C_WmunuNp4.merge.NTUP_TAU.e1880_s1581_s1586_r3658_r3549_p1344/'])
mc.WmunuAPNp5 = Sample2(events =   798898, xsec =   11.414*1.15, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147038.AlpgenPythia_Auto_P2011C_WmunuNp5incl.merge.NTUP_TAU.e1880_s1581_s1586_r3658_r3549_p1344/'])
mc.WmunuAPNpXs = [mc.WmunuAPNp0, mc.WmunuAPNp1, mc.WmunuAPNp2, mc.WmunuAPNp3, mc.WmunuAPNp4, mc.WmunuAPNp5]

mc.WmunuEW = Sample2(label = "W^{EW}->#mu#nu", events = 1999195, xsec = 4.2128, d3pds = ['mc12_8TeV.129916.Sherpa_CT10_Wmunu2JetsEW1JetQCD15GeV_min_n_tchannels.merge.NTUP_TAU.e1557_s1499_s1504_r3658_r3549_p1344/'])

# -----------------------------------------------------------------------------
# Wtaunu. NB: samples are missing generally.
# -----------------------------------------------------------------------------

mc.WtaunuAHNp0 = Sample2(events = 495999, xsec = 8035.800*1.19, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107700.AlpgenJimmy_AUET2CTEQ6L1_WtaunuNp0.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.WtaunuAHNp1 = Sample2(events = 199999, xsec = 1579.800*1.19, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107701.AlpgenJimmy_AUET2CTEQ6L1_WtaunuNp1.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.WtaunuAHNp2 = Sample2(events = 100000, xsec =  477.550*1.19, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107702.AlpgenJimmy_AUET2CTEQ6L1_WtaunuNp2.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.WtaunuAHNp3 = Sample2(events =  49999, xsec =  133.790*1.19, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107703.AlpgenJimmy_AUET2CTEQ6L1_WtaunuNp3.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.WtaunuAHNp4 = Sample2(events =  19900, xsec =   35.583*1.19, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107704.AlpgenJimmy_AUET2CTEQ6L1_WtaunuNp4.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.WtaunuAHNp5 = Sample2(events =  10000, xsec =   10.540*1.19, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107705.AlpgenJimmy_AUET2CTEQ6L1_WtaunuNp5.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.WtaunuAHNpXs = [mc.WtaunuAHNp0, mc.WtaunuAHNp1, mc.WtaunuAHNp2, mc.WtaunuAHNp3, mc.WtaunuAHNp4, mc.WtaunuAHNp5]

mc.WtaunuAHVBFNp3 = Sample2(events = 1559194, xsec = 133.790*1.19*0.120380, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.169573.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_WtaunuNp3.merge.NTUP_TAU.e1747_s1581_s1586_r3658_r3549_p1344/'])
mc.WtaunuAHVBFNp4 = Sample2(events =  965595, xsec =  35.583*1.19*0.251200, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.169574.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_WtaunuNp4.merge.NTUP_TAU.e1747_s1581_s1586_r3658_r3549_p1344/'])
mc.WtaunuAHVBFNp5 = Sample2(events =  522419, xsec =  10.540*1.19*0.442310, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.169575.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_WtaunuNp5.merge.NTUP_TAU.e1747_s1581_s1586_r3658_r3549_p1344/'])
mc.WtaunuAHVBFNpXs = [mc.WtaunuAHVBFNp3, mc.WtaunuAHVBFNp4, mc.WtaunuAHVBFNp5]

mc.WtaunuAPNp0 = Sample2(events = -1, xsec = 8135.700*1.15, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147041.AlpgenPythia_Auto_P2011C_WtaunuNp0.merge.NTUP_TAU.e1881_s1581_s1586_r3658_r3549_p1344/'])
mc.WtaunuAPNp1 = Sample2(events = -1, xsec = 1793.700*1.15, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147042.AlpgenPythia_Auto_P2011C_WtaunuNp1.merge.NTUP_TAU.e1881_s1581_s1586_r3658_r3549_p1344/'])
mc.WtaunuAPNp2 = Sample2(events = -1, xsec =  541.240*1.15, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147043.AlpgenPythia_Auto_P2011C_WtaunuNp2.merge.NTUP_TAU.e1881_s1581_s1586_r3658_r3549_p1344/'])
mc.WtaunuAPNp3 = Sample2(events = -1, xsec =  146.480*1.15, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147044.AlpgenPythia_Auto_P2011C_WtaunuNp3.merge.NTUP_TAU.e1881_s1581_s1586_r3658_r3549_p1344/'])
mc.WtaunuAPNp4 = Sample2(events = -1, xsec =   37.264*1.15, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147045.AlpgenPythia_Auto_P2011C_WtaunuNp4.merge.NTUP_TAU.e1881_s1581_s1586_r3658_r3549_p1344/'])
mc.WtaunuAPNp5 = Sample2(events = -1, xsec =   11.537*1.15, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147046.AlpgenPythia_Auto_P2011C_WtaunuNp5incl.merge.NTUP_TAU.e1881_s1581_s1586_r3658_r3549_p1344/'])
mc.WtaunuAPNpXs = [mc.WtaunuAPNp0, mc.WtaunuAPNp1, mc.WtaunuAPNp2, mc.WtaunuAPNp3, mc.WtaunuAPNp4, mc.WtaunuAPNp5]

mc.WtaunuEW = Sample2(label = "W^{EW}->#tau#nu", events = 30000, xsec = 4.2124, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.129917.Sherpa_CT10_Wtaunu2JetsEW1JetQCD15GeV_min_n_tchannels.merge.NTUP_TAU.e1557_s1499_s1504_r3658_r3549_p1344/'])

# -----------------------------------------------------------------------------
# Sherpa W
# -----------------------------------------------------------------------------

mc.WenuSherpaPt0_CJVBV        = Sample2(events = -1, xsec = 11000 * 1.1 * 0.94,         d3pds = ['mc12_8TeV.167742.Sherpa_CT10_WenuMassiveCBPt0_CJetVetoBVeto.merge.NTUP_TAU.e1585_a159_a171_r3549_p1344/'])
mc.WenuSherpaPt70_140_CJVBV   = Sample2(events = -1, xsec = 250.597 * 1.1 * 0.75485,    d3pds = ['mc12_8TeV.167763.Sherpa_CT10_WenuMassiveCBPt70_140_CJetVetoBVeto.merge.NTUP_TAU.e1620_a159_a171_r3549_p1344/'])
mc.WenuSherpaPt140_280_CJVBV  = Sample2(events = -1, xsec = 31.16320 * 1.1 * 0.71609,   d3pds = ['mc12_8TeV.167772.Sherpa_CT10_WenuMassiveCBPt140_280_CJetVetoBVeto.merge.NTUP_TAU.e1620_a159_a171_r3549_p1344/'])
mc.WenuSherpaPt280_500_CJVBV  = Sample2(events = -1, xsec = 1.83740 * 1.1 * 0.68397,    d3pds = ['mc12_8TeV.167781.Sherpa_CT10_WenuMassiveCBPt280_500_CJetVetoBVeto.merge.NTUP_TAU.e1714_s1581_s1586_r3658_r3549_p1344/'])
mc.WenuSherpaPt500_CJVBV      = Sample2(events = -1, xsec = 0.10193 * 1.1 * 0.66004,    d3pds = ['mc12_8TeV.167790.Sherpa_CT10_WenuMassiveCBPt500_CJetVetoBVeto.merge.NTUP_TAU.e1620_s1499_s1504_r3658_r3549_p1344/'])
mc.WenuSherpaPt0_CJFBV        = Sample2(events = -1, xsec = 11000 * 1.1 * 0.048,        d3pds = ['mc12_8TeV.167741.Sherpa_CT10_WenuMassiveCBPt0_CJetFilterBVeto.merge.NTUP_TAU.e1585_a159_a171_r3549_p1344/'])
mc.WenuSherpaPt70_140_CJFBV   = Sample2(events = -1, xsec = 250.59700 * 1.1 * 0.19889,  d3pds = ['mc12_8TeV.167762.Sherpa_CT10_WenuMassiveCBPt70_140_CJetFilterBVeto.merge.NTUP_TAU.e1620_a159_a171_r3549_p1344/'])
mc.WenuSherpaPt140_280_CJFBV  = Sample2(events = -1, xsec = 31.16320 * 1.1 * 0.22015,   d3pds = ['mc12_8TeV.167771.Sherpa_CT10_WenuMassiveCBPt140_280_CJetFilterBVeto.merge.NTUP_TAU.e1620_a159_a171_r3549_p1344/'])
mc.WenuSherpaPt280_500_BF     = Sample2(events = -1, xsec = 1.83740 * 1.1 * 0.23271,    d3pds = ['mc12_8TeV.167779.Sherpa_CT10_WenuMassiveCBPt280_500_BFilter.merge.NTUP_TAU.e1714_s1581_s1586_r3658_r3549_p1344/'])
mc.WenuSherpaPt500_CJFBV      = Sample2(events = -1, xsec = 0.10193 * 1.1 * 0.24221,    d3pds = ['mc12_8TeV.167789.Sherpa_CT10_WenuMassiveCBPt500_CJetFilterBVeto.merge.NTUP_TAU.e1620_s1499_s1504_r3658_r3549_p1344/'])
mc.WenuSherpaPt0_BF           = Sample2(events = -1, xsec = 11000 * 1.1 * 0.012,        d3pds = ['mc12_8TeV.167740.Sherpa_CT10_WenuMassiveCBPt0_BFilter.merge.NTUP_TAU.e1585_a159_a171_r3549_p1344/'])
mc.WenuSherpaPt70_140_BF      = Sample2(events = -1, xsec = 250.59700 * 1.1 * 0.045942, d3pds = ['mc12_8TeV.167761.Sherpa_CT10_WenuMassiveCBPt70_140_BFilter.merge.NTUP_TAU.e1620_a159_a171_r3549_p1344/'])
mc.WenuSherpaPt140_280_BF     = Sample2(events = -1, xsec = 31.16320 * 1.1 * 0.063078,  d3pds = ['mc12_8TeV.167770.Sherpa_CT10_WenuMassiveCBPt140_280_BFilter.merge.NTUP_TAU.e1620_a159_a171_r3549_p1344/'])
mc.WenuSherpaPt280_500_BF     = Sample2(events = -1, xsec = 1.83740 * 1.1 * 0.083026,   d3pds = ['mc12_8TeV.167779.Sherpa_CT10_WenuMassiveCBPt280_500_BFilter.merge.NTUP_TAU.e1714_s1581_s1586_r3658_r3549_p1344/'])
mc.WenuSherpaPt500_BF         = Sample2(events = -1, xsec = 0.10193 * 1.1 * 0.099663,   d3pds = ['mc12_8TeV.167788.Sherpa_CT10_WenuMassiveCBPt500_BFilter.merge.NTUP_TAU.e1620_s1499_s1504_r3658_r3549_p1344/'])
mc.WenuSherpas = [mc.WenuSherpaPt0_CJVBV, mc.WenuSherpaPt70_140_CJVBV, mc.WenuSherpaPt140_280_CJVBV, mc.WenuSherpaPt280_500_CJVBV, mc.WenuSherpaPt500_CJVBV,
                  mc.WenuSherpaPt0_CJFBV, mc.WenuSherpaPt70_140_CJFBV, mc.WenuSherpaPt140_280_CJFBV, mc.WenuSherpaPt280_500_BF,    mc.WenuSherpaPt500_CJFBV,
                  mc.WenuSherpaPt0_BF,    mc.WenuSherpaPt70_140_BF,    mc.WenuSherpaPt140_280_BF,    mc.WenuSherpaPt280_500_BF,    mc.WenuSherpaPt500_BF,
                  ]

mc.WmunuSherpaPt0_CJVBV        = Sample2(events = -1, xsec = 11000 * 1.1 * 0.94,         d3pds = ['mc12_8TeV.167745.Sherpa_CT10_WmunuMassiveCBPt0_CJetVetoBVeto.merge.NTUP_TAU.e1585_a159_a171_r3549_p1344/'])
mc.WmunuSherpaPt70_140_CJVBV   = Sample2(events = -1, xsec = 250.59700 * 1.1 * 0.75485,  d3pds = ['mc12_8TeV.167766.Sherpa_CT10_WmunuMassiveCBPt70_140_CJetVetoBVeto.merge.NTUP_TAU.e1714_a159_a171_r3549_p1344/'])
mc.WmunuSherpaPt140_280_CJVBV  = Sample2(events = -1, xsec = 31.16320 * 1.1 * 0.71609,   d3pds = ['mc12_8TeV.167775.Sherpa_CT10_WmunuMassiveCBPt140_280_CJetVetoBVeto.merge.NTUP_TAU.e1714_a159_a171_r3549_p1344/'])
mc.WmunuSherpaPt280_500_CJVBV  = Sample2(events = -1, xsec = 1.83740 * 1.1 * 1.83740,    d3pds = ['mc12_8TeV.167784.Sherpa_CT10_WmunuMassiveCBPt280_500_CJetVetoBVeto.merge.NTUP_TAU.e1714_s1581_s1586_r3658_r3549_p1344/'])
mc.WmunuSherpaPt500_CJVBV      = Sample2(events = -1, xsec = 0.10193 * 1.1 * 0.66004,    d3pds = ['mc12_8TeV.167793.Sherpa_CT10_WmunuMassiveCBPt500_CJetVetoBVeto.merge.NTUP_TAU.e1714_s1581_s1586_r3658_r3549_p1344/'])
mc.WmunuSherpaPt0_CJFBV        = Sample2(events = -1, xsec = 11000 * 1.1 * 0.048,        d3pds = ['mc12_8TeV.167744.Sherpa_CT10_WmunuMassiveCBPt0_CJetFilterBVeto.merge.NTUP_TAU.e1585_a159_a171_r3549_p1344/'])
mc.WmunuSherpaPt70_140_CJFBV   = Sample2(events = -1, xsec = 250.59700 * 1.1 * 0.19889,  d3pds = ['mc12_8TeV.167765.Sherpa_CT10_WmunuMassiveCBPt70_140_CJetFilterBVeto.merge.NTUP_TAU.e1714_a159_a171_r3549_p1344/'])
mc.WmunuSherpaPt140_280_CJFBV  = Sample2(events = -1, xsec = 31.16320 * 1.1 * 0.22015,   d3pds = ['mc12_8TeV.167774.Sherpa_CT10_WmunuMassiveCBPt140_280_CJetFilterBVeto.merge.NTUP_TAU.e1714_a159_a171_r3549_p1344/'])
mc.WmunuSherpaPt280_500_CJFBV  = Sample2(events = -1, xsec = 1.83740 * 1.1 * 0.23271,    d3pds = ['mc12_8TeV.167783.Sherpa_CT10_WmunuMassiveCBPt280_500_CJetFilterBVeto.merge.NTUP_TAU.e1714_s1581_s1586_r3658_r3549_p1344/'])
mc.WmunuSherpaPt500_CJFBV      = Sample2(events = -1, xsec = 0.10193 * 1.1 * 0.24221,    d3pds = ['mc12_8TeV.167792.Sherpa_CT10_WmunuMassiveCBPt500_CJetFilterBVeto.merge.NTUP_TAU.e1714_s1581_s1586_r3658_r3549_p1344/'])
mc.WmunuSherpaPt0_BF           = Sample2(events = -1, xsec = 11000 * 1.1 * 0.012,        d3pds = ['mc12_8TeV.167743.Sherpa_CT10_WmunuMassiveCBPt0_BFilter.merge.NTUP_TAU.e1585_a159_a171_r3549_p1344/'])
mc.WmunuSherpaPt70_140_BF      = Sample2(events = -1, xsec = 250.59700 * 1.1 * 0.045942, d3pds = ['mc12_8TeV.167764.Sherpa_CT10_WmunuMassiveCBPt70_140_BFilter.merge.NTUP_TAU.e1714_a159_a171_r3549_p1344/'])
mc.WmunuSherpaPt140_280_BF     = Sample2(events = -1, xsec = 31.16320 * 1.1 * 0.063078,  d3pds = ['mc12_8TeV.167773.Sherpa_CT10_WmunuMassiveCBPt140_280_BFilter.merge.NTUP_TAU.e1741_a159_a171_r3549_p1344/'])
mc.WmunuSherpaPt280_500_BF     = Sample2(events = -1, xsec = 1.83740 * 1.1 * 0.083026,   d3pds = ['mc12_8TeV.167782.Sherpa_CT10_WmunuMassiveCBPt280_500_BFilter.merge.NTUP_TAU.e1714_s1581_s1586_r3658_r3549_p1344/'])
mc.WmunuSherpaPt500_BF         = Sample2(events = -1, xsec = 0.10193 * 1.1 * 0.099663,   d3pds = ['mc12_8TeV.167791.Sherpa_CT10_WmunuMassiveCBPt500_BFilter.merge.NTUP_TAU.e1714_s1581_s1586_r3658_r3549_p1344/'])
mc.WmunuSherpas = [mc.WmunuSherpaPt0_CJVBV, mc.WmunuSherpaPt70_140_CJVBV, mc.WmunuSherpaPt140_280_CJVBV, mc.WmunuSherpaPt280_500_CJVBV, mc.WmunuSherpaPt500_CJVBV,
                   mc.WmunuSherpaPt0_CJFBV, mc.WmunuSherpaPt70_140_CJFBV, mc.WmunuSherpaPt140_280_CJFBV, mc.WmunuSherpaPt280_500_CJFBV, mc.WmunuSherpaPt500_CJFBV,
                   mc.WmunuSherpaPt0_BF,    mc.WmunuSherpaPt70_140_BF,    mc.WmunuSherpaPt140_280_BF,    mc.WmunuSherpaPt280_500_BF,    mc.WmunuSherpaPt500_BF,
                   ]

mc.WtaunuSherpaPt0_CJVBV        = Sample2(events = -1, xsec = 11000 * 1.1 * 0.94,         d3pds = ['mc12_8TeV.167748.Sherpa_CT10_WtaunuMassiveCBPt0_CJetVetoBVeto.merge.NTUP_TAU.e1585_a159_a171_r3549_p1344/'])
mc.WtaunuSherpaPt70_140_CJVBV   = Sample2(events = -1, xsec = 250.59700 * 1.1 * 0.75485,  d3pds = ['mc12_8TeV.167769.Sherpa_CT10_WtaunuMassiveCBPt70_140_CJetVetoBVeto.merge.NTUP_TAU.e1714_s1581_s1586_r3658_r3549_p1344/'])
mc.WtaunuSherpaPt140_280_CJVBV  = Sample2(events = -1, xsec = 31.16320 * 1.1 * 0.71609,   d3pds = ['mc12_8TeV.167778.Sherpa_CT10_WtaunuMassiveCBPt140_280_CJetVetoBVeto.merge.NTUP_TAU.e1714_s1581_s1586_r3658_r3549_p1344/'])
mc.WtaunuSherpaPt280_500_CJVBV  = Sample2(events = -1, xsec = 1.83740 * 1.1 * 0.68397,    d3pds = ['mc12_8TeV.167787.Sherpa_CT10_WtaunuMassiveCBPt280_500_CJetVetoBVeto.merge.NTUP_TAU.e1714_s1581_s1586_r3658_r3549_p1344/'])
mc.WtaunuSherpaPt500_CJVBV      = Sample2(events = -1, xsec = 0.10193 * 1.1 * 0.66004,    d3pds = ['mc12_8TeV.167796.Sherpa_CT10_WtaunuMassiveCBPt500_CJetVetoBVeto.merge.NTUP_TAU.e1714_s1581_s1586_r3658_r3549_p1344/'])
mc.WtaunuSherpaPt0_CJFBV        = Sample2(events = -1, xsec = 11000 * 1.1 * 0.048,        d3pds = ['mc12_8TeV.167747.Sherpa_CT10_WtaunuMassiveCBPt0_CJetFilterBVeto.merge.NTUP_TAU.e1585_a159_a171_r3549_p1344/'])
mc.WtaunuSherpaPt70_140_CJFBV   = Sample2(events = -1, xsec = 250.59700 * 1.1 * 0.19889,  d3pds = ['mc12_8TeV.167768.Sherpa_CT10_WtaunuMassiveCBPt70_140_CJetFilterBVeto.merge.NTUP_TAU.e1714_s1581_s1586_r3658_r3549_p1344/'])
mc.WtaunuSherpaPt140_280_CJFBV  = Sample2(events = -1, xsec = 31.16320 * 1.1 * 0.22015,   d3pds = ['mc12_8TeV.167777.Sherpa_CT10_WtaunuMassiveCBPt140_280_CJetFilterBVeto.merge.NTUP_TAU.e1714_s1581_s1586_r3658_r3549_p1344/'])
mc.WtaunuSherpaPt280_500_CJFBV  = Sample2(events = -1, xsec = 1.83740 * 1.1 * 0.23271,    d3pds = ['mc12_8TeV.167786.Sherpa_CT10_WtaunuMassiveCBPt280_500_CJetFilterBVeto.merge.NTUP_TAU.e1714_s1581_s1586_r3658_r3549_p1344/'])
mc.WtaunuSherpaPt500_CJFBV      = Sample2(events = -1, xsec = 0.10193 * 1.1 * 0.24221,    d3pds = ['mc12_8TeV.167795.Sherpa_CT10_WtaunuMassiveCBPt500_CJetFilterBVeto.merge.NTUP_TAU.e1714_s1581_s1586_r3658_r3549_p1344/'])
mc.WtaunuSherpaPt0_BF           = Sample2(events = -1, xsec = 11000 * 1.1 *0.012,         d3pds = ['mc12_8TeV.167746.Sherpa_CT10_WtaunuMassiveCBPt0_BFilter.merge.NTUP_TAU.e1585_a159_a171_r3549_p1344/'])
mc.WtaunuSherpaPt70_140_BF      = Sample2(events = -1, xsec = 250.59700 * 1.1 * 0.045942, d3pds = ['mc12_8TeV.167767.Sherpa_CT10_WtaunuMassiveCBPt70_140_BFilter.merge.NTUP_TAU.e1714_s1581_s1586_r3658_r3549_p1344/'])
mc.WtaunuSherpaPt140_280_BF     = Sample2(events = -1, xsec = 31.16320 * 1.1 * 0.063078,  d3pds = ['mc12_8TeV.167776.Sherpa_CT10_WtaunuMassiveCBPt140_280_BFilter.merge.NTUP_TAU.e1741_s1581_s1586_r3658_r3549_p1344/'])
mc.WtaunuSherpaPt280_500_BF     = Sample2(events = -1, xsec = 1.83740 * 1.1 * 0.083026,   d3pds = ['mc12_8TeV.167785.Sherpa_CT10_WtaunuMassiveCBPt280_500_BFilter.merge.NTUP_TAU.e1714_s1581_s1586_r3658_r3549_p1344/'])
mc.WtaunuSherpaPt500_BF         = Sample2(events = -1, xsec = 0.10193 * 1.1 * 0.099663,   d3pds = ['mc12_8TeV.167794.Sherpa_CT10_WtaunuMassiveCBPt500_BFilter.merge.NTUP_TAU.e1714_s1581_s1586_r3658_r3549_p1344/'])
mc.WtaunuSherpas = [mc.WtaunuSherpaPt0_CJVBV, mc.WtaunuSherpaPt70_140_CJVBV, mc.WtaunuSherpaPt140_280_CJVBV, mc.WtaunuSherpaPt280_500_CJVBV, mc.WtaunuSherpaPt500_CJVBV,
                    mc.WtaunuSherpaPt0_CJFBV, mc.WtaunuSherpaPt70_140_CJFBV, mc.WtaunuSherpaPt140_280_CJFBV, mc.WtaunuSherpaPt280_500_CJFBV, mc.WtaunuSherpaPt500_CJFBV,
                    mc.WtaunuSherpaPt0_BF,    mc.WtaunuSherpaPt70_140_BF,    mc.WtaunuSherpaPt140_280_BF,    mc.WtaunuSherpaPt280_500_BF,    mc.WtaunuSherpaPt500_BF,
                    ]

# -----------------------------------------------------------------------------
# Z/DYee
# -----------------------------------------------------------------------------

mc.ZeeAHNp0 = Sample2(events = 498999, xsec = 711.7700*1.23*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107650.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp0.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.ZeeAHNp1 = Sample2(events = 200000, xsec = 155.1700*1.23*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107651.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp1.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.ZeeAHNp2 = Sample2(events =  99500, xsec =  48.7450*1.23*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107652.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp2.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.ZeeAHNp3 = Sample2(events =  50000, xsec =  14.2250*1.23*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107653.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp3.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.ZeeAHNp4 = Sample2(events =  20000, xsec =   3.7595*1.23*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107654.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp4.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.ZeeAHNp5 = Sample2(events =  10000, xsec =   1.0945*1.23*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107655.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp5.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.ZeeAHNpXs = [mc.ZeeAHNp0, mc.ZeeAHNp1, mc.ZeeAHNp2, mc.ZeeAHNp3, mc.ZeeAHNp4, mc.ZeeAHNp5]

mc.ZeeAHM60Np0 = Sample2(events = 999998, xsec = 3477.20000*1.19*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.146830.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZeeNp0Excl_Mll10to60.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZeeAHM60Np1 = Sample2(events = 299999, xsec =  108.80000*1.19*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.146831.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZeeNp1Excl_Mll10to60.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZeeAHM60Np2 = Sample2(events = 469999, xsec =   52.76700*1.19*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.146832.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZeeNp2Excl_Mll10to60.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZeeAHM60Np3 = Sample2(events = 144500, xsec =   11.29700*1.19*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.146833.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZeeNp3Excl_Mll10to60.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZeeAHM60Np4 = Sample2(events =  36300, xsec =    2.58360*1.19*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.146834.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZeeNp4Excl_Mll10to60.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZeeAHM60Np5 = Sample2(events =  79619, xsec =    0.69267*1.19*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.146835.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZeeNp5Incl_Mll10to60.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZeeAHM60NpXs = [mc.ZeeAHM60Np0, mc.ZeeAHM60Np1, mc.ZeeAHM60Np2, mc.ZeeAHM60Np3, mc.ZeeAHM60Np4, mc.ZeeAHM60Np5]

mc.ZeeAHVBFNp0 = Sample2(events = 6419080, xsec = 712.0800*1.23*0.033522, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.167320.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_ZeeNp0.merge.NTUP_TAU.e1422_s1499_s1504_r3658_r3549_p1344/'])
mc.ZeeAHVBFNp1 = Sample2(events = 3394288, xsec = 154.9900*1.23*0.080913, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.167321.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_ZeeNp1.merge.NTUP_TAU.e1422_s1499_s1504_r3658_r3549_p1344/'])
mc.ZeeAHVBFNp2 = Sample2(events = 3134987, xsec =  48.8330*1.23*0.2463,   site = "MWT2_DATADISK",     d3pds = ['mc12_8TeV.167322.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_ZeeNp2.merge.NTUP_TAU.e1422_s1499_s1504_r3658_r3549_p1344/'])
mc.ZeeAHVBFNp3 = Sample2(events = 1685796, xsec =  14.1830*1.23*0.4692,   site = "MWT2_DATADISK",     d3pds = ['mc12_8TeV.167323.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_ZeeNp3.merge.NTUP_TAU.e1422_s1499_s1504_r3658_r3549_p1344/'])
mc.ZeeAHVBFNp4 = Sample2(events =  653597, xsec =   3.7909*1.23*0.67933,  site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.167324.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_ZeeNp4.merge.NTUP_TAU.e1422_s1499_s1504_r3658_r3549_p1344/'])
mc.ZeeAHVBFNp5 = Sample2(events =  295000, xsec =   1.1331*1.23*1,        site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.147078.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZeeNp5.merge.NTUP_TAU.e1422_s1499_s1504_r3658_r3549_p1344/'])
mc.ZeeAHVBFNpXs = [mc.ZeeAHVBFNp0, mc.ZeeAHVBFNp1, mc.ZeeAHVBFNp2, mc.ZeeAHVBFNp3, mc.ZeeAHVBFNp4, mc.ZeeAHVBFNp5]

mc.ZeeAHTVBFNp2 = Sample2(events = 4375786, xsec = 48.8330*1.23*0.074897, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.169502.AlpgenJimmy_Auto_AUET2CTEQ6L1_TVBF_ZeeNp2.merge.NTUP_TAU.e1733_s1581_s1586_r3658_r3549_p1344/'])
mc.ZeeAHTVBFNp3 = Sample2(events = 2712894, xsec = 14.1830*1.23*0.16132,  site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.169503.AlpgenJimmy_Auto_AUET2CTEQ6L1_TVBF_ZeeNp3.merge.NTUP_TAU.e1733_s1581_s1586_r3658_r3549_p1344/'])
mc.ZeeAHTVBFNp4 = Sample2(events = 1264697, xsec =  3.7909*1.23*0.27884,  site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.169504.AlpgenJimmy_Auto_AUET2CTEQ6L1_TVBF_ZeeNp4.merge.NTUP_TAU.e1733_s1581_s1586_r3658_r3549_p1344/'])
mc.ZeeAHTVBFNp5 = Sample2(events =  564658, xsec =  1.1331*1.23*0.43324,  site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.169505.AlpgenJimmy_Auto_AUET2CTEQ6L1_TVBF_ZeeNp5.merge.NTUP_TAU.e1733_s1581_s1586_r3658_r3549_p1344/'])
#mc.ZeeAHTVBFNpXs = [mc.ZeeAHTVBFNp2, mc.ZeeAHTVBFNp3, mc.ZeeAHTVBFNp4, mc.ZeeAHTVBFNp5]
mc.ZeeAHTVBFNpXs = [mc.ZeeAHTVBFNp3, mc.ZeeAHTVBFNp4]

mc.ZeeAPNp0 = Sample2(events = 6298988, xsec = 718.9700*1.18*1.0, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147105.AlpgenPythia_Auto_P2011C_ZeeNp0.merge.NTUP_TAU.e1879_s1581_s1586_r3658_r3549_p1344/'])
mc.ZeeAPNp1 = Sample2(events = 8199476, xsec = 175.7000*1.18*1.0, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147106.AlpgenPythia_Auto_P2011C_ZeeNp1.merge.NTUP_TAU.e1879_s1581_s1586_r3658_r3549_p1344/'])
mc.ZeeAPNp2 = Sample2(events = 3175991, xsec =  58.8750*1.18*1.0, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147107.AlpgenPythia_Auto_P2011C_ZeeNp2.merge.NTUP_TAU.e1879_s1581_s1586_r3658_r3549_p1344/'])
mc.ZeeAPNp3 = Sample2(events =  894995, xsec =  15.6360*1.18*1.0, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147108.AlpgenPythia_Auto_P2011C_ZeeNp3.merge.NTUP_TAU.e1879_s1581_s1586_r3658_r3549_p1344/'])
mc.ZeeAPNp4 = Sample2(events =  398597, xsec =   4.0116*1.18*1.0, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147109.AlpgenPythia_Auto_P2011C_ZeeNp4.merge.NTUP_TAU.e1879_s1581_s1586_r3658_r3549_p1344/'])
mc.ZeeAPNp5 = Sample2(events =  229700, xsec =   1.2592*1.18*1.0, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147110.AlpgenPythia_Auto_P2011C_ZeeNp5incl.merge.NTUP_TAU.e1879_s1581_s1586_r3658_r3549_p1344/'])
mc.ZeeAPNpXs = [mc.ZeeAPNp0, mc.ZeeAPNp1, mc.ZeeAPNp2, mc.ZeeAPNp3, mc.ZeeAPNp4, mc.ZeeAPNp5]

mc.ZeeEW = Sample2(label = "Z^{EW}->ee", events = 499996, xsec = 0.35899, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.129921.Sherpa_CT10_Ztoee2JetsEW1JetQCD15GeVM40_min_n_tchannels.merge.NTUP_TAU.e1557_s1499_s1504_r3658_r3549_p1344/'])

mc.ZeePP = Sample2(label = "Z->ee (PP)", events = 9994580, xsec = 1109.9, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.147806.PowhegPythia8_AU2CT10_Zee.merge.NTUP_TAU.e1169_s1469_s1470_r3542_r3549_p1344/'])

mc.DYee120M180   = Sample2(events = -1, xsec = -1.0, d3pds = ['mc12_8TeV.129504.PowhegPythia8_AU2CT10_DYee_120M180.merge.NTUP_TAU.e1248_s1469_s1470_r3752_r3549_p1344/'])
mc.DYee180M250   = Sample2(events = -1, xsec = -1.0, d3pds = ['mc12_8TeV.129505.PowhegPythia8_AU2CT10_DYee_180M250.merge.NTUP_TAU.e1248_s1469_s1470_r3542_r3549_p1344/'])
mc.DYee250M400   = Sample2(events = -1, xsec = -1.0, d3pds = ['mc12_8TeV.129506.PowhegPythia8_AU2CT10_DYee_250M400.merge.NTUP_TAU.e1248_s1469_s1470_r3542_r3549_p1344/'])
mc.DYee400M600   = Sample2(events = -1, xsec = -1.0, d3pds = ['mc12_8TeV.129507.PowhegPythia8_AU2CT10_DYee_400M600.merge.NTUP_TAU.e1248_s1469_s1470_r3542_r3549_p1344/'])
mc.DYee600M800   = Sample2(events = -1, xsec = -1.0, d3pds = ['mc12_8TeV.129508.PowhegPythia8_AU2CT10_DYee_600M800.merge.NTUP_TAU.e1248_s1469_s1470_r3542_r3549_p1344/'])
mc.DYee800M1000  = Sample2(events = -1, xsec = -1.0, d3pds = ['mc12_8TeV.129509.PowhegPythia8_AU2CT10_DYee_800M1000.merge.NTUP_TAU.e1248_s1469_s1470_r3542_r3549_p1344/'])
mc.DYee1000M1250 = Sample2(events = -1, xsec = -1.0, d3pds = ['mc12_8TeV.129510.PowhegPythia8_AU2CT10_DYee_1000M1250.merge.NTUP_TAU.e1248_s1469_s1470_r3542_r3549_p1344/'])
mc.DYee1250M1500 = Sample2(events = -1, xsec = -1.0, d3pds = ['mc12_8TeV.129511.PowhegPythia8_AU2CT10_DYee_1250M1500.merge.NTUP_TAU.e1248_s1469_s1470_r3542_r3549_p1344/'])
mc.DYee1500M1750 = Sample2(events = -1, xsec = -1.0, d3pds = ['mc12_8TeV.129512.PowhegPythia8_AU2CT10_DYee_1500M1750.merge.NTUP_TAU.e1248_s1469_s1470_r3752_r3549_p1344/'])
mc.DYee1750M2000 = Sample2(events = -1, xsec = -1.0, d3pds = ['mc12_8TeV.129513.PowhegPythia8_AU2CT10_DYee_1750M2000.merge.NTUP_TAU.e1248_s1469_s1470_r3542_r3549_p1344/'])
mc.DYee2000M2250 = Sample2(events = -1, xsec = -1.0, d3pds = ['mc12_8TeV.129514.PowhegPythia8_AU2CT10_DYee_2000M2250.merge.NTUP_TAU.e1248_s1469_s1470_r3542_r3549_p1344/'])
mc.DYee2250M2500 = Sample2(events = -1, xsec = -1.0, d3pds = ['mc12_8TeV.129515.PowhegPythia8_AU2CT10_DYee_2250M2500.merge.NTUP_TAU.e1248_s1469_s1470_r3542_r3549_p1344/'])
mc.DYee2500M2750 = Sample2(events = -1, xsec = -1.0, d3pds = ['mc12_8TeV.129516.PowhegPythia8_AU2CT10_DYee_2500M2750.merge.NTUP_TAU.e1248_s1469_s1470_r3752_r3549_p1344/'])
mc.DYee2750M3000 = Sample2(events = -1, xsec = -1.0, d3pds = ['mc12_8TeV.129517.PowhegPythia8_AU2CT10_DYee_2750M3000.merge.NTUP_TAU.e1248_s1469_s1470_r3752_r3549_p1344/'])
mc.DYee3000M     = Sample2(events = -1, xsec = -1.0, d3pds = ['mc12_8TeV.129518.PowhegPythia8_AU2CT10_DYee_3000M.merge.NTUP_TAU.e1248_s1469_s1470_r3752_r3549_p1344/'])
mc.ZDYees = [mc.ZeePP,
             mc.DYee120M180,
             mc.DYee180M250,
             mc.DYee250M400,
             mc.DYee400M600,
             mc.DYee600M800,
             mc.DYee800M1000,
             mc.DYee1000M1250,
             mc.DYee1250M1500,
             mc.DYee1500M1750,
             mc.DYee1750M2000,
             mc.DYee2000M2250,
             mc.DYee2250M2500,
             mc.DYee2500M2750,
             mc.DYee2750M3000,
             mc.DYee3000M
             ]

# -----------------------------------------------------------------------------
# mc.Z/DYmumu
# -----------------------------------------------------------------------------

mc.ZmumuAHNp0 = Sample2(events = 499900, xsec = 712.1100*1.23*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107660.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp0.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.ZmumuAHNp1 = Sample2(events = 200000, xsec = 154.7700*1.23*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107661.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp1.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.ZmumuAHNp2 = Sample2(events = 100000, xsec =  48.9120*1.23*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107662.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp2.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.ZmumuAHNp3 = Sample2(events =  50000, xsec =  14.2260*1.23*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107663.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp3.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.ZmumuAHNp4 = Sample2(events =  20000, xsec =   3.7838*1.23*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107664.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp4.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.ZmumuAHNp5 = Sample2(events =  10000, xsec =   1.1148*1.23*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107665.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp5.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.ZmumuAHNpXs = [mc.ZmumuAHNp0, mc.ZmumuAHNp1, mc.ZmumuAHNp2, mc.ZmumuAHNp3, mc.ZmumuAHNp4, mc.ZmumuAHNp5]

mc.ZmumuAHM60Np0 = Sample2(events = 999999, xsec = 3477.10000*1.19*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.146840.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZmumuNp0Excl_Mll10to60.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZmumuAHM60Np1 = Sample2(events = 299998, xsec =  108.75000*1.19*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.146841.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZmumuNp1Excl_Mll10to60.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZmumuAHM60Np2 = Sample2(events = 469998, xsec =   52.74100*1.19*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.146842.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZmumuNp2Excl_Mll10to60.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZmumuAHM60Np3 = Sample2(events = 144499, xsec =   11.24100*1.19*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.146843.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZmumuNp3Excl_Mll10to60.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZmumuAHM60Np4 = Sample2(events =  36300, xsec =    2.60050*1.19*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.146844.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZmumuNp4Excl_Mll10to60.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZmumuAHM60Np5 = Sample2(events =  79740, xsec =    0.69373*1.19*1.0, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.146845.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZmumuNp5Incl_Mll10to60.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZmumuAHM60NpXs = [mc.ZmumuAHM60Np0, mc.ZmumuAHM60Np1, mc.ZmumuAHM60Np2, mc.ZmumuAHM60Np3, mc.ZmumuAHM60Np4, mc.ZmumuAHM60Np5]

mc.ZmumuAHVBFNp0 = Sample2(events = 1256195, xsec = 712.1100*1.23*0.0065069, site = "AGLT2_PHYS-HIGGS",  d3pds = ['mc12_8TeV.167330.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_ZmumuNp0.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZmumuAHVBFNp1 = Sample2(events = 1589693, xsec = 155.0000*1.23*0.038308,  site = "AGLT2_PHYS-HIGGS",  d3pds = ['mc12_8TeV.167331.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_ZmumuNp1.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZmumuAHVBFNp2 = Sample2(events = 1738993, xsec =  48.9450*1.23*0.14105,   site = "AGLT2_PHYS-HIGGS",  d3pds = ['mc12_8TeV.167332.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_ZmumuNp2.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZmumuAHVBFNp3 = Sample2(events = 1349997, xsec =  14.1870*1.23*0.35368,   site = "AGLT2_PHYS-HIGGS",  d3pds = ['mc12_8TeV.167333.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_ZmumuNp3.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZmumuAHVBFNp4 = Sample2(events =  534998, xsec =   3.7943*1.23*0.5921,    site = "AGLT2_PHYS-HIGGS",  d3pds = ['mc12_8TeV.167334.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_ZmumuNp4.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZmumuAHVBFNp5 = Sample2(events =  304099, xsec =   1.1342*1.23*1.0000,    site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.147086.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZmumuNp5.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZmumuAHVBFNpXs = [mc.ZmumuAHVBFNp0, mc.ZmumuAHVBFNp1, mc.ZmumuAHVBFNp2, mc.ZmumuAHVBFNp3, mc.ZmumuAHVBFNp4, mc.ZmumuAHVBFNp5]

mc.ZmumuAHTVBFNp2 = Sample2(events = 1615096, xsec = 48.9450*1.23*0.035006, site = "TRIUMF-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.169512.AlpgenJimmy_Auto_AUET2CTEQ6L1_TVBF_ZmumuNp2.merge.NTUP_TAU.e1733_s1581_s1586_r3658_r3549_p1344/'])
mc.ZmumuAHTVBFNp3 = Sample2(events = 1486296, xsec = 14.1870*1.23*0.089845, site = "FZK-LCG2_PERF-TAU",    d3pds = ['mc12_8TeV.169513.AlpgenJimmy_Auto_AUET2CTEQ6L1_TVBF_ZmumuNp3.merge.NTUP_TAU.e1733_s1581_s1586_r3658_r3549_p1344/'])
mc.ZmumuAHTVBFNp4 = Sample2(events =  756200, xsec =  3.7943*1.23*0.18890,  site = "TRIUMF-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.169514.AlpgenJimmy_Auto_AUET2CTEQ6L1_TVBF_ZmumuNp4.merge.NTUP_TAU.e1733_s1581_s1586_r3658_r3549_p1344/'])
mc.ZmumuAHTVBFNp5 = Sample2(events =  465537, xsec =  1.1342*1.23*0.34240,  site = "FZK-LCG2_PERF-TAU",    d3pds = ['mc12_8TeV.169515.AlpgenJimmy_Auto_AUET2CTEQ6L1_TVBF_ZmumuNp5.merge.NTUP_TAU.e1733_s1581_s1586_r3658_r3549_p1344/'])
mc.ZmumuAHTVBFNpXs = [mc.ZmumuAHTVBFNp2, mc.ZmumuAHTVBFNp3, mc.ZmumuAHTVBFNp4, mc.ZmumuAHTVBFNp5]

mc.ZmumuAPNp0 = Sample2(events = 6298796, xsec = 719.1600*1.18*1.0, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147113.AlpgenPythia_Auto_P2011C_ZmumuNp0.merge.NTUP_TAU.e1880_s1581_s1586_r3658_r3549_p1344/'])
mc.ZmumuAPNp1 = Sample2(events = 8198384, xsec = 175.7400*1.18*1.0, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147114.AlpgenPythia_Auto_P2011C_ZmumuNp1.merge.NTUP_TAU.e1880_s1581_s1586_r3658_r3549_p1344/'])
mc.ZmumuAPNp2 = Sample2(events = 3175488, xsec =  58.8820*1.18*1.0, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147115.AlpgenPythia_Auto_P2011C_ZmumuNp2.merge.NTUP_TAU.e1880_s1581_s1586_r3658_r3549_p1344/'])
mc.ZmumuAPNp3 = Sample2(events =  894799, xsec =  15.6730*1.18*1.0, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147116.AlpgenPythia_Auto_P2011C_ZmumuNp3.merge.NTUP_TAU.e1880_s1581_s1586_r3658_r3549_p1344/'])
mc.ZmumuAPNp4 = Sample2(events =  398200, xsec =   4.0057*1.18*1.0, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147117.AlpgenPythia_Auto_P2011C_ZmumuNp4.merge.NTUP_TAU.e1880_s1581_s1586_r3658_r3549_p1344/'])
mc.ZmumuAPNp5 = Sample2(events =  229200, xsec =   1.2544*1.18*1.0, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147118.AlpgenPythia_Auto_P2011C_ZmumuNp5incl.merge.NTUP_TAU.e1880_s1581_s1586_r3658_r3549_p1344/'])
mc.ZmumuAPNpXs = [mc.ZmumuAPNp0, mc.ZmumuAPNp1, mc.ZmumuAPNp2, mc.ZmumuAPNp3, mc.ZmumuAPNp4, mc.ZmumuAPNp5]

mc.ZmumuEW = Sample2(label = "Z^{EW}->#mu#mu", events = 499898, xsec = 0.35843, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.129922.Sherpa_CT10_Ztomm2JetsEW1JetQCD15GeVM40_min_n_tchannels.merge.NTUP_TAU.e1557_s1499_s1504_r3658_r3549_p1344/'])

mc.ZmumuPP = Sample2(label = "Z->#mu#mu (PP)", events = 9988282, xsec = 1109.9, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.147807.PowhegPythia8_AU2CT10_Zmumu.merge.NTUP_TAU.e1169_s1469_s1470_r3542_r3549_p1344/'])

mc.DYmumu120M180   = Sample2(events = -1, xsec = 9.8450,     d3pds = ['mc12_8TeV.129524.PowhegPythia8_AU2CT10_DYmumu_120M180.merge.NTUP_TAU.e1248_s1469_s1470_r3542_r3549_p1344/'])
mc.DYmumu180M250   = Sample2(events = -1, xsec = 1.5710,     d3pds = ['mc12_8TeV.129525.PowhegPythia8_AU2CT10_DYmumu_180M250.merge.NTUP_TAU.e1248_s1469_s1470_r3752_r3549_p1344/'])
mc.DYmumu250M400   = Sample2(events = -1, xsec = 5.4920E-01, d3pds = ['mc12_8TeV.129526.PowhegPythia8_AU2CT10_DYmumu_250M400.merge.NTUP_TAU.e1248_s1469_s1470_r3542_r3549_p1344/'])
mc.DYmumu400M600   = Sample2(events = -1, xsec = 8.9660E-02, d3pds = ['mc12_8TeV.129527.PowhegPythia8_AU2CT10_DYmumu_400M600.merge.NTUP_TAU.e1248_s1469_s1470_r3752_r3549_p1344/'])
mc.DYmumu600M800   = Sample2(events = -1, xsec = 1.5100E-02, d3pds = ['mc12_8TeV.129528.PowhegPythia8_AU2CT10_DYmumu_600M800.merge.NTUP_TAU.e1248_s1469_s1470_r3542_r3549_p1344/'])
mc.DYmumu800M1000  = Sample2(events = -1, xsec = 3.7500E-03, d3pds = ['mc12_8TeV.129529.PowhegPythia8_AU2CT10_DYmumu_800M1000.merge.NTUP_TAU.e1248_s1469_s1470_r3542_r3549_p1344/'])
mc.DYmumu1000M1250 = Sample2(events = -1, xsec = 1.2930E-03, d3pds = ['mc12_8TeV.129530.PowhegPythia8_AU2CT10_DYmumu_1000M1250.merge.NTUP_TAU.e1248_s1469_s1470_r3752_r3549_p1344/'])
mc.DYmumu1250M1500 = Sample2(events = -1, xsec = 3.5770E-04, d3pds = ['mc12_8TeV.129531.PowhegPythia8_AU2CT10_DYmumu_1250M1500.merge.NTUP_TAU.e1248_s1469_s1470_r3542_r3549_p1344/'])
mc.DYmumu1500M1750 = Sample2(events = -1, xsec = 1.1230E-04, d3pds = ['mc12_8TeV.129532.PowhegPythia8_AU2CT10_DYmumu_1500M1750.merge.NTUP_TAU.e1248_s1469_s1470_r3542_r3549_p1344/'])
mc.DYmumu1750M2000 = Sample2(events = -1, xsec = 3.8380E-05, d3pds = ['mc12_8TeV.129533.PowhegPythia8_AU2CT10_DYmumu_1750M2000.merge.NTUP_TAU.e1248_s1469_s1470_r3542_r3549_p1344/'])
mc.DYmumu2000M2250 = Sample2(events = -1, xsec = 1.3890E-05, d3pds = ['mc12_8TeV.129534.PowhegPythia8_AU2CT10_DYmumu_2000M2250.merge.NTUP_TAU.e1248_s1469_s1470_r3542_r3549_p1344/'])
mc.DYmumu2250M2500 = Sample2(events = -1, xsec = 5.2260E-06, d3pds = ['mc12_8TeV.129535.PowhegPythia8_AU2CT10_DYmumu_2250M2500.merge.NTUP_TAU.e1248_s1469_s1470_r3542_r3549_p1344/'])
mc.DYmumu2500M2750 = Sample2(events = -1, xsec = 2.0170E-06, d3pds = ['mc12_8TeV.129536.PowhegPythia8_AU2CT10_DYmumu_2500M2750.merge.NTUP_TAU.e1248_s1469_s1470_r3542_r3549_p1344/'])
mc.DYmumu2750M3000 = Sample2(events = -1, xsec = 7.8910E-07, d3pds = ['mc12_8TeV.129537.PowhegPythia8_AU2CT10_DYmumu_2750M3000.merge.NTUP_TAU.e1248_s1469_s1470_r3542_r3549_p1344/'])
mc.DYmumu3000M     = Sample2(events = -1, xsec = 5.0390E-07, d3pds = ['mc12_8TeV.129538.PowhegPythia8_AU2CT10_DYmumu_3000M.merge.NTUP_TAU.e1248_s1469_s1470_r3542_r3549_p1344/'])
mc.ZDYmumus = [mc.ZmumuPP,
               mc.DYmumu120M180,
               mc.DYmumu180M250,
               mc.DYmumu250M400,
               mc.DYmumu400M600,
               mc.DYmumu600M800,
               mc.DYmumu800M1000,
               mc.DYmumu1000M1250,
               mc.DYmumu1250M1500,
               mc.DYmumu1500M1750,
               mc.DYmumu1750M2000,
               mc.DYmumu2000M2250,
               mc.DYmumu2250M2500,
               mc.DYmumu2500M2750,
               mc.DYmumu2750M3000,
               mc.DYmumu3000M
               ]

# -----------------------------------------------------------------------------
# Z/DYtautau
# -----------------------------------------------------------------------------

mc.ZtautauAHNp0 = Sample2(events = -1, xsec = 711.8100*1.23*1.0, site = "FZK-LCG2_PERF-TAU",    d3pds = ['mc12_8TeV.107670.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp0.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.ZtautauAHNp1 = Sample2(events = -1, xsec = 155.1300*1.23*1.0, site = "FZK-LCG2_PERF-TAU",    d3pds = ['mc12_8TeV.107671.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp1.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.ZtautauAHNp2 = Sample2(events = -1, xsec =  48.8040*1.23*1.0, site = "FZK-LCG2_PERF-TAU",    d3pds = ['mc12_8TeV.107672.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp2.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.ZtautauAHNp3 = Sample2(events = -1, xsec =  14.1600*1.23*1.0, site = "FZK-LCG2_PERF-TAU",    d3pds = ['mc12_8TeV.107673.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp3.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.ZtautauAHNp4 = Sample2(events = -1, xsec =   3.7744*1.23*1.0, site = "FZK-LCG2_PERF-TAU",    d3pds = ['mc12_8TeV.107674.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp4.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.ZtautauAHNp5 = Sample2(events = -1, xsec =   1.1163*1.23*1.0, site = "TRIUMF-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107675.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp5.merge.NTUP_TAU.e1571_s1499_s1504_r3658_r3549_p1344/'])
mc.ZtautauAHNpXs = [mc.ZtautauAHNp0, mc.ZtautauAHNp1, mc.ZtautauAHNp2, mc.ZtautauAHNp3, mc.ZtautauAHNp4, mc.ZtautauAHNp5]

mc.ZtautauAHM60Np0 = Sample2(events = -1, xsec = 3477.1000*1.19*1.0, site = "", d3pds = ['mc12_8TeV.146850.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZtautauNp0Excl_Mll10to60.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZtautauAHM60Np1 = Sample2(events = -1, xsec =  108.7400*1.19*1.0, site = "", d3pds = ['mc12_8TeV.146851.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZtautauNp1Excl_Mll10to60.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZtautauAHM60Np2 = Sample2(events = -1, xsec =   52.7320*1.19*1.0, site = "", d3pds = ['mc12_8TeV.146852.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZtautauNp2Excl_Mll10to60.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZtautauAHM60Np3 = Sample2(events = -1, xsec =   11.3260*1.19*1.0, site = "", d3pds = ['mc12_8TeV.146853.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZtautauNp3Excl_Mll10to60.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZtautauAHM60Np4 = Sample2(events = -1, xsec =    2.5920*1.19*1.0, site = "", d3pds = ['mc12_8TeV.146854.AlpgenJimmy_Auto_AUET3CTEQ6L1_ZtautauNp4Excl_Mll10to60.merge.NTUP_TAU.e1551_s1499_s1504_r3658_r3549_p1344/'])
mc.ZtautauAHM60Np5 = Sample2(events = -1, xsec =    0.6929*1.19*1.0, site = "", d3pds = ['mc12_8TeV.146855.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZtautauNp5Incl_Mll10to60.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZtautauAHM60NpXs = [mc.ZtautauAHM60Np0, mc.ZtautauAHM60Np1, mc.ZtautauAHM60Np2, mc.ZtautauAHM60Np3, mc.ZtautauAHM60Np4, mc.ZtautauAHM60Np5]

mc.ZtautauAHVBFNp0 = Sample2(events = -1, xsec = 712.1000*1.23*0.008043, site = "AGLT2_PHYS-HIGGS",  d3pds = ['mc12_8TeV.167340.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_ATau_ZtautauNp0.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZtautauAHVBFNp1 = Sample2(events = -1, xsec = 154.9900*1.23*0.02242,  site = "AGLT2_PHYS-HIGGS",  d3pds = ['mc12_8TeV.167341.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_ATau_ZtautauNp1.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZtautauAHVBFNp2 = Sample2(events = -1, xsec =  48.8500*1.23*0.083617, site = "AGLT2_PHYS-HIGGS",  d3pds = ['mc12_8TeV.167342.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_ATau_ZtautauNp2.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZtautauAHVBFNp3 = Sample2(events = -1, xsec =  14.1850*1.23*0.19376,  site = "AGLT2_PHYS-HIGGS",  d3pds = ['mc12_8TeV.167343.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_ATau_ZtautauNp3.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZtautauAHVBFNp4 = Sample2(events = -1, xsec =   3.7934*1.23*0.30956,  site = "AGLT2_PHYS-HIGGS",  d3pds = ['mc12_8TeV.167344.AlpgenJimmy_Auto_AUET2CTEQ6L1_VBF_ATau_ZtautauNp4.merge.NTUP_TAU.e1600_s1499_s1504_r3658_r3549_p1344/'])
mc.ZtautauAHVBFNp5 = Sample2(events = -1, xsec =   1.1366*1.23*1,        site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.147094.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZtautauNp5.merge.NTUP_TAU.e1551_s1499_s1504_r3658_r3549_p1344/'])
mc.ZtautauAHVBFNpXs = [mc.ZtautauAHVBFNp0, mc.ZtautauAHVBFNp1, mc.ZtautauAHVBFNp2, mc.ZtautauAHVBFNp3, mc.ZtautauAHVBFNp4, mc.ZtautauAHVBFNp5]

mc.ZtautauAHTVBFNp2 = Sample2(events = -1, xsec = 48.8500*1.23*0.019898, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.169522.AlpgenJimmy_Auto_AUET2CTEQ6L1_TVBF_ATau_ZtautauNp2.merge.NTUP_TAU.e1733_s1581_s1586_r3658_r3549_p1344/'])
mc.ZtautauAHTVBFNp3 = Sample2(events = -1, xsec = 14.1850*1.23*0.051770, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.169523.AlpgenJimmy_Auto_AUET2CTEQ6L1_TVBF_ATau_ZtautauNp3.merge.NTUP_TAU.e1733_s1581_s1586_r3658_r3549_p1344/'])
mc.ZtautauAHTVBFNp4 = Sample2(events = -1, xsec =  3.7934*1.23*0.10523,  site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.169524.AlpgenJimmy_Auto_AUET2CTEQ6L1_TVBF_ATau_ZtautauNp4.merge.NTUP_TAU.e1733_s1581_s1586_r3658_r3549_p1344/'])
mc.ZtautauAHTVBFNp5 = Sample2(events = -1, xsec =  1.1366*1.23*0.18852,  site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.169525.AlpgenJimmy_Auto_AUET2CTEQ6L1_TVBF_ATau_ZtautauNp5.merge.NTUP_TAU.e1733_s1581_s1586_r3658_r3549_p1344/'])
mc.ZtautauAHTVBFNpXs = [mc.ZtautauAHTVBFNp2, mc.ZtautauAHTVBFNp3, mc.ZtautauAHTVBFNp4, mc.ZtautauAHTVBFNp5]

mc.ZtautauAPNp0 = Sample2(events = -1, xsec = 719.1800*1.18*1.0, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147121.AlpgenPythia_Auto_P2011C_ZtautauNp0.merge.NTUP_TAU.e1881_s1581_s1586_r3658_r3549_p1344/'])
mc.ZtautauAPNp1 = Sample2(events = -1, xsec = 175.7200*1.18*1.0, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147122.AlpgenPythia_Auto_P2011C_ZtautauNp1.merge.NTUP_TAU.e1881_s1581_s1586_r3658_r3549_p1344/'])
mc.ZtautauAPNp2 = Sample2(events = -1, xsec =  58.8620*1.18*1.0, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147123.AlpgenPythia_Auto_P2011C_ZtautauNp2.merge.NTUP_TAU.e1881_s1581_s1586_r3658_r3549_p1344/'])
mc.ZtautauAPNp3 = Sample2(events = -1, xsec =  15.6640*1.18*1.0, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147124.AlpgenPythia_Auto_P2011C_ZtautauNp3.merge.NTUP_TAU.e1881_s1581_s1586_r3658_r3549_p1344/'])
mc.ZtautauAPNp4 = Sample2(events = -1, xsec =   4.0121*1.18*1.0, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147125.AlpgenPythia_Auto_P2011C_ZtautauNp4.merge.NTUP_TAU.e1881_s1581_s1586_r3658_r3549_p1344/'])
mc.ZtautauAPNp5 = Sample2(events = -1, xsec =   1.2560*1.18*1.0, site = "AGLT2_PHYS-HIGGS", d3pds = ['mc12_8TeV.147126.AlpgenPythia_Auto_P2011C_ZtautauNp5incl.merge.NTUP_TAU.e1881_s1581_s1586_r3658_r3549_p1344/'])
mc.ZtautauAPNpXs = [mc.ZtautauAPNp0, mc.ZtautauAPNp1, mc.ZtautauAPNp2, mc.ZtautauAPNp3, mc.ZtautauAPNp4, mc.ZtautauAPNp5]

mc.ZtautauEW = Sample2(label = "Z^{EW}->#tau#tau", events = -1, xsec = 0.46085, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.167723.Sherpa_CT10_Ztott2JetsEW_Mll40_NoYtau.merge.NTUP_TAU.e1982_s1581_s1586_r3658_r3549_p1344/'])

mc.ZtautauPythia = Sample2(label = "Z->#tau#tau (Pyth)", events = -1, xsec = 878.04, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.147818.Pythia8_AU2CTEQ6L1_Ztautau.merge.NTUP_TAU.e1176_s1479_s1470_r3553_r3549_p1344/'])

mc.ZtautauPowhegPythia = Sample2(label = "Z->#tau#tau (PP)", events = -1, xsec = 1109.9, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.147808.PowhegPythia8_AU2CT10_Ztautau.merge.NTUP_TAU.e1169_s1469_s1470_r3542_r3549_p1344/'])

mc.DYtautau180M250   = Sample2(events = -1, xsec = 1.2485E-00, d3pds = ['mc12_8TeV.158731.Pythia8_AU2CTEQ6L1_DYtautau_180M250.merge.NTUP_TAU.e1518_s1499_s1504_r3658_r3549_p1344/'])
mc.DYtautau250M400   = Sample2(events = -1, xsec = 4.3608E-01, d3pds = ['mc12_8TeV.158732.Pythia8_AU2CTEQ6L1_DYtautau_250M400.merge.NTUP_TAU.e1518_s1499_s1504_r3658_r3549_p1344/'])
mc.DYtautau400M600   = Sample2(events = -1, xsec = 7.1800E-02, d3pds = ['mc12_8TeV.158733.Pythia8_AU2CTEQ6L1_DYtautau_400M600.merge.NTUP_TAU.e1518_s1499_s1504_r3658_r3549_p1344/'])
mc.DYtautau600M800   = Sample2(events = -1, xsec = 1.2235E-02, d3pds = ['mc12_8TeV.158734.Pythia8_AU2CTEQ6L1_DYtautau_600M800.merge.NTUP_TAU.e1518_s1499_s1504_r3658_r3549_p1344/'])
mc.DYtautau800M1000  = Sample2(events = -1, xsec = 3.0727E-03, d3pds = ['mc12_8TeV.158735.Pythia8_AU2CTEQ6L1_DYtautau_800M1000.merge.NTUP_TAU.e1518_s1499_s1504_r3658_r3549_p1344/'])
mc.DYtautau1000M1250 = Sample2(events = -1, xsec = 1.0719E-03, d3pds = ['mc12_8TeV.158736.Pythia8_AU2CTEQ6L1_DYtautau_1000M1250.merge.NTUP_TAU.e1518_s1499_s1504_r3658_r3549_p1344/'])
mc.DYtautau1250M1500 = Sample2(events = -1, xsec = 2.9974E-04, d3pds = ['mc12_8TeV.158737.Pythia8_AU2CTEQ6L1_DYtautau_1250M1500.merge.NTUP_TAU.e1518_s1499_s1504_r3658_r3549_p1344/'])
mc.DYtautau1500M1750 = Sample2(events = -1, xsec = 9.5176E-05, d3pds = ['mc12_8TeV.158738.Pythia8_AU2CTEQ6L1_DYtautau_1500M1750.merge.NTUP_TAU.e1518_s1499_s1504_r3658_r3549_p1344/'])
mc.DYtautau1750M2000 = Sample2(events = -1, xsec = 3.2609E-05, d3pds = ['mc12_8TeV.158739.Pythia8_AU2CTEQ6L1_DYtautau_1750M2000.merge.NTUP_TAU.e1518_s1499_s1504_r3658_r3549_p1344/'])
mc.DYtautau2000M2250 = Sample2(events = -1, xsec = 1.1855E-05, d3pds = ['mc12_8TeV.158740.Pythia8_AU2CTEQ6L1_DYtautau_2000M2250.merge.NTUP_TAU.e1518_s1499_s1504_r3658_r3549_p1344/'])
mc.DYtautau2250M2500 = Sample2(events = -1, xsec = 4.4565E-06, d3pds = ['mc12_8TeV.158741.Pythia8_AU2CTEQ6L1_DYtautau_2250M2500.merge.NTUP_TAU.e1518_s1499_s1504_r3658_r3549_p1344/'])
## </MISSING FROM p1344 PRODUCTION?>
#DYtautau2500M2750 = Sample2(events = -1, xsec = -1.0, d3pds = [])
#DYtautau2750M3000 = Sample2(events = -1, xsec = -1.0, d3pds = [])
#DYtautau3000M     = Sample2(events = -1, xsec = -1.0, d3pds = [])
mc.ZDYtautaus = [mc.ZtautauPythia,
                 mc.DYtautau180M250,
                 mc.DYtautau250M400,
                 mc.DYtautau400M600,
                 mc.DYtautau600M800,
                 mc.DYtautau800M1000,
                 mc.DYtautau1000M1250,
                 mc.DYtautau1250M1500,
                 mc.DYtautau1500M1750,
                 mc.DYtautau1750M2000,
                 ]

# -----------------------------------------------------------------------------
# top
# -----------------------------------------------------------------------------

mc.ttbarMC = Sample2(events = 14997103, xsec = 137.320, site = "TRIUMF-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.105200.McAtNloJimmy_CT10_ttbar_LeptonFilter.merge.NTUP_TAU.e1513_s1499_s1504_r3658_r3549_p1344/'])
mc.ttbarPP = Sample2(events = 14996424, xsec = 137.320, site = "AGLT2_PHYS-HIGGS",     d3pds = ['mc12_8TeV.117050.PowhegPythia_P2011C_ttbar.merge.NTUP_TAU.e1728_s1581_s1586_r3658_r3549_p1443/']) # oops p1443

mc.ttbarAPlnlnNp0 = Sample2(events = 3199485, xsec =  4.28690*1.9655, site = "RAL-LCG2_DATADISK",             d3pds = ["mc12_8TeV.201020.AlpgenAutoPythia_P2012_ttbar_lnlnNp0.merge.NTUP_TAU.e2356_s1581_s1586_r3925_r4540_p1344/"])
mc.ttbarAPlnlnNp1 = Sample2(events = 3187981, xsec =  4.38440*1.9655, site = "IN2P3-LPSC_DATADISK",           d3pds = ["mc12_8TeV.201021.AlpgenAutoPythia_P2012_ttbar_lnlnNp1.merge.NTUP_TAU.e2356_s1581_s1586_r3925_r4540_p1344/"])
mc.ttbarAPlnlnNp2 = Sample2(events = 2091691, xsec =  2.79850*1.9655, site = "BNL-OSG2_DATADISK",             d3pds = ["mc12_8TeV.201022.AlpgenAutoPythia_P2012_ttbar_lnlnNp2.merge.NTUP_TAU.e2356_s1581_s1586_r3925_r4540_p1344/"])
mc.ttbarAPlnlnNp3 = Sample2(events =  971691, xsec =  1.29390*1.9655, site = "BNL-OSG2_DATADISK",             d3pds = ["mc12_8TeV.201023.AlpgenAutoPythia_P2012_ttbar_lnlnNp3.merge.NTUP_TAU.e2356_s1581_s1586_r3925_r4540_p1344/"])
mc.ttbarAPlnlnNp4 = Sample2(events =  589998, xsec =  0.74637*1.9655, site = "UKI-SOUTHGRID-OX-HEP_DATADISK", d3pds = ["mc12_8TeV.201024.AlpgenAutoPythia_P2012_ttbar_lnlnNp4inc.merge.NTUP_TAU.e2356_s1581_s1586_r3925_r4540_p1344/"])

mc.ttbarAPjjlnNp0 = Sample2(events = 6293873, xsec = 17.1510*2.0491,  site = "BNL-OSG2_DATADISK",             d3pds = ["mc12_8TeV.201220.AlpgenAutoPythia_P2012_ttbar_jjlnNp0.merge.NTUP_TAU.e2356_s1581_s1586_r3925_r4540_p1344/"])
mc.ttbarAPjjlnNp1 = Sample2(events = 6389459, xsec = 17.5320*2.0491,  site = "MWT2_DATADISK",                 d3pds = ["mc12_8TeV.201221.AlpgenAutoPythia_P2012_ttbar_jjlnNp1.merge.NTUP_TAU.e2356_s1581_s1586_r3925_r4540_p1344/"])
mc.ttbarAPjjlnNp2 = Sample2(events = 4179757, xsec = 11.2090*2.0491,  site = "IN2P3-CPPM_DATADISK",           d3pds = ["mc12_8TeV.201222.AlpgenAutoPythia_P2012_ttbar_jjlnNp2.merge.NTUP_TAU.e2356_s1581_s1586_r3925_r4540_p1344/"])
mc.ttbarAPjjlnNp3 = Sample2(events = 1949886, xsec =  5.1767*2.0491,  site = "BNL-OSG2_DATADISK",             d3pds = ["mc12_8TeV.201223.AlpgenAutoPythia_P2012_ttbar_jjlnNp3.merge.NTUP_TAU.e2356_s1581_s1586_r3925_r4540_p1344/"])
mc.ttbarAPjjlnNp4 = Sample2(events = 1179291, xsec =  2.9869*2.0491,  site = "BNL-OSG2_DATADISK",             d3pds = ["mc12_8TeV.201224.AlpgenAutoPythia_P2012_ttbar_jjlnNp4inc.merge.NTUP_TAU.e2356_s1581_s1586_r3925_r4540_p1344/"])

mc.ttbarAPjjjjNp0 = Sample2(events = 2494881, xsec = 17.1640*2.1385,  site = "AGLT2_DATADISK",                d3pds = ["mc12_8TeV.201420.AlpgenAutoPythia_P2012_ttbar_jjjjNp0.merge.NTUP_TAU.e2356_s1581_s1586_r3925_r4540_p1344/"])
mc.ttbarAPjjjjNp1 = Sample2(events = 3894575, xsec = 17.5210*2.1385,  site = "IN2P3-LAPP_DATADISK",           d3pds = ["mc12_8TeV.201421.AlpgenAutoPythia_P2012_ttbar_jjjjNp1.merge.NTUP_TAU.e2356_s1581_s1586_r3925_r4540_p1344/"])
mc.ttbarAPjjjjNp2 = Sample2(events = 2491478, xsec = 11.2040*2.1385,  site = "",                              d3pds = ["mc12_8TeV.201422.AlpgenAutoPythia_P2012_ttbar_jjjjNp2.merge.NTUP_TAU.e2356_s1581_s1586_r3925_r4540_p1344/"])
mc.ttbarAPjjjjNp3 = Sample2(events = 1173988, xsec =  5.1704*2.1385,  site = "BNL-OSG2_DATADISK",             d3pds = ["mc12_8TeV.201423.AlpgenAutoPythia_P2012_ttbar_jjjjNp3.merge.NTUP_TAU.e2356_s1581_s1586_r3925_r4540_p1344/"])
mc.ttbarAPjjjjNp4 = Sample2(events =      -1, xsec =  2.9829*2.1385,  site = "",                              d3pds = ["mc12_8TeV.201424.AlpgenAutoPythia_P2012_ttbar_jjjjNp4inc.merge.NTUP_TAU.e2356_s1581_s1586_r3925_r4540_p1344/"])

mc.ttbarAPlnlnNpXs = [mc.ttbarAPlnlnNp0, mc.ttbarAPlnlnNp1, mc.ttbarAPlnlnNp2, mc.ttbarAPlnlnNp3, mc.ttbarAPlnlnNp4]
mc.ttbarAPjjlnNpXs = [mc.ttbarAPjjlnNp0, mc.ttbarAPjjlnNp1, mc.ttbarAPjjlnNp2, mc.ttbarAPjjlnNp3, mc.ttbarAPjjlnNp4]
mc.ttbarAPjjjjNpXs = [mc.ttbarAPjjjjNp0, mc.ttbarAPjjjjNp1, mc.ttbarAPjjjjNp2, mc.ttbarAPjjjjNp3, mc.ttbarAPjjjjNp4]

mc.topSe   = Sample2(events =  199997, xsec = 0.606,   site = "IN2P3-CPPM_DATADISK",  d3pds = ['mc12_8TeV.108343.McAtNloJimmy_AUET2CT10_SingleTopSChanWenu.merge.NTUP_TAU.e1525_s1499_s1504_r3658_r3549_p1344/'])
mc.topSmu  = Sample2(events =  200000, xsec = 0.606,   site = "FZK-LCG2_PERF-TAU",    d3pds = ['mc12_8TeV.108344.McAtNloJimmy_AUET2CT10_SingleTopSChanWmunu.merge.NTUP_TAU.e1525_s1499_s1504_r3658_r3549_p1344/'])
mc.topStau = Sample2(events =  199999, xsec = 0.606,   site = "FZK-LCG2_PERF-TAU",    d3pds = ['mc12_8TeV.108345.McAtNloJimmy_AUET2CT10_SingleTopSChanWtaunu.merge.NTUP_TAU.e1525_s1499_s1504_r3658_r3549_p1344/'])
mc.topW    = Sample2(events = 1999194, xsec = 22.37,   site = "TRIUMF-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.108346.McAtNloJimmy_AUET2CT10_SingleTopWtChanIncl.merge.NTUP_TAU.e1525_s1499_s1504_r3658_r3549_p1344/'])
mc.topTe   = Sample2(events =  299899, xsec = 9.48,    site = "TRIUMF-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.117360.AcerMCPythia_AUET2BCTEQ6L1_singletop_tchan_e.merge.NTUP_TAU.e1346_s1499_s1504_r3658_r3549_p1344/'])
mc.topTmu  = Sample2(events =  300000, xsec = 9.48,    site = "FZK-LCG2_PERF-TAU",    d3pds = ['mc12_8TeV.117361.AcerMCPythia_AUET2BCTEQ6L1_singletop_tchan_mu.merge.NTUP_TAU.e1346_s1499_s1504_r3658_r3549_p1344/'])
mc.topTtau = Sample2(events =  293499, xsec = 9.48,    site = "IN2P3-CPPM_DATADISK",  d3pds = ['mc12_8TeV.117362.AcerMCPythia_AUET2BCTEQ6L1_singletop_tchan_tau.merge.NTUP_TAU.e1346_s1499_s1504_r3658_r3549_p1344/'])

mc.singletops = [mc.topW,
                 mc.topSe, mc.topSmu, mc.topStau,
                 mc.topTe, mc.topTmu, mc.topTtau,
                 ]

# -----------------------------------------------------------------------------
# diboson
# -----------------------------------------------------------------------------

mc.WWlnulnuNp0 = Sample2(events = 255000, xsec = 2.49700*1.21, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107100.AlpgenJimmy_AUET2CTEQ6L1_WWlnulnuNp0.merge.NTUP_TAU.e1596_s1499_s1504_r3658_r3549_p1344/'])
mc.WWlnulnuNp1 = Sample2(events = 125000, xsec = 1.24910*1.21, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107101.AlpgenJimmy_AUET2CTEQ6L1_WWlnulnuNp1.merge.NTUP_TAU.e1596_s1499_s1504_r3658_r3549_p1344/'])
mc.WWlnulnuNp2 = Sample2(events =  60000, xsec = 0.59200*1.21, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107102.AlpgenJimmy_AUET2CTEQ6L1_WWlnulnuNp2.merge.NTUP_TAU.e1596_s1499_s1504_r3658_r3549_p1344/'])
mc.WWlnulnuNp3 = Sample2(events =  35000, xsec = 0.32847*1.21, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.107103.AlpgenJimmy_AUET2CTEQ6L1_WWlnulnuNp3.merge.NTUP_TAU.e1596_s1499_s1504_r3658_r3549_p1344/'])
mc.WWlnulnuNpXs = [mc.WWlnulnuNp0, mc.WWlnulnuNp1, mc.WWlnulnuNp2, mc.WWlnulnuNp3]

mc.WWqqlnuNp0 = Sample2(events = 994999, xsec = 9.9819*1.26, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.110829.AlpgenJimmy_AUET2CTEQ6L1_WWqqlnuNp0.merge.NTUP_TAU.e1596_s1499_s1504_r3658_r3549_p1344/'])
mc.WWqqlnuNp1 = Sample2(events = 494899, xsec = 5.0144*1.26, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.110830.AlpgenJimmy_AUET2CTEQ6L1_WWqqlnuNp1.merge.NTUP_TAU.e1596_s1499_s1504_r3658_r3549_p1344/'])
mc.WWqqlnuNp2 = Sample2(events = 234998, xsec = 2.3658*1.26, site = "SWT2_CPB_DATADISK", d3pds = ['mc12_8TeV.110831.AlpgenJimmy_AUET2CTEQ6L1_WWqqlnuNp2.merge.NTUP_TAU.e1596_s1499_s1504_r3658_r3549_p1344/'])
mc.WWqqlnuNp3 = Sample2(events = 130000, xsec = 1.3139*1.26, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.110832.AlpgenJimmy_AUET2CTEQ6L1_WWqqlnuNp3.merge.NTUP_TAU.e1596_s1499_s1504_r3658_r3549_p1344/'])
mc.WWqqlnuNpXs = [mc.WWqqlnuNp0, mc.WWqqlnuNp1, mc.WWqqlnuNp2, mc.WWqqlnuNp3]

mc.WWenuenu     = Sample2(events = 30000, xsec = 0.018, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.106011.gg2WW0240Jimmy_AUET2CT10_WpWmenuenu.merge.NTUP_TAU.e1249_s1469_s1470_r3542_r3549_p1344/'])
mc.WWenumunu    = Sample2(events = 30000, xsec = 0.018, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.106012.gg2WW0240Jimmy_AUET2CT10_WpWmenumunu.merge.NTUP_TAU.e1249_s1469_s1470_r3542_r3549_p1344/'])
mc.WWenutaunu   = Sample2(events = 30000, xsec = 0.018, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.106013.gg2WW0240Jimmy_AUET2CT10_WpWmenutaunu.merge.NTUP_TAU.e1249_s1469_s1470_r3542_r3549_p1344/'])
mc.WWmunumunu   = Sample2(events = 30000, xsec = 0.018, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.106014.gg2WW0240Jimmy_AUET2CT10_WpWmmunumunu.merge.NTUP_TAU.e1253_s1469_s1470_r3542_r3549_p1344/'])
mc.WWmunuenu    = Sample2(events = 30000, xsec = 0.018, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.106015.gg2WW0240Jimmy_AUET2CT10_WpWmmunuenu.merge.NTUP_TAU.e1253_s1469_s1470_r3542_r3549_p1344/'])
mc.WWmunutaunu  = Sample2(events = 29900, xsec = 0.018, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.106016.gg2WW0240Jimmy_AUET2CT10_WpWmmunutaunu.merge.NTUP_TAU.e1249_s1469_s1470_r3542_r3549_p1344/'])
mc.WWtaunutaunu = Sample2(events = 30000, xsec = 0.018, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.106017.gg2WW0240Jimmy_AUET2CT10_WpWmtaunutaunu.merge.NTUP_TAU.e1253_s1469_s1470_r3542_r3549_p1344/'])
mc.WWtaunuenu   = Sample2(events = 30000, xsec = 0.018, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.106018.gg2WW0240Jimmy_AUET2CT10_WpWmtaunuenu.merge.NTUP_TAU.e1253_s1469_s1470_r3542_r3549_p1344/'])
mc.WWtaunumunu  = Sample2(events = 30000, xsec = 0.018, site = "SWT2_CPB_DATADISK", d3pds = ['mc12_8TeV.106019.gg2WW0240Jimmy_AUET2CT10_WpWmtaunumunu.merge.NTUP_TAU.e1253_s1469_s1470_r3542_r3549_p1344/'])
mc.gg2WWs = [mc.WWenuenu,     mc.WWenumunu,  mc.WWenutaunu,
             mc.WWmunumunu,   mc.WWmunuenu,  mc.WWmunutaunu,
             mc.WWtaunutaunu, mc.WWtaunuenu, mc.WWtaunumunu,
             ]

mc.ZZ = Sample2(events = 245000, xsec =  7.32*1.0*0.21165, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.105986.Herwig_AUET2CTEQ6L1_ZZ.merge.NTUP_TAU.e1576_s1499_s1504_r3658_r3549_p1344/'])
mc.WZ = Sample2(events = 999998, xsec = 22.30*1.0*0.30546, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.105987.Herwig_AUET2CTEQ6L1_WZ.merge.NTUP_TAU.e1576_s1499_s1504_r3658_r3549_p1344/'])
mc.HerwigVVs = [mc.WZ, mc.ZZ]

mc.dibosons = mc.HerwigVVs + mc.WWlnulnuNpXs + mc.WWqqlnuNpXs + mc.gg2WWs

# -----------------------------------------------------------------------------
# Higgs 125
# -----------------------------------------------------------------------------

mc.ggFH125tautau = Sample2(events = 1994795, xsec = 1.2297600*0.456192, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.161566.PowHegPythia8_AU2CT10_ggH125_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.VBFH125tautau = Sample2(events = 1999895, xsec = 0.0982107*0.456192, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.161606.PowHegPythia8_AU2CT10_VBFH125_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.WH125tautau   = Sample2(events =   30000, xsec = 0.0438858*0.456192, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.161646.Pythia8_AU2CTEQ6L1_WH125_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.ZH125tautau   = Sample2(events =   30000, xsec = 0.0248409*0.456192, site = "FZK-LCG2_PERF-TAU", d3pds = ['mc12_8TeV.161686.Pythia8_AU2CTEQ6L1_ZH125_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.H125s = [mc.ggFH125tautau, mc.VBFH125tautau]

# -----------------------------------------------------------------------------
# Higgs other
# -----------------------------------------------------------------------------

mc.ggFH100tautau = Sample2(xsec = 2.49996*0.456192, d3pds = ['mc12_8TeV.161561.PowHegPythia8_AU2CT10_ggH100_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3752_r3549_p1344/'])
mc.ggFH105tautau = Sample2(xsec = 2.24598*0.456192, d3pds = ['mc12_8TeV.161562.PowHegPythia8_AU2CT10_ggH105_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3752_r3549_p1344/'])
mc.ggFH110tautau = Sample2(xsec = 2.00320*0.456192, d3pds = ['mc12_8TeV.161563.PowHegPythia8_AU2CT10_ggH110_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.ggFH115tautau = Sample2(xsec = 1.74496*0.456192, d3pds = ['mc12_8TeV.161564.PowHegPythia8_AU2CT10_ggH115_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.ggFH120tautau = Sample2(xsec = 1.50023*0.456192, d3pds = ['mc12_8TeV.161565.PowHegPythia8_AU2CT10_ggH120_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3753_r3549_p1344/'])
mc.ggFH130tautau = Sample2(xsec = 0.97578*0.456192, d3pds = ['mc12_8TeV.161567.PowHegPythia8_AU2CT10_ggH130_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.ggFH135tautau = Sample2(xsec = 0.75555*0.456192, d3pds = ['mc12_8TeV.161568.PowHegPythia8_AU2CT10_ggH135_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.ggFH140tautau = Sample2(xsec = 0.54705*0.456192, d3pds = ['mc12_8TeV.161569.PowHegPythia8_AU2CT10_ggH140_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.ggFH145tautau = Sample2(xsec = 0.37934*0.456192, d3pds = ['mc12_8TeV.161570.PowHegPythia8_AU2CT10_ggH145_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.ggFH150tautau = Sample2(xsec = 0.23205*0.456192, d3pds = ['mc12_8TeV.161571.PowHegPythia8_AU2CT10_ggH150_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.ggFHtautaus = [mc.ggFH100tautau, mc.ggFH105tautau, mc.ggFH110tautau, mc.ggFH115tautau, mc.ggFH120tautau, mc.ggFH125tautau, mc.ggFH130tautau, mc.ggFH135tautau, mc.ggFH140tautau, mc.ggFH145tautau, mc.ggFH150tautau]

mc.VBFH100tautau = Sample2(xsec = 0.163593*0.456192, d3pds = ['mc12_8TeV.161601.PowHegPythia8_AU2CT10_VBFH100_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.VBFH105tautau = Sample2(xsec = 0.153996*0.456192, d3pds = ['mc12_8TeV.161602.PowHegPythia8_AU2CT10_VBFH105_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3752_r3549_p1344/'])
mc.VBFH110tautau = Sample2(xsec = 0.143280*0.456192, d3pds = ['mc12_8TeV.161603.PowHegPythia8_AU2CT10_VBFH110_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.VBFH115tautau = Sample2(xsec = 0.129884*0.456192, d3pds = ['mc12_8TeV.161604.PowHegPythia8_AU2CT10_VBFH115_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.VBFH120tautau = Sample2(xsec = 0.115872*0.456192, d3pds = ['mc12_8TeV.161605.PowHegPythia8_AU2CT10_VBFH120_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.VBFH130tautau = Sample2(xsec = 0.080460*0.456192, d3pds = ['mc12_8TeV.161607.PowHegPythia8_AU2CT10_VBFH130_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.VBFH135tautau = Sample2(xsec = 0.064125*0.456192, d3pds = ['mc12_8TeV.161608.PowHegPythia8_AU2CT10_VBFH135_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3752_r3549_p1344/'])
mc.VBFH140tautau = Sample2(xsec = 0.047775*0.456192, d3pds = ['mc12_8TeV.161609.PowHegPythia8_AU2CT10_VBFH140_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.VBFH145tautau = Sample2(xsec = 0.033956*0.456192, d3pds = ['mc12_8TeV.161610.PowHegPythia8_AU2CT10_VBFH145_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.VBFH150tautau = Sample2(xsec = 0.021267*0.456192, d3pds = ['mc12_8TeV.161611.PowHegPythia8_AU2CT10_VBFH150_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.VBFHtautaus = [mc.VBFH100tautau, mc.VBFH105tautau, mc.VBFH110tautau, mc.VBFH115tautau, mc.VBFH120tautau, mc.VBFH125tautau, mc.VBFH130tautau, mc.VBFH135tautau, mc.VBFH140tautau, mc.VBFH145tautau, mc.VBFH150tautau]

mc.WH100tautau = Sample2(xsec = 0.118856*0.456192,  d3pds = ['mc12_8TeV.161641.Pythia8_AU2CTEQ6L1_WH100_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.WH105tautau = Sample2(xsec = 0.100778*0.456192,  d3pds = ['mc12_8TeV.161642.Pythia8_AU2CTEQ6L1_WH105_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3752_r3549_p1344/'])
mc.WH110tautau = Sample2(xsec = 0.084800*0.456192,  d3pds = ['mc12_8TeV.161643.Pythia8_AU2CTEQ6L1_WH110_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3752_r3549_p1344/'])
mc.WH115tautau = Sample2(xsec = 0.0696540*0.456192, d3pds = ['mc12_8TeV.161644.Pythia8_AU2CTEQ6L1_WH115_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.WH120tautau = Sample2(xsec = 0.0565586*0.456192, d3pds = ['mc12_8TeV.161645.Pythia8_AU2CTEQ6L1_WH120_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.WH130tautau = Sample2(xsec = 0.0329130*0.456192, d3pds = ['mc12_8TeV.161647.Pythia8_AU2CTEQ6L1_WH130_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.WH135tautau = Sample2(xsec = 0.0240795*0.456192, d3pds = ['mc12_8TeV.161648.Pythia8_AU2CTEQ6L1_WH135_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.WH140tautau = Sample2(xsec = 0.0164955*0.456192, d3pds = ['mc12_8TeV.161649.Pythia8_AU2CTEQ6L1_WH140_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.WH145tautau = Sample2(xsec = 0.0108264*0.456192, d3pds = ['mc12_8TeV.161650.Pythia8_AU2CTEQ6L1_WH145_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.WH150tautau = Sample2(xsec = 0.0062577*0.456192, d3pds = ['mc12_8TeV.161651.Pythia8_AU2CTEQ6L1_WH150_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.WHtautaus = [mc.WH100tautau, mc.WH105tautau, mc.WH110tautau, mc.WH115tautau, mc.WH120tautau, mc.WH125tautau, mc.WH130tautau, mc.WH135tautau, mc.WH140tautau, mc.WH145tautau, mc.WH150tautau]

mc.ZH100tautau = Sample2(xsec = 0.0647981*0.456192, d3pds = ['mc12_8TeV.161681.Pythia8_AU2CTEQ6L1_ZH100_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.ZH105tautau = Sample2(xsec = 0.0553500*0.456192, d3pds = ['mc12_8TeV.161682.Pythia8_AU2CTEQ6L1_ZH105_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.ZH110tautau = Sample2(xsec = 0.0469520*0.456192, d3pds = ['mc12_8TeV.161683.Pythia8_AU2CTEQ6L1_ZH110_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.ZH115tautau = Sample2(xsec = 0.0388892*0.456192, d3pds = ['mc12_8TeV.161684.Pythia8_AU2CTEQ6L1_ZH115_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.ZH120tautau = Sample2(xsec = 0.0318293*0.456192, d3pds = ['mc12_8TeV.161685.Pythia8_AU2CTEQ6L1_ZH120_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3753_r3549_p1344/'])
mc.ZH130tautau = Sample2(xsec = 0.0187542*0.456192, d3pds = ['mc12_8TeV.161687.Pythia8_AU2CTEQ6L1_ZH130_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.ZH135tautau = Sample2(xsec = 0.0138330*0.456192, d3pds = ['mc12_8TeV.161688.Pythia8_AU2CTEQ6L1_ZH135_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.ZH140tautau = Sample2(xsec = 0.0095480*0.456192, d3pds = ['mc12_8TeV.161689.Pythia8_AU2CTEQ6L1_ZH140_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.ZH145tautau = Sample2(xsec = 0.0063024*0.456192, d3pds = ['mc12_8TeV.161690.Pythia8_AU2CTEQ6L1_ZH145_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.ZH150tautau = Sample2(xsec = 0.0036703*0.456192, d3pds = ['mc12_8TeV.161691.Pythia8_AU2CTEQ6L1_ZH150_tautaulh.merge.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344/'])
mc.ZHtautaus = [mc.ZH100tautau, mc.ZH105tautau, mc.ZH110tautau, mc.ZH115tautau, mc.ZH120tautau, mc.ZH125tautau, mc.ZH130tautau, mc.ZH135tautau, mc.ZH140tautau, mc.ZH145tautau, mc.ZH150tautau]

# -----------------------------------------------------------------------------
# Zprime tautau
# -----------------------------------------------------------------------------
mc.Zprime250  = Sample2(xsec = 37.39610, d3pds = ['mc12_8TeV.170201.Pythia8_AU2CTEQ6L1_Zprime250tautau.merge.NTUP_TAU.e1176_s1479_s1470_r3553_r3549_p1344/'])
mc.Zprime500  = Sample2(xsec =  2.82650, d3pds = ['mc12_8TeV.170202.Pythia8_AU2CTEQ6L1_Zprime500tautau.merge.NTUP_TAU.e1176_s1479_s1470_r3553_r3549_p1344/'])
mc.Zprime750  = Sample2(xsec =  0.53747, d3pds = ['mc12_8TeV.170203.Pythia8_AU2CTEQ6L1_Zprime750tautau.merge.NTUP_TAU.e1176_s1479_s1470_r3553_r3549_p1344/'])
mc.Zprime1000 = Sample2(xsec =  0.14845, d3pds = ['mc12_8TeV.170204.Pythia8_AU2CTEQ6L1_Zprime1000tautau.merge.NTUP_TAU.e1176_s1479_s1470_r3553_r3549_p1344/'])
mc.Zprime1250 = Sample2(xsec =  0.49671, d3pds = ['mc12_8TeV.170205.Pythia8_AU2CTEQ6L1_Zprime1250tautau.merge.NTUP_TAU.e1176_s1479_s1470_r3553_r3549_p1344/'])
mc.Zprimes = [mc.Zprime500, mc.Zprime750, mc.Zprime1000, mc.Zprime1250]

# -----------------------------------------------------------------------------
# Dummy samples
# -----------------------------------------------------------------------------
# backgrounds (nominal)
mc.diboson       = Sample2(label = "diboson",            d3pds = ["mc12_8TeV.diboson.merge"])
mc.gg2WW         = Sample2(label = "gg->WW",             d3pds = ["mc12_8TeV.gg2WW.merge"])
mc.HerwigVV      = Sample2(label = "WZ, ZZ",             d3pds = ["mc12_8TeV.HerwigVV.merge"])
mc.singletop     = Sample2(label = "single t",           d3pds = ["mc12_8TeV.singletop.merge"])
mc.tt            = Sample2(label = "t#bar{t}",           d3pds = ["mc12_8TeV.tt.merge"])
mc.ttMC          = Sample2(label = "t#bar{t} (MC)",      d3pds = ["mc12_8TeV.ttMC.merge"])
mc.ttPP          = Sample2(label = "t#bar{t} (PP)",      d3pds = ["mc12_8TeV.ttPP.merge"])
mc.ttAP          = Sample2(label = "t#bar{t} (AP)",      d3pds = ["mc12_8TeV.ttAP.merge"])
mc.ttAPlnln      = Sample2(label = "t#bar{t} lnln (AP)", d3pds = ["mc12_8TeV.ttAPlnln.merge"])
mc.ttAPjjln      = Sample2(label = "t#bar{t} jjln (AP)", d3pds = ["mc12_8TeV.ttAPjjln.merge"])
mc.ttAPjjjj      = Sample2(label = "t#bar{t} jjjj (AP)", d3pds = ["mc12_8TeV.ttAPjjjj.merge"])
mc.WenuAP        = Sample2(label = "W->e#nu",            d3pds = ["mc12_8TeV.WenuAP.merge"])
mc.WenuAHVBF     = Sample2(label = "W->e#nu VBF",        d3pds = ["mc12_8TeV.WenuAHVBF.merge"])
mc.WenuHybrid    = Sample2(label = "W^{hyb.}->e#nu",     d3pds = ["mc12_8TeV.WenuHybrid.merge"])
mc.WmunuAP       = Sample2(label = "W->#mu#nu",          d3pds = ["mc12_8TeV.WmunuAP.merge"])
mc.WmunuAHVBF    = Sample2(label = "W->#mu#nu VBF",      d3pds = ["mc12_8TeV.WmunuAHVBF.merge"])
mc.WmunuHybrid   = Sample2(label = "W^{hyb.}->#mu#nu",   d3pds = ["mc12_8TeV.WmunuHybrid.merge"])
mc.WtaunuAP      = Sample2(label = "W->#tau#nu",         d3pds = ["mc12_8TeV.WtaunuAP.merge"])
mc.WtaunuAHVBF   = Sample2(label = "W->#tau#nu VBF",     d3pds = ["mc12_8TeV.WtaunuAHVBF.merge"])
mc.WtaunuHybrid  = Sample2(label = "W^{hyb.}->#tau#nu",  d3pds = ["mc12_8TeV.WtaunuHybrid.merge"])
mc.WWlnulnu      = Sample2(label = "WWlnulnu",           d3pds = ["mc12_8TeV.WWlnulnu.merge"])
mc.WWqqlnu       = Sample2(label = "WWqqlnu",            d3pds = ["mc12_8TeV.WWqqlnu.merge"])
mc.ZeeAP         = Sample2(label = "Z->ee",              d3pds = ["mc12_8TeV.ZeeAP.merge"])
mc.ZeeAHVBF      = Sample2(label = "Z->ee VBF",          d3pds = ["mc12_8TeV.ZeeAHVBF.merge"])
mc.ZeeAHTVBF     = Sample2(label = "Z->ee TVBF",         d3pds = ["mc12_8TeV.ZeeAHTVBF.merge"])
mc.ZeeHybrid     = Sample2(label = "Z^{hyb.}->ee",       d3pds = ["mc12_8TeV.ZeeHybrid.merge"])
mc.ZeeAHM60      = Sample2(label = "Z->ee (M<60)",       d3pds = ["mc12_8TeV.ZeeAHM60.merge"])
mc.ZmumuAP       = Sample2(label = "Z->#mu#mu",          d3pds = ["mc12_8TeV.ZmumuAP.merge"])
mc.ZmumuAHVBF    = Sample2(label = "Z->#mu#mu VBF",      d3pds = ["mc12_8TeV.ZmumuAHVBF.merge"])
mc.ZmumuAHTVBF   = Sample2(label = "Z->#mu#mu TVBF",     d3pds = ["mc12_8TeV.ZmumuAHTVBF.merge"])
mc.ZmumuHybrid   = Sample2(label = "Z^{hyb.}->#mu#mu",   d3pds = ["mc12_8TeV.ZmumuHybrid.merge"])
mc.ZmumuAHM60    = Sample2(label = "Z->#mu#mu (M<60)",   d3pds = ["mc12_8TeV.ZmumuAHM60.merge"])
mc.ZtautauAP     = Sample2(label = "Z->#tau#tau",        d3pds = ["mc12_8TeV.ZtautauAP.merge"])
mc.ZtautauAHVBF  = Sample2(label = "Z->#tau#tau VBF",    d3pds = ["mc12_8TeV.ZtautauAHVBF.merge"])
mc.ZtautauAHTVBF = Sample2(label = "Z->#tau#tau TVBF",   d3pds = ["mc12_8TeV.ZtautauAHTVBF.merge"])
mc.ZtautauHybrid = Sample2(label = "Z^{hyb.}->#tau#tau", d3pds = ["mc12_8TeV.ZtautauHybrid.merge"])
mc.ZtautauAHM60  = Sample2(label = "Z->#tau#tau (M<60)", d3pds = ["mc12_8TeV.ZtautauAHM60.merge"])
mc.ggFH125       = Sample2(label = "ggFH^{125}",         d3pds = ["mc12_8TeV.161566.ggH125.merge"])
mc.VBFH125       = Sample2(label = "VBFH^{125}",         d3pds = ["mc12_8TeV.161606.VBFH125.merge"])
mc.WH125         = Sample2(label =   "WH^{125}",         d3pds = ["mc12_8TeV.161646.WH125.merge"])
mc.ZH125         = Sample2(label =   "ZH^{125}",         d3pds = ["mc12_8TeV.161686.ZH125.merge"])

# backgrounds (OS-SS)
mc.OSminusSS_diboson       = Sample2(label = "diboson",            d3pds = ["mc12_8TeV.diboson.OSminusSS"])
mc.OSminusSS_gg2WW         = Sample2(label = "gg->WW",             d3pds = ["mc12_8TeV.gg2WW.OSminusSS"])
mc.OSminusSS_HerwigVV      = Sample2(label = "WZ, ZZ",             d3pds = ["mc12_8TeV.HerwigVV.OSminusSS"])
mc.OSminusSS_singletop     = Sample2(label = "single t",           d3pds = ["mc12_8TeV.singletop.OSminusSS"])
mc.OSminusSS_tt            = Sample2(label = "t#bar{t}",           d3pds = ["mc12_8TeV.tt.OSminusSS"])
mc.OSminusSS_ttMC          = Sample2(label = "t#bar{t} (MC)",      d3pds = ["mc12_8TeV.ttMC.OSminusSS"])
mc.OSminusSS_ttPP          = Sample2(label = "t#bar{t} (PP)",      d3pds = ["mc12_8TeV.ttPP.OSminusSS"])
mc.OSminusSS_WenuAP        = Sample2(label = "W->e#nu",            d3pds = ["mc12_8TeV.WenuAP.OSminusSS"])
mc.OSminusSS_WenuAHVBF     = Sample2(label = "W->e#nu VBF",        d3pds = ["mc12_8TeV.WenuAHVBF.OSminusSS"])
mc.OSminusSS_WenuHybrid    = Sample2(label = "W^{hyb.}->e#nu",     d3pds = ["mc12_8TeV.WenuHybrid.OSminusSS"])
mc.OSminusSS_WmunuAP       = Sample2(label = "W->#mu#nu",          d3pds = ["mc12_8TeV.WmunuAP.OSminusSS"])
mc.OSminusSS_WmunuAHVBF    = Sample2(label = "W->#mu#nu VBF",      d3pds = ["mc12_8TeV.WmunuAHVBF.OSminusSS"])
mc.OSminusSS_WmunuHybrid   = Sample2(label = "W^{hyb.}->#mu#nu",   d3pds = ["mc12_8TeV.WmunuHybrid.OSminusSS"])
mc.OSminusSS_WtaunuAP      = Sample2(label = "W->#tau#nu",         d3pds = ["mc12_8TeV.WtaunuAP.OSminusSS"])
mc.OSminusSS_WtaunuAHVBF   = Sample2(label = "W->#tau#nu VBF",     d3pds = ["mc12_8TeV.WtaunuAHVBF.OSminusSS"])
mc.OSminusSS_WtaunuHybrid  = Sample2(label = "W^{hyb.}->#tau#nu",  d3pds = ["mc12_8TeV.WtaunuHybrid.OSminusSS"])
mc.OSminusSS_WWlnulnu      = Sample2(label = "WWlnulnu",           d3pds = ["mc12_8TeV.WWlnulnu.OSminusSS"])
mc.OSminusSS_WWqqlnu       = Sample2(label = "WWqqlnu",            d3pds = ["mc12_8TeV.WWqqlnu.OSminusSS"])
mc.OSminusSS_ZeeAP         = Sample2(label = "Z->ee",              d3pds = ["mc12_8TeV.ZeeAP.OSminusSS"])
mc.OSminusSS_ZeeAHVBF      = Sample2(label = "Z->ee VBF",          d3pds = ["mc12_8TeV.ZeeAHVBF.OSminusSS"])
mc.OSminusSS_ZeeAHTVBF     = Sample2(label = "Z->ee TVBF",         d3pds = ["mc12_8TeV.ZeeAHTVBF.OSminusSS"])
mc.OSminusSS_ZeeHybrid     = Sample2(label = "Z^{hyb.}->ee",       d3pds = ["mc12_8TeV.ZeeHybrid.OSminusSS"])
mc.OSminusSS_ZeeAHM60      = Sample2(label = "Z->ee (M<60)",       d3pds = ["mc12_8TeV.ZeeAHM60.OSminusSS"])
mc.OSminusSS_ZmumuAP       = Sample2(label = "Z->#mu#mu",          d3pds = ["mc12_8TeV.ZmumuAP.OSminusSS"])
mc.OSminusSS_ZmumuAHVBF    = Sample2(label = "Z->#mu#mu VBF",      d3pds = ["mc12_8TeV.ZmumuAHVBF.OSminusSS"])
mc.OSminusSS_ZmumuAHTVBF   = Sample2(label = "Z->#mu#mu TVBF",     d3pds = ["mc12_8TeV.ZmumuAHTVBF.OSminusSS"])
mc.OSminusSS_ZmumuHybrid   = Sample2(label = "Z^{hyb.}->#mu#mu",   d3pds = ["mc12_8TeV.ZmumuHybrid.OSminusSS"])
mc.OSminusSS_ZmumuAHM60    = Sample2(label = "Z->#mu#mu (M<60)",   d3pds = ["mc12_8TeV.ZmumuAHM60.OSminusSS"])
mc.OSminusSS_ZtautauAP     = Sample2(label = "Z->#tau#tau",        d3pds = ["mc12_8TeV.ZtautauAP.OSminusSS"])
mc.OSminusSS_ZtautauAHVBF  = Sample2(label = "Z->#tau#tau VBF",    d3pds = ["mc12_8TeV.ZtautauAHVBF.OSminusSS"])
mc.OSminusSS_ZtautauAHTVBF = Sample2(label = "Z->#tau#tau TVBF",   d3pds = ["mc12_8TeV.ZtautauAHTVBF.OSminusSS"])
mc.OSminusSS_ZtautauHybrid = Sample2(label = "Z^{hyb.}->#tau#tau", d3pds = ["mc12_8TeV.ZtautauHybrid.OSminusSS"])
mc.OSminusSS_ZtautauAHM60  = Sample2(label = "Z->#tau#tau (M<60)", d3pds = ["mc12_8TeV.ZtautauAHM60.OSminusSS"])
mc.OSminusSS_ggFH125       = Sample2(label = "ggFH^{125}",         d3pds = ["mc12_8TeV.161566.ggH125.OSminusSS"])
mc.OSminusSS_VBFH125       = Sample2(label = "VBFH^{125}",         d3pds = ["mc12_8TeV.161606.VBFH125.OSminusSS"])
mc.OSminusSS_WH125         = Sample2(label =   "WH^{125}",         d3pds = ["mc12_8TeV.161646.WH125.OSminusSS"])
mc.OSminusSS_ZH125         = Sample2(label =   "ZH^{125}",         d3pds = ["mc12_8TeV.161686.ZH125.OSminusSS"])

# signal
mc.H120       = Sample2(label = "H^{120}->#tau#tau", d3pds = ["mc12_8TeV.H120.merge"])
mc.H125       = Sample2(label = "H^{125}->#tau#tau", d3pds = ["mc12_8TeV.H125.merge"])
mc.H130       = Sample2(label = "H^{130}->#tau#tau", d3pds = ["mc12_8TeV.H130.merge"])

# misc
mc.ElFakes    = Sample2(label = "", d3pds = ["mc12_8TeV.ElFakes.merge"])
mc.MinBias    = Sample2(label = "", d3pds = ["mc12_8TeV.MinBias.merge"])
mc.other      = Sample2(label = "", d3pds = ["mc12_8TeV.other.merge"])

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
