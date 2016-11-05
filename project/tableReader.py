from sklearn import preprocessing
import sys, num, sym, csvReader, math, arffReader

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
    def __init__(self, filename = None) :
        self.headers = []
        self.rows = []
        self.cols = []
        fileType = filename.split(".")[-1]
        if fileType == "csv" :
            self.rowsGenerator = csvReader.csv(filename)
        if fileType == "arff":
            self.rowsGenerator = arffReader.read(filename)
        self.generateTable()
    
    def addRow(self,row) :
        if len(self.cols) == 0:
            for index, val in enumerate(row):
                col = Column(index, None)
                col.add(val)
                self.rows += [row]
                return row.rid
        else:
            row = Row(row)
            self.rows +=[row]
            for i, val in enumerate(row):
                self.cols[i].add(val)
                return row.rid
        
    def generateTable(self) :
        self.headers = self.rowsGenerator.next()
        for index, val in enumerate(self.headers) :
            col = Column(index, val)
            self.cols += [ col ]
            
        for row in self.rowsGenerator :
            self.addRow(row)
                
    def showStats(self) :
        for record in self.cols:
            print record.name
            record.col.show()
            
    def row_distance(self, row1, row2) :
        distance = 0
        for index in self.cols[:-1]:
            distance += (index.col.dist(row1[index.pos], row2[index.pos])**2)
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
    newTable = table()
    for col in table.cols:
        c = Column(col.pos, col.name)
        newTable.cols += [c]
    return newTable    
    
if __name__ == "__main__" :
    table = Table(sys.argv[1])
    