from typing import List
import graphviz
from matplotlib import pyplot as plot
from State.index import FourConnectState
from DataCenter.index import DataCenter
from sklearn import tree,metrics

class Machine:
    def __init__(self,ratioTrainTest=[90,10],maxDepth = None) -> None:
        self.decistionTree = None
        self.ratioString = ''
        self.ratio = ratioTrainTest
        self.maxDepth = maxDepth
        self.Y_predict = []
        self.Y_actual = []

    def train(self):
        self.ratioString = str(self.ratio[0]) + "_" + str(self.ratio[1])

        trainData = DataCenter.readFromFile(DataCenter.textPath + "feature_train_" + self.ratioString + ".dat")
        labelTrainData = DataCenter.readFromFile(DataCenter.textPath + "label_train_" + self.ratioString + ".dat")
        
        print("Training Stage")
        trainingStates:List[FourConnectState] = []
        for i in range(len(trainData)):
            state = FourConnectState(trainData[i],labelTrainData[i])
            trainingStates.append(state)
        X = list(map(lambda state: state.state, trainingStates))
        Y = list(map(lambda state: state.result, trainingStates))
        winLabels = []
        lossLabels = []
        drawLabels = []
        for label in Y:
            if label == "win":
                winLabels.append(label)
            elif label == "loss":
                lossLabels.append(label)
            elif label == "draw":
                drawLabels.append(label)
        
        print(" - Win label amount: ",len(winLabels), f"({str(round(len(winLabels)/len(Y)*100,2))}%)")
        print(" - Loss label amount: ",len(lossLabels), f"({str(round(len(lossLabels)/len(Y)*100,2))}%)")
        print(" - Draw label amount: ",len(drawLabels), f"({str(round(len(drawLabels)/len(Y)*100,2))}%)")
        self.decisionTree = tree.DecisionTreeClassifier(criterion="gini",max_depth=self.maxDepth).fit(X, Y)
        self.maxDepth = self.decisionTree.tree_.max_depth
        print('Max depth: ', self.maxDepth)
        

    def test(self):
        testData = DataCenter.readFromFile(DataCenter.textPath + "feature_test_" + self.ratioString + ".dat")
        labelTestData = DataCenter.readFromFile(DataCenter.textPath + "label_test_" + self.ratioString + ".dat")
        print("Testing Stage")
        testingStates:List[FourConnectState] = []
        for i in range(len(testData)):
            state = FourConnectState(testData[i],labelTestData[i])
            testingStates.append(state)

        X = list(map(lambda state: state.state, testingStates))
        self.Y_actual = list(map(lambda state: state.result, testingStates))
        
        if self.decisionTree:
            self.Y_predict = self.decisionTree.predict(X) 
            accuracyScore = metrics.accuracy_score(self.Y_actual, self.Y_predict)
            print('Accuracy: ', accuracyScore)

    def plotConfusionMatrix(self):
        print('Plot confusion matrix')
        metrics.ConfusionMatrixDisplay.from_predictions(self.Y_actual, self.Y_predict, labels=self.decisionTree.classes_)
        plot.savefig(DataCenter.matrixPath + 'confusion_matrix_'+self.ratioString)
        # labels argument is ["win","loss","draw"]
        print(metrics.classification_report(self.Y_actual, self.Y_predict, labels=self.decisionTree.classes_,zero_division=0))

    def drawDecisionTree(self):
        print('Draw decision tree')
        graphData = tree.export_graphviz(
            filled=True,
            rounded=True,
            max_depth=self.maxDepth,
            feature_names=DataCenter.label,
            decision_tree=self.decisionTree,
        ) 

        graph = graphviz.Source(graphData) 
        graph.render(filename='descision_tree_'+self.ratioString+'_max_depth_'+ str(self.maxDepth),format='png',directory=DataCenter.treePath)