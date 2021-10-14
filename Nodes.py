class Node:
    def __init__(self, id, x, y, initEnergy, energyTransfer, energyReceive,
                 energyFreeSpace, energyMultiPath, energyAgg, isDead, numPkts, dataPktSize):
        self.id = id
        self.x = x,
        self.y = y
        self.initEnergy = initEnergy
        self.energyTransfer = energyTransfer
        self.energyReceive = energyReceive
        self.energyFreeSpace = energyFreeSpace
        self.energyMultiPath = energyMultiPath
        self.energyAgg = energyAgg
        self.isDead = isDead
        self.numPkts = numPkts
        self.dataPktSize = dataPktSize
