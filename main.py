from DataCenter.index import DataCenter
from Machine.index import Machine

dataCenter = DataCenter("connect4.data")

dataCenter.separateIntoRatioAccording()
dataCenter.separateIntoRatioAccording()
dataCenter.separateIntoRatioAccording()

ratioList = [[90,10],[80,20],[60,40],[40,60]]

for ratio in ratioList:
    dataCenter.separateIntoRatioAccording(ratio)
    machine = Machine(ratio,8)
    machine.train()
    machine.test()
    machine.plotConfusionMatrix()
    machine.drawDecisionTree()


