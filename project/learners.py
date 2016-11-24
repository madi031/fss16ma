import math
import random
from sklearn import tree
import errorMeasurement, preprocess
from sklearn import linear_model
from sklearn.cross_decomposition import PLSRegression



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

        predicted = clf.predict(testX)
        actual = testY

        return errorMeasurement.errorMeasurement().calculateErrorMeasure(actual, predicted)

    def lReg(self, trainingData, testData):

        trainX,trainY, testX, testY = self.splitXY(trainingData,testData)

        regr = linear_model.LinearRegression()
        regr.fit(trainX, trainY)
        predicted = regr.predict(testX)
        actual = testY


        return errorMeasurement.errorMeasurement().calculateErrorMeasure(actual, predicted)

    def plsr(self,trainingData, testData):
        
        trainX,trainY, testX, testY = self.splitXY(trainingData,testData)

        pls2 = PLSRegression(n_components=2)
        pls2.fit(trainX, trainY)
        predicted = pls2.predict(testX)
        actual = testY

        return errorMeasurement.errorMeasurement().calculateErrorMeasure(actual, predicted) 

    def pcr(self, table):
        #Call PCA and then cross val is performed before lReg 
        newTable = preprocess.preprocess().pca(table)  
        return self.lReg(newTable)

    def abe0_kNN(self,trainingData, testData,k):

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
            return (row[-1], max_class)

        def predict(row) :
            return knn(row)

        
        for row in testData.rows:
            print predict(row)


