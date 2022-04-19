import random
from typing import List
class DataCenter:
    def __init__(self,filename: str,isSuffle = True) -> None:
        self.data = DataCenter.readFromFile(filename)
        if isSuffle:
            random.shuffle(self.data)

    def separateIntoRatioAccording(self,ratio:List[int] = [90,10]):
        trainFile = open("DataCenter/feature_train_"+ str(ratio[0]) + "_" + str(ratio[1]) + ".dat","w")
        testFile = open("DataCenter/feature_test_"+ str(ratio[0]) + "_" + str(ratio[1]) + ".dat","w")
        labelTrainFile = open("DataCenter/label_train_"+ str(ratio[0]) + "_" + str(ratio[1]) + ".dat","w")
        labelTestFile = open("DataCenter/label_test_"+ str(ratio[0]) + "_" + str(ratio[1]) + ".dat","w")

        splitPosition = int(ratio[0] / 100 * len(self.data))

        trainFile.write(''.join(map(lambda line: line[:84] + '\n',self.data[ :splitPosition])))
        testFile.write(''.join(map(lambda line: line[:84] + '\n',self.data[splitPosition :])))
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

    