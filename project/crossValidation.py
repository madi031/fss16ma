import tableReader, random, learners

class crossValidation:
    def cv(self, table,m = 5,n = 5):
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

                print learners.learners().abe0_kNN(trainData,testData,1 )

			