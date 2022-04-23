# Connect-4 Decision tree

## How to use:

### Prerequisites

>Download Python compiler

>Install pip
```
pip install graphviz sklearn matplotlib
```
```
sudo apt-get install graphviz
```

### To run:
```
make
```
or
```
python3 main.py
```

### To clean cache:
```
make clean
```

# Assignment requirements

### Source code overview:
```
├── main.py
├── connect4.data
├── DataCenter
│   ├── index.py
│   ├── feature_test_40_60.dat
│   ├── feature_test_60_40.dat
│   ├── feature_test_80_20.dat
│   ├── feature_test_90_10.dat
│   ├── feature_train_40_60.dat
│   ├── feature_train_60_40.dat
│   ├── feature_train_80_20.dat
│   ├── feature_train_90_10.dat
│   ├── label_test_40_60.dat
│   ├── label_test_60_40.dat
│   ├── label_test_80_20.dat
│   ├── label_test_90_10.dat 
│   ├── label_train_40_60.dat 
│   ├── label_train_60_40.dat 
│   ├── label_train_80_20.dat 
│   └── label_train_90_10.dat
├── State
│   └── index.py
└── Machine
    └── index.py
```

## Preparing the datasets

> ### DataCenter
> Read data from connect4.data and seperate according to ratio respectively ((`train/test`) `40/60`, `60/40`, `80/20`, and `90/10`)
> <br> After prepare train and test data. I read lines by lines and convert to form `State`



## Building the decision tree classifiers

> ### State
> This class will convert ['b','x','o'] to ['0','-1','1'] and save to state, ['win','lose','draw'] is saved to result 

```
state: [
    0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 1, 0, 
    0, 0, 0, 0, -1, 1, -1, 
    1, -1, 0, -1, 1, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0
]
result: "draw"
```

> ### Machine
```python
class Machine
    #you can provide ratio and max depth for the machine
    def __init__(self,ratio=[90,10],maxDepth = None):

    # First, let the machine training itself
    def train(self):

    # Second, machine perform test 
    def test(self):

    # you can plot confusion matrix to statistic
    def plotConfusionMatrix(self):

    # or draw decision tree to illustrate the process    
    def drawDecisionTree(self):
```

## Evaluating the decision tree classifiers

- [x] Train/Test is 40/60
    - ### Confusion Matrix: ![](DataCenter/matrix/confusion_matrix_40_60.png)
    - ### Classification Report: 
        |                 | precision     |  recall   | f1-score      | support |
        | ------------    | ---------     | --------- | ------------  | ------  |
        |  draw           |      0.28     |     0.28  |     0.28      |    3876 |
        |  loss           |     0.66      |    0.66   |     0.66      |   9942  |
        |  win            |   0.85        |  0.85     |  0.85         |  26717  |
        | accuracy        |               |           |  0.75         |  40535  |
        | macro avg       |  0.60         |   0.60    |  0.60         |  40535  |
        | weighted avg    |   0.75        |    0.75   |   0.75        |   40535 |   

- [x] Train/Test is 60/40
    - ### Confusion Matrix: ![](DataCenter/matrix/confusion_matrix_60_40.png)
    - ### Classification Report: 
        |                 | precision     |  recall   | f1-score      | support |
        | ------------    | ---------     | --------- | ------------  | ------  |
        |  draw           |      0.28     |     0.28  |     0.28      |    3876 |
        |  loss           |     0.66      |    0.66   |     0.66      |   9942  |
        |  win            |   0.85        |  0.85     |  0.85         |  26717  |
        | accuracy        |               |           |  0.75         |  40535  |
        | macro avg       |  0.60         |   0.60    |  0.60         |  40535  |
        | weighted avg    |   0.75        |    0.75   |   0.75        |   40535 |    

- [x] Train/Test is 80/20
    - ### Confusion Matrix: ![](DataCenter/matrix/confusion_matrix_80_20.png)
    - ### Classification Report: 
        |                 | precision     |  recall   | f1-score      | support |
        | ------------    | ---------     | --------- | ------------  | ------  |
        |  draw           |      0.28     |     0.28  |     0.28      |    3876 |
        |  loss           |     0.66      |    0.66   |     0.66      |   9942  |
        |  win            |   0.85        |  0.85     |  0.85         |  26717  |
        | accuracy        |               |           |  0.75         |  40535  |
        | macro avg       |  0.60         |   0.60    |  0.60         |  40535  |
        | weighted avg    |   0.75        |    0.75   |   0.75        |   40535 |    

- [x] Train/Test is 90/10
    - ### Confusion Matrix: ![](DataCenter/matrix/confusion_matrix_90_10.png)
    - ### Classification Report: 
        |                 | precision     |  recall   | f1-score      | support |
        | ------------    | ---------     | --------- | ------------  | ------  |
        |  draw           |      0.28     |     0.28  |     0.28      |    3876 |
        |  loss           |     0.66      |    0.66   |     0.66      |   9942  |
        |  win            |   0.85        |  0.85     |  0.85         |  26717  |
        | accuracy        |               |           |  0.75         |  40535  |
        | macro avg       |  0.60         |   0.60    |  0.60         |  40535  |
        | weighted avg    |   0.75        |    0.75   |   0.75        |   40535 |                     




## The depth and accuracy of a decision tree
> This task works on the 80/20 training set and test set

- [x] Decision Tree
    - ### Max depth = None ![](DataCenter/tree/descision_tree_80_20_max_depth_38.png)
    - ### Max depth = 2 ![](DataCenter/tree/descision_tree_80_20_max_depth_2.png)
    - ### Max depth = 3 ![](DataCenter/tree/descision_tree_80_20_max_depth_3.png)
    - ### Max depth = 4 ![](DataCenter/tree/descision_tree_80_20_max_depth_4.png)
    - ### Max depth = 5 ![](DataCenter/tree/descision_tree_80_20_max_depth_5.png)
    - ### Max depth = 6 ![](DataCenter/tree/descision_tree_80_20_max_depth_6.png)
    - ### Max depth = 7 ![](DataCenter/tree/descision_tree_80_20_max_depth_7.png)



- [x] Accuracy table
    | max_depth | None  | 2     | 3     | 4     | 5     | 6     | 7     |
    | --------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
    | accuracy  | 0.77 | 0.67 | 0.69 |  0.69 | 0.70 | 0.72 | 0.72 |

- [x] Comment: the `accuracy` increase proportionally to the `max_depth`. 
The higher the `max_depth` is, the higher the `accuracy` is


## Grading

| No    | Specifications                             | Scores (%) | Complete (%) |
| ----- | ------------------------------------------ | ---------- | ------------ |
| 1     | Preparing the datasets                     | 20         | 100          |
| 2     | Building the decision tree classifiers     | 20         | 100          |
| 3     | Evaluating the decision tree classifiers   |            |              |
|       | Classification report and confusion matrix | 20         | 100          |
|       | Comments                                   | 10         | 100          |
| 4     | The depth and accuracy of a decision tree  |            |              |
|       | Trees, tables, and charts                  | 20         | 100          |
|       | Comments                                   | 10         | 100          |
| Total |                                            | 100        | 100          |

References
- [1] Scikit-learn decision trees: https://scikit-learn.org/stable/modules/tree.html
- [2] Tutorial: https://github.com/lamnguyen5464/Connect-4-decicion-tree
- [3] How to use sklearn.tree: https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier
- [4] How to use sklearn.metric: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report


