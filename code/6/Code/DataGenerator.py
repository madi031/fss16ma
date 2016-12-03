import tableReader, sys
from random import randint

class DataGenerator:
	def __init__(self, data):
		self.table = data
		self.tables = {}
		self.segregateClassTables()
		self.k = 1
		self.outputData = tableReader.Table()

	def segregateClassTables(self) :
		for row in self.table.rows :
			currentClass = row[-1]
			if currentClass not in self.tables:
				classTable = tableReader.clone(self.table)
			else:
				classTable = self.tables.get(currentClass)
			classTable.add_row(row.contents)
			self.tables[currentClass] = classTable

	def getRandomClass(self, k):
		if self.k <= 1000:
			return randint(0, 1)
		else:
			r = randint(1, 10)
			if r == 1:
				return 0
			elif r < 5:
				return 1
			else:
				return 2

	def generateData(self):
		availableClass = self.tables.keys()
		for i in range(len(self.table.rows)):
			rClass = availableClass[self.getRandomClass(self.k)]
			self.outputData.add_row(self.tables[rClass].next_row().contents)
			self.k = self.k + 1
		return self.outputData

if __name__ == "__main__":
	table = tableReader.Table(sys.argv[1])
	dg = DataGenerator(table)
	data = dg.generateData()
	# output = {'path': 0, 'sky': 0, 'brickface': 0}
	# for i, row in enumerate(data.rows):
	# 	r = row.contents
	# 	if (i >= 1000):
	# 		break
	# 	if r[-1] == 'path':
	# 		output['path'] = output['path'] + 1
	# 	elif r[-1] == 'sky':
	# 		output['sky'] = output['sky'] + 1
	# 	elif r[-1] == 'brickface':
	# 		output['brickface'] = output['brickface'] + 1

	# print 'path = ' + str(output['path'])
	# print 'sky = ' + str(output['sky'])
	# print 'brickface = ' + str(output['brickface'])
