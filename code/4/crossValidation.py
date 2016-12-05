import tableReader, random, errorMeasurement, knn, abcd, stats
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

        pd_outputs = {}
        pf_outputs = {}
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
                x = knn.learners(trainData, testData, "kNN")
                p = abcd.Abcd('kNN', 'db')
                [p(x1[0], x1[1]) for x1 in x]
                
                report = p.report()
                print report
                pd = report[0][8]
                pf = report[0][9]

                if "kNN" in pd_outputs :
                    pd_outputs["kNN"].append(pd)
                else :
                    pd_outputs["kNN"] = [pd]

                if "kNN" in pf_outputs :
                    pf_outputs["kNN"].append(pf)
                else :
                    pf_outputs["kNN"] = [pf]


                x = knn.learners(trainData, testData, "KMeans")
                p = abcd.Abcd('KMeans', 'db')
                [p(x1[0], x1[1]) for x1 in x]
                
                report = p.report()
                print report
                pd = report[0][8]
                pf = report[0][9]

                if "KMeans" in pd_outputs :
                    pd_outputs["KMeans"].append(pd)
                else :
                    pd_outputs["KMeans"] = [pd]

                if "KMeans" in pf_outputs :
                    pf_outputs["KMeans"].append(pf)
                else :
                    pf_outputs["KMeans"] = [pf]

                x = knn.learners(trainData, testData, "KDTree")
                p = abcd.Abcd('KDTree', 'db')
                [p(x1[0], x1[1]) for x1 in x]
                
                report = p.report()
                print report
                pd = report[0][8]
                pf = report[0][9]

                if "KDTree" in pd_outputs :
                    pd_outputs["KDTree"].append(pd)
                else :
                    pd_outputs["KDTree"] = [pd]

                if "KDTree" in pf_outputs :
                    pf_outputs["KDTree"].append(pf)
                else :
                    pf_outputs["KDTree"] = [pf]

        print "PD"
        stats.rdivDemo( [ [k] + v for k,v in pd_outputs.items() ] )
        
        print "PF"
        stats.rdivDemo( [ [k] + v for k,v in pf_outputs.items() ] )