import math
class learners:
	actual_value = None
	pred_value = None
	def abe0_1nn:
		ar = []
		mre = []
		mer = 0
		bre = 0
		ibre = 0
		sumPred25 = 0
		for r in test_table: 
            print "Row : ", r
            nearest_neighbor = training_table.find_nearest(r)
            print "Nearest neighbor : ", nearest_neighbor
            pred_value = nearest_neighbor[-1]
            actual_value = r[-1]
            ar.append(absoluteResidual())
            mre.append(mRE())
            mer += mER()
            bre += bRE()
            ibre += iBRE()
            sumPred25 += isPred25()


        mar = float(sum(ar)) / max(len(ar), 1)
        mmre = float(sum(mmre)) / max(len(mmre), 1)
       	mdmre = median(mre)
       	mmer = float(mer) / max(len(ar), 1)
       	mbre = float(bre) / max(len(ar), 1)
       	mibre = float(ibre) / max(len(ar),1)
       	pred25 = float(sumPred25) / max(len(ar), 1)

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


    def absoluteResidual(a = self.actual_value, b = self.pred_value):
    	return abs(a - b)

    def mRE(self):
    	return float(absoluteResidual(self.actual_value, self.pred_value))/self.actual_value

    def mER(self):
    	return float(absoluteResidual(self.actual_value, self.pred_value))/self.pred_value

    def bRE(self):
    	return float(absoluteResidual(self.actual_value, self.pred_value)) / min(self.pred_value, self.actual_value)

    def iBRE(self):
    	return float(absoluteResidual(self.actual_value, self.pred_value)) / max(self.pred_value, self.actual_value)

    def isPred25(self):
    	if self.pred_value >= 0.75 * self.actual_value and self.pred_value <= 1.25 * self.actual_value: 
    		return 1 
    	else 
    		return 0  