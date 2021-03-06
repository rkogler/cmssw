import FWCore.ParameterSet.Config as cms

#pileupSummary = cms.EDProducer("PileupInformation",
addPileupInfo = cms.EDProducer("PileupInformation",

    TrackingParticlesLabel = cms.string('mergedtruth'),
    PileupMixingLabel = cms.string('mix'),
    simHitLabel = cms.string('g4SimHits'),
    volumeRadius = cms.double(1200.0),
    vertexDistanceCut = cms.double(0.003),
    volumeZ = cms.double(3000.0),
    pTcut_1 = cms.double(0.1),
    pTcut_2 = cms.double(0.5)                               

)

#addPileupInfo = cms.Sequence(pileupSummary)
