from sklearn import preprocessing
import tableReader

class preprocess:

	allValues = [] 

	def norm(table):
		normValue = float(actual_value - min(allValues))/(max(max(allValues) - min(allValues)),1) 
		
	def width5bin(table):
		minVal = min(allValues)

		interval = float(max(allValues) - minVal) / 5
		bins = []
		for i in range(5):
			bins.append(minVal + interval*i )

		print numpy.digitize(allValues, bins)