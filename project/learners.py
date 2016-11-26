import math
import random
from sklearn import tree, linear_model, cross_decomposition

class learners:

    def splitXY(self, trainingData, testData) :
        trainX =[]
        trainY= []
        testX = []
        testY = []
        for i,row in enumerate(trainingData.rows):
            trainX.append(trainingData.rows[i][:-1])
            trainY.append(trainingData.rows[i][-1])

        for i,row in enumerate(testData.rows):
            testX.append(testData.rows[i][:-1])
            testY.append(testData.rows[i][-1])
        
        return trainX,trainY, testX, testY

    def cartNo(self,trainingData, testData):
        
        trainX,trainY, testX, testY = self.splitXY(trainingData,testData)

        clf = tree.DecisionTreeRegressor()
        clf = clf.fit(trainX,trainY)

        return testY, clf.predict(testX)

    def lReg(self, trainingData, testData):

        trainX,trainY, testX, testY = self.splitXY(trainingData,testData)

        regr = linear_model.LinearRegression()
        regr.fit(trainX, trainY)
        
        return testY, regr.predict(testX)

    def plsr(self,trainingData, testData):
        
        trainX,trainY, testX, testY = self.splitXY(trainingData,testData)

        plsrModel = cross_decomposition.PLSRegression(n_components=2)
        plsrModel.fit(trainX, trainY)
        
        return testY, plsrModel.predict(testX)

    def abe0_kNN(self,trainingData, testData,k):

        actual = []
        predicted = []

        def knn(row) :
            distances = [(trainingData.row_distance(row, data), data[-1]) for data in trainingData.rows]
            distances = sorted(distances, key = lambda x : x[0])
            classCounts = {}
            max_class = None
            for cl in distances[ : k] :
                cl = cl[1]
                if max_class is None:
                    max_class = cl
                count = classCounts.get(cl, 0)
                classCounts[cl] = count = count + 1
                if classCounts[max_class] < count :
                    max_class = cl
            actual.append(row[-1])
            predicted.append(max_class)

        for row in testData.rows:
            knn(row)

        return actual, predicted


