# NMSSM Hto2Ato4mu 13TeV pythia8 configuration file
import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter(
    "Pythia8GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    crossSection = cms.untracked.double(0.0),
    comEnergy = cms.double(13000.0),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythiaUESettings = cms.vstring(),
        processParameters = cms.vstring(
            'Higgs:useBSM = on',      # Initialize and use the two-Higgs-doublet BSM states
            'HiggsBSM:all = off',      # Switch off all BSM Higgs production
            'HiggsBSM:gg2H2 = on',     # Switch on gg->H^0(H_2^0) scattering via loop contributions primarily from top. Code 1022.
            '35:m0 = 125.0',           #  mass in GeV of H0 (PDG ID = 35)
            # decays of H0 (PDG ID = 35)
            '35:onMode = off',
            'HiggsH2:coup2A3A3 = .01',
            'HiggsA3:coup2d = 0.0',
            'HiggsA3:coup2u = 0.0',
            '35:onIfMatch = 36 36',
            '36:mMin = 0.1',
            '36:m0 = 0.25',
            '36:onMode = off',
            '35:onIfMatch = 13 -13',
        ),
        parameterSets = cms.vstring(
            'pythiaUESettings',
            'pythia8CommonSettings',
            'pythia8CP5Settings',
            'processParameters'
            )
        )
    )
