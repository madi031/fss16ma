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

            binWidth = (maxValue - minValue)/5

            bins = []
            for i in range(5):
                bins.append(minValue + binWidth*i )

            allValues = numpy.digitize(allValues, bins)

            for i, actual_value in enumerate(allValues):
                table.rows[i][colPos] =  actual_value 
        return table

	def freq5bin(table):
		table.sort()
		result = []
		length = len(table)
		# for i in range(5):
		# 	temp = 