import sys, tableReader

class kNN:
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
