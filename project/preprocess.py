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
            allValues = [row[colPos] for row in table.rows]

            maxValue = max(allValues)
            minValue = min(allValues)

            for i, actual_value in enumerate(allValues):
                table.rows[i][colPos] =  float(actual_value - minValue)/max((maxValue - minValue),1) 

        return table

    def logarithm(self, table):
    	for i in range(len(table.cols)-1):
            for row in table.rows:
                try:
                    row[i] = math.log(row[i])
                except: 
                    row[i] = math.log(row[i]+0.01)
    	
        return table

    def widthBin(self, table, size = 5):        
        for colPos in range(len(table.cols)-1):
            allValues = [row[colPos] for row in table.rows]
            maxValue = max(allValues)
            minValue = min(allValues)
            
            binWidth = (maxValue - minValue)/size
            bins = [minValue + binWidth * i for i in range(size)]

            allValues = numpy.digitize(allValues, bins)

            for i, actual_value in enumerate(allValues):
                table.rows[i][colPos] =  actual_value 
        return table

    def freqBin(self, table, size = 5):
        numOfInstances = len(table.rows)
        
        for colPos in range(len(table.cols)-1):
            allValues = {} 
            for i, row in enumerate(table.rows):
                allValues[i] = row[colPos]

            sortedIndex = sorted(allValues, key=allValues.__getitem__)
            
            for i, index in enumerate(sortedIndex):
                table.rows[index-1][colPos] = math.floor(i/math.ceil(numOfInstances/float(size))) + 1
        
        return table

    def pca(self, table, n = 2):
        X = []
        Y = []
        for i, row in enumerate(table.rows):
            X.append(row[:-1])
            Y.append(row[-1])
        # X = [table.rows[row.rid -1][:-1] for row in table.rows]
        # Y = [table.rows[row.rid-1][-1] for row in table.rows]
            
        pca = PCA(n_components = n)
        pca.fit(X)
        result = pca.transform(X)

        newTable = tableReader.Table()
        for i,row in enumerate(result):
            row = numpy.append(row, Y[i])
            newTable.add_row(row)
        
        return newTable 




        