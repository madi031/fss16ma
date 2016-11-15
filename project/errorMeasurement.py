import math, numpy

class errorMeasurement:    
    def __init__(self):
        self.actual_value = 0
        self.pred_value = 0
            
    def calculateErrorMeasure(self, actual, predicted):
        ar = []
        mre = []
        mer = 0
        bre = 0
        ibre = 0
        sumPred25 = 0
        for i, actualValue in enumerate(actual):
            self.actual_value = actualValue
            self.pred_value = predicted[i]
            ar.append(self.absoluteResidual())
            mre.append(self.mRE())
            mer += self.mER()
            bre += self.bRE()
            ibre += self.iBRE()
            sumPred25 += self.isPred25()

        errorMeasures = {}
        
        errorMeasures['mar'] = float(sum(ar)) / max(len(ar), 1)
        errorMeasures['mmre'] = float(sum(mre)) / max(len(ar), 1)
        errorMeasures['mdmre'] = numpy.median(mre)
        errorMeasures['mmer'] = float(mer) / max(len(ar), 1)
        errorMeasures['mbre'] = float(bre) / max(len(ar), 1)
        errorMeasures['mibre'] = float(ibre) / max(len(ar),1)
        errorMeasures['pred25'] = float(sumPred25) / max(len(ar), 1)
        return errorMeasures

    def absoluteResidual(self):
    	return abs(self.actual_value - self.pred_value)

    def mRE(self):
    	return float(self.absoluteResidual())/self.actual_value

    def mER(self):
    	return float(self.absoluteResidual())/self.pred_value

    def bRE(self):
    	return float(self.absoluteResidual()) / min(self.pred_value, self.actual_value)

    def iBRE(self):
    	return float(self.absoluteResidual()) / max(self.pred_value, self.actual_value)

    def isPred25(self):
    	if self.pred_value >= 0.75 * self.actual_value and self.pred_value <= 1.25 * self.actual_value: 
           return 1 
        else: 
            return 0  