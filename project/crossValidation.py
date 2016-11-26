import tableReader, errorMeasurement, random, learners
class ErrorMeasure:    
    def __init__(self):
        self.mar = []
        self.mmre = []
        self.mdmre = []
        self.mmer = []
        self.mbre = []
        self.mibre = []
        self.pred25 = []

class crossValidation:
    def cv(self, table,learner, m = 5,n = 5):
        errorMeasures = ErrorMeasure()
        for i in range(m):
            random.shuffle(table.rows)
            for j in range(n):
                testData = tableReader.Table()
                trainData = tableReader.Table()
                testIndex = []
                numOfTestInstances = len(table.rows)/n
                for k in range(numOfTestInstances*j, numOfTestInstances*(j+1)):
                    testData.add_row(table.rows[k].contents)
                    testIndex.append(table.rows[k].rid)
                
                for row in table.rows: 
                    if row.rid not in testIndex:
                        trainData.add_row(row.contents)

                if learner == "lReg" or learner == "pcr":
                    actual, predicted = learners.learners().lReg(trainData,testData)
                elif learner == "cartNo":
                    actual, predicted = learners.learners().cartNo(trainData,testData)
                elif learner == "plsr":
                    actual, predicted = learners.learners().plsr(trainData, testData)
                elif learner == "abe0_1NN":
                    actual, predicted = learners.learners().abe0_kNN(trainData, testData, 1)
                elif learner == "abe0_5NN":
                    actual, predicted = learners.learners().abe0_kNN(trainData, testData, 5)
                else:
                    actual, predicted = learners.learners().lReg(trainData,testData)

                x = errorMeasurement.errorMeasurement().calculateErrorMeasure(actual, predicted, errorMeasures)
        
        print x.mar
        
			