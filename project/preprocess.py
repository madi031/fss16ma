from sklearn import preprocessing
import tableReader, num, math, numpy
from sklearn.decomposition import PCA

class preprocess:     
    def missingValue(self,table):
        for colPos in range(len(table.cols)):
            col = [] 
            for row in table.rows:
                col.append(row[colPos])
            mynewlist = [s for s in col if self.is_number(s)]
            if len(mynewlist) != len(col):
                medianValue = numpy.median(mynewlist)
                for i, val in enumerate(col):
                    if not self.is_number(val):
                        table.rows[i][colPos] = medianValue
        return table
    def is_number(self,i):
        try:
            float(i)
            return True
        except ValueError:
            return False

    def norm(self, table):
        for colPos in range(len(table.cols)-1):
            allValues = [] 
            for row in table.rows:
                allValues.append(row[colPos])

            maxValue = max(allValues)
            minValue = min(allValues)

            for i, actual_value in enumerate(allValues):
                table.rows[i][colPos] =  float(actual_value - minValue)/(maxValue - minValue) 

        return table

    def logarithm(self, table):
    	for i in range(len(table.cols)-1):
            for row in table.rows:
                row[i] = math.log(row[i])
    	
        return table

    def width5bin(self, table):        
        for colPos in range(len(table.cols)-1):
            allValues = [] 
            for row in table.rows:
                allValues.append(row[colPos])
            maxValue = max(allValues)
            minValue = min(allValues)
            print maxValue, minValue

            binWidth = (maxValue - minValue)/5

            bins = []
            for i in range(5):
                bins.append(minValue + binWidth*i )

            allValues = numpy.digitize(allValues, bins)

            for i, actual_value in enumerate(allValues):
                table.rows[i][colPos] =  actual_value 
        return table

    def freq5bin(self, table):
        numOfInstances = len(table.rows)
        
        for colPos in range(len(table.cols)-1):
            allValues = {} 
            for row in table.rows:
                allValues[row.rid] = row[colPos]

            sortedIndex = sorted(allValues, key=allValues.__getitem__)
            
            for i, index in enumerate(sortedIndex):
                table.rows[index-1][colPos] = math.floor(i/math.ceil(numOfInstances/5.0)) + 1
        
        return table

    def pca(self, table, n = 2):
        X =[]
        Y =[]
        for i, row in enumerate(table.rows):
            X.append(table.rows[row.rid-1][:-1])
            Y.append(table.rows[row.rid-1][-1])
            
        pca = PCA(n_components = n)
        pca.fit(X)
        result = pca.transform(X)

        newTable = tableReader.Table()
        for i,row in enumerate(result):
            row = numpy.append(row, Y[i])
            newTable.add_row(row)
        
        return newTable 




        