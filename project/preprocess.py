from sklearn import preprocessing
import tableReader, math, numpy

class preprocess:
    def norm(self, table):
        for colPos in range(len(table.cols)-1):
	        allValues = [] 
	        for row in table.rows:
	            allValues.append(row[colPos])
	        maxValue = max(allValues)
	        minValue = min(allValues)
	        print minValue, maxValue

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

    # def pca(self, table):
    #     temp =[]
    # for i, row in enumerate(table.rows):
    #     temp.append(table.rows[row.rid-1])
        
    # print temp
    # X = numpy.array(temp)
    # pca = PCA(n_components = len(table.cols))
    # pca.fit(X)
    # print pca.explained_variance_ratio_

    # c = len(table.cols)
    # ipca = IncrementalPCA(n_components= c)
    # ipca.fit(X)
    # print ipca.transform(X)
