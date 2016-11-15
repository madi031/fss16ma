import math
import random
from sklearn import tree
import errorMeasurement

class learners:
    def cartYes(self,table):
        trainingData = random.sample(table.rows, int(len(table.rows)*.7))
        trainingIndex = []
        for i in trainingData:
            trainingIndex.append(i.rid)
        testData =[]
        for row in table.rows:
            if row.rid not in trainingIndex:
                testData.append(row)

        
        X =[]
        y= []
        testX = []
        testY = []
        for i,row in enumerate(trainingData):
            X.append(trainingData[i][:-1])
            y.append(trainingData[i][-1])

        for i,row in enumerate(testData):
            testX.append(testData[i][:-1])
            testY.append(testData[i][-1])

        clf = tree.DecisionTreeRegressor()
        clf = clf.fit(X,y)

        predicted = clf.predict(testX)
        actual = testY

        errorMeasures = errorMeasurement.errorMeasurement().calculateErrorMeasure(actual, predicted)