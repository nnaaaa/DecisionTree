import random
from typing import List
class DataCenter:
    textPath = "DataCenter/text/"
    matrixPath = "DataCenter/matrix/"
    treePath = "DataCenter/tree/"
    label = [
        'C1', ' C2', ' C3', ' C4', ' C5', ' C6', ' C7', 
        ' C8', ' C9', ' C10', ' C11', ' C12', ' C13', 
        ' C14', ' C15', ' C16', ' C17', ' C18', ' C19', 
        ' C20', ' C21', ' C22', ' C23', ' C24', ' C25', 
        ' C26', ' C27', ' C28', ' C29', ' C30', ' C31', 
        ' C32', ' C33', ' C34', ' C35', ' C36', ' C37', 
        ' C38', ' C39', ' C40', ' C41', ' C42'
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

    