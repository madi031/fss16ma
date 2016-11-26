import sys, math, collections
import num, sym, csvReader, arffReader, preprocess, learners, errorMeasurement, crossValidation
import numpy, random


class Row :
    rid = 0
    def __init__(self, values):
        self.rid = Row.rid = Row.rid + 1
        self.contents = values

    def __repr__(self):
        return '#%s,%s' % (self.rid, self.contents)

    def __getitem__(self, key):
        return self.contents[key]

    def __setitem__(self, key, value):
        self.contents[key] = value

    def __len__(self):
        return len(self.contents)

    def __hash__(self):
        return self.rid

    def __eq__(self, other):
        return self.rid == other.rid

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return str(self.contents)

class Column:
    UNKNOWN = "?"
    def __init__(self, index, name):
        self.name = name or index
        self.name = str(self.name)
        self.col = None
        self.pos = index

    def add(self, val) :
        if val != Column.UNKNOWN:
            if self.col is None:
                val, valtype = self.what(val)
                self.col = valtype()
            self.col.add(val)

    def what(self, val):
        try: return float(val), num.Num
        except ValueError: return val, sym.Sym 

    def dist(self, row1, row2):
        return self.col.dist(row1, row2)

class Table :
    def __init__(self, fileName=None):
        self.rows = []
        self.cols = []
        self.current_row = -1;
        if fileName is not None:
            self.fileToTable(fileName)

    def fileToTable(self, fileName):
        filetype = fileName.split(".")[-1]
        if filetype == "arff" :
            self.rowsGenerator = arffReader.arffReader(fileName).read()
        # elif filetype == "csv" :
        #     self.rowsGenerator = CSVReader.CSVReader(fileName).read()
        self.generateTable()

    def next_row(self):
        self.current_row += 1
        if self.current_row >= len(self.rows):
            self.current_row = 0
        return self.rows[self.current_row]

    def add_row(self, row) :
        if len(self.cols) == 0:
            for index, val in enumerate(row) :
                col = Column(index, None)
                col.add(val)
                self.cols += [col]
            row = Row(row)
            self.rows += [row]
            return row.rid
        else :
            row = Row(row)
            self.rows += [row]
            for i, val in enumerate(row) :
                self.cols[i].add(val)
            return row.rid


    def generateTable(self):
        headers = self.rowsGenerator.next()
        for i, val in enumerate(headers) :
            col = Column(i, val)
            self.cols += [ col ]
            
        for row in self.rowsGenerator :
            self.add_row(row)

    def showStats(self) :
        for col in self.cols :
            print col.name
            col.col.show()

    def row_distance(self, row1, row2) :
        distance = 0
        for col in self.cols[:-1]:
            distance += (col.col.dist(row1[col.pos], row2[col.pos]) ** 2)
        return math.sqrt(distance)

    def find_nearest(self, row) :
        nearest = None
        distance = sys.maxint
        for r in self.rows:
            if r.rid != row.rid:
                current_distance = self.row_distance(row, r)
                if distance >= current_distance:
                    nearest = r
                    distance = current_distance
        return nearest
        
    def find_furthest(self, row) :
        furthest = None
        distance = -sys.maxint - 1
        for r in self.rows:
            if r.rid != row.rid:
                current_distance = self.row_distance(row, r)
                if distance <= current_distance:
                    furthest = r
                    distance = current_distance
        return furthest

def clone(table):
    newTable = Table()
    for col in table.cols:
        c = Column(col.pos, col.name)
        newTable.cols += [c]
    return newTable



if __name__ == "__main__":
    table = Table(sys.argv[1])
    #print table.showStats()
    if len(sys.argv) > 3:
        solo_preprocess = sys.argv[2]
        solo_learner = sys.argv[3]
    # else:
    #     solo_preprocess = "none"
    #     solo_learner = "abe0_1NN"
        
    table = preprocess.preprocess().missingValue(table)
    
    if solo_preprocess == "norm":
        newTable = preprocess.preprocess().norm(table) 
    elif solo_preprocess == "pca": 
        newTable = preprocess.preprocess().pca(table, len(table.cols)-1)
    elif solo_preprocess == "freq5bin":
        newTable = preprocess.preprocess().freq5bin(table)
    elif solo_preprocess == "log":
        newTable = preprocess.preprocess().logarithm(table)
    elif solo_preprocess == "width5bin":
        newTable = preprocess.preprocess().width5bin(table)
    else:
        newTable = table

    if solo_learner == "pcr":
        newTable = preprocess.preprocess().pca(newTable)

    crossValidation.crossValidation().cv(newTable, solo_learner)            
#     for row in table.rows:
#         print row