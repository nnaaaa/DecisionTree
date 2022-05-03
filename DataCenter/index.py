import random
from typing import List
class DataCenter:
    textPath = "DataCenter/text/"
    matrixPath = "DataCenter/matrix/"
    treePath = "DataCenter/tree/"
    label = [
        'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 
        'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 
        'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 
        'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 
        'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 
        'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 
        'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 
    ]
    def __init__(self,filename: str,isSuffle = True) -> None:
        self.data = DataCenter.readFromFile(filename)
        if isSuffle:
            random.shuffle(self.data)

    def separateIntoRatioAccording(self,ratio:List[int] = [90,10]):
        trainFile = open(DataCenter.textPath + "feature_train_"+ str(ratio[0]) + "_" + str(ratio[1]) + ".dat","w")
        testFile = open(DataCenter.textPath +"feature_test_"+ str(ratio[0]) + "_" + str(ratio[1]) + ".dat","w")
        labelTrainFile = open(DataCenter.textPath +"label_train_"+ str(ratio[0]) + "_" + str(ratio[1]) + ".dat","w")
        labelTestFile = open(DataCenter.textPath +"label_test_"+ str(ratio[0]) + "_" + str(ratio[1]) + ".dat","w")

        splitPosition = int(ratio[0] / 100 * len(self.data))

        trainFile.write(''.join(map(lambda line: line[:83] + '\n',self.data[ :splitPosition])))
        testFile.write(''.join(map(lambda line: line[:83] + '\n',self.data[splitPosition :])))
        labelTrainFile.write(''.join(map(lambda line: line[84:],self.data[ :splitPosition])))
        labelTestFile.write(''.join(map(lambda line: line[84:],self.data[splitPosition :])))

        trainFile.close()
        testFile.close()
        labelTrainFile.close()
        labelTestFile.close()

    @staticmethod
    def readFromFile(filename: str):
        file = open(filename, 'r')
        data = file.readlines()
        file.close()
        return data

    