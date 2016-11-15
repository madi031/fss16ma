import math
import random
from sklearn import tree

class learners:
    actual_value = None
    pred_value = None
	# def abe0_1nn(self):
	# 	ar = []
	# 	mre = []
	# 	mer = 0
	# 	bre = 0
	# 	ibre = 0
	# 	sumPred25 = 0
	# 	for r in test_table: 
 #            print "Row : ", r
 #            nearest_neighbor = training_table.find_nearest(r)
 #            print "Nearest neighbor : ", nearest_neighbor
 #            pred_value = nearest_neighbor[-1]
 #            actual_value = r[-1]
 #            ar.append(absoluteResidual())
 #            mre.append(mRE())
 #            mer += mER()
 #            bre += bRE()
 #            ibre += iBRE()
 #            sumPred25 += isPred25()


 #        mar = float(sum(ar)) / max(len(ar), 1)
 #        mmre = float(sum(mmre)) / max(len(mmre), 1)
 #       	mdmre = median(mre)
 #       	mmer = float(mer) / max(len(ar), 1)
 #       	mbre = float(bre) / max(len(ar), 1)
 #       	mibre = float(ibre) / max(len(ar),1)
 #       	pred25 = float(sumPred25) / max(len(ar), 1)

  #   def errorMeasures():
  #   	ar = []
		# mre = []
		# mer = []
		# bre =[]
		# ibre = []
		# for r in test_table:
		# 	ar.append(absoluteResidual())
  #           mre.append(mRE())
  #           mer.append(mER())
  #           bre.append(bRE())
  #           ibre.append(iBRE())
  #       mar = float(sum(ar)) / max(len(ar), 1)
  #       mmre = float(sum(mmre)) / max(len(mmre), 1)
  #      	mdmre = median(mre)
  #      	mmer = float(sum(mer)) / max(len(mer), 1)
  #      	mbre = float(sum(bre)) / max(len(bre), 1)
  #      	mibre = float(sum(ibre)) / max(len(ibre),1)
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

        print clf.predict(testX)
        print testY



    def absoluteResidual(self, a = actual_value, b = pred_value):
    	return abs(a - b)

    def mRE(self):
    	return float(absoluteResidual(actual_value, pred_value))/actual_value

    def mER(self):
    	return float(absoluteResidual(actual_value, pred_value))/pred_value

    def bRE(self):
    	return float(absoluteResidual(actual_value, pred_value)) / min(pred_value, actual_value)

    def iBRE(self):
    	return float(absoluteResidual(actual_value, pred_value)) / max(pred_value, actual_value)

    def isPred25(self):
    	if pred_value >= 0.75 * actual_value and pred_value <= 1.25 * actual_value: 
           return 1 
        else: 
            return 0  