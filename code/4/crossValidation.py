import tableReader, random, kNN
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
    def cv(self, table,m = 5,n = 5):
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

                actual, predicted = kNN.kNN().abe0_kNN(trainData,testData,1)
                print i, actual, predicted 
                # x = errorMeasurement.errorMeasurement().calculateErrorMeasure(actual, predicted, errorMeasures)
        
        # print x.mar

			