from typing import List
from State.index import FourConnectState
from DataCenter.index import DataCenter
from sklearn import tree,metrics

dataCenter = DataCenter("connect4.data")
dataCenter.separateIntoRatioAccording([90,10])
dataCenter.separateIntoRatioAccording([80,20])
dataCenter.separateIntoRatioAccording([60,40])
dataCenter.separateIntoRatioAccording([40,60])


def experiment(ratio=[90,10],maxDeepth=2,plotDecisionTree=False,plotConfusionMatrix=False):
    trainData = DataCenter.readFromFile("DataCenter/feature_train_" + str(ratio[0]) + "_" + str(ratio[1]) + ".dat")
    testData = DataCenter.readFromFile("DataCenter/feature_test_" + str(ratio[0]) + "_" + str(ratio[1]) + ".dat")
    labelTrainData = DataCenter.readFromFile("DataCenter/label_train_" + str(ratio[0]) + "_" + str(ratio[1]) + ".dat")
    labelTestData = DataCenter.readFromFile("DataCenter/label_test_" + str(ratio[0]) + "_" + str(ratio[1]) + ".dat")


    print("Training Stage")
    trainingStates:List[FourConnectState] = []
    for i in range(len(trainData)):
        state = FourConnectState(trainData[i],labelTrainData[i])
        trainingStates.append(state)
    X = list(map(lambda state: state.state, trainingStates))
    Y = list(map(lambda state: state.result, trainingStates))
    decisionTree = tree.DecisionTreeClassifier(criterion="entropy",max_depth=maxDeepth).fit(X, Y)

    print('Max depth: ', decisionTree.tree_.max_depth)

    print("Testing Stage")
    testingStates:List[FourConnectState] = []
    for i in range(len(trainData)):
        state = FourConnectState(testData[i],labelTestData[i])
        testingStates.append(state)

    X = list(map(lambda state: state.state, trainingStates))
    Y_actual = list(map(lambda state: state.result, trainingStates))
    
    Y_predict = decisionTree.predict(X)
    accuracyScore = metrics.accuracy_score(Y_actual, Y_predict)
    print('Accuracy: ', accuracyScore)


experiment()
