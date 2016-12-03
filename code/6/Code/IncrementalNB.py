import sys, tableReader, num, sym, NaiveBayes, DataGenerator
from random import randint
import math

class IncrementalNB:
	def __init__(self, data):
		self.table = data
		self.classes = []

	def getEras(self, testTable, erasSize):
		for i in range(erasSize):
			row = self.table.next_row()
			if row[-1] not in self.classes:
				self.classes.append(row[-1])
			testTable.add_row(row)
		return testTable

	def calculcateRecall(self, result):
		for actualClass in self.classes:
			b = 0.0
			d = 0.0
			for predict in result:
				actual = predict[0]
				predicted = predict[1]
				# print 'Expected = %s, \t Predicted = %s, \t Log of the likelihood = %.2f' % (str(actualClass), str(predicted), math.log(predict[2]))
				if actual == actualClass and predicted == actualClass:
					d = d + 1
					pd = d / (b + d)
				elif actual == actualClass:
					b = b + 1
					pd = d / (b + d)
			print 'Class = %s, recall %.2f' % (str(actualClass), pd)

	def mergeEras(self, era1, era2):
		for row in era2.rows:
			era1.add_row(row.contents)

	# Copied from stats.py
	def a12Test(self, list1, list2):
		more = same = 0.0
		for x in sorted(list1):
			for y in sorted(list2):
				if x == y:
					same += 1
				elif x > y:
					more += 1
		return (more + 0.5 * same) / (len(list1) * len(list2))

	def detectAnamoly(self, prevResults, results, prevScore):
		oldLikelihood = [math.log(x[2]) for x in prevResults]
		newLikelihood = [math.log(x[2]) for x in results]
		score = self.a12Test(oldLikelihood, newLikelihood)
		if score >= 0.71:
			print "Anamoly detected\n"
		return score

	def incrementalNB(self, table):
		a12Score = 0.0
		prevResults = None
		size = len(table.rows)
		noOfEras = size / 100
		trainTable = self.getEras(tableReader.Table(), 100)
		for i in range(noOfEras):
			nb = NaiveBayes.NaiveBayes(trainTable)
			testTable = self.getEras(tableReader.Table(), 100)
			results = nb.predictTable(testTable)
			print 'Era ' + str(i + 1)
			self.calculcateRecall(results)
			if prevResults is not None:
				a12Score = self.detectAnamoly(prevResults, results, a12Score)
			prevResults = results
			print '\n\n\n'
			self.mergeEras(trainTable, testTable)

if __name__ == "__main__":
	table = tableReader.Table(sys.argv[1])
	dg = DataGenerator.DataGenerator(table)
	data = dg.generateData()
	incNB = IncrementalNB(data)
	incNB.incrementalNB(table)