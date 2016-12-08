import tableReader, errorMeasurement, random, learners, stats
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
                
                x = errorMeasurement.errorMeasurement().calculateErrorMeasure(actual, predicted, errorMeasures)
        return x
    
    @staticmethod
    def error_metrics_to_file(base_filename, solo, errors):
        
        mar_file = open(base_filename + "_mar.txt", "a")
        for v in errors.mar :
            mar_file.write(solo + "," + str(v) + "\n")
        
        mmre_file = open(base_filename + "_mmre.txt", "a")
        for v in errors.mmre :
            mmre_file.write(solo + "," + str(v) + "\n")

        mdmre_file = open(base_filename + "_mdmre.txt", "a")
        for v in errors.mdmre :
            mdmre_file.write(solo + "," + str(v) + "\n")

        mmer_file = open(base_filename + "_mmer.txt", "a")
        for v in errors.mmer :
            mmer_file.write(solo + "," + str(v) + "\n")

        mbre_file = open(base_filename + "_mbre.txt", "a")
        for v in errors.mbre :
            mbre_file.write(solo + "," + str(v) + "\n")

        mibre_file = open(base_filename + "_mibre.txt", "a")
        for v in errors.mibre :
            mibre_file.write(solo + "," + str(v) + "\n")

        pred25_file = open(base_filename + "_pred25.txt", "a")
        for v in errors.pred25 :
            pred25_file.write(solo + "," + str(v) + "\n")
