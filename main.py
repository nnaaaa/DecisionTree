from DataCenter.index import DataCenter
from Machine.index import Machine

dataCenter = DataCenter("connect4.data")

# run for many ratio
ratioList = [[90,10],[80,20],[60,40],[40,60]]
for ratio in ratioList:
    dataCenter.separateIntoRatioAccording(ratio)
    machine = Machine(ratio)
    machine.train()
    machine.test()
    machine.plotConfusionMatrix()
    machine.drawDecisionTree()
    print('\n\n')

# run for many max_depth 
for i in range(2,8):
    dataCenter.separateIntoRatioAccording([80,20])
    machine = Machine([80,20],i)
    machine.train()
    machine.test()
    machine.plotConfusionMatrix()
    machine.drawDecisionTree()
    print('\n\n')




