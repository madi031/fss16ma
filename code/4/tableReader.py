import sys, num, sym, csvReader, math, arffReader

class TableReader :
    def __init__(self, filename) :
        self.headers = []
        self.rows = []
        self.cols = []
        fileType = filename.split(".")[-1]
        if fileType == "csv" :
            self.rowsGenerator = csvReader.csv(filename)
        if fileType == "arff":
            self.rowsGenerator = arffReader.read(filename)
        self.generateTable()
        
    def generateTable(self) :
        self.headers = self.rowsGenerator.next()
        self.rows.append(self.rowsGenerator.next())
        index = 0
        for row in self.rows[0] :
            if type(row) is (int or float) :
                self.cols.append(num.Num())
                self.cols[index].add(row)
            else :
                self.cols.append(sym.Sym())
                self.cols[index].add(row)
            index += 1
            
        for row in self.rowsGenerator :
            self.rows.append(row)
            index = 0
            for record in row :
                self.cols[index].add(record)
                index += 1
                
    def showStats(self) :
        index = 0
        for record in self.cols:
            print self.headers[index]
            index += 1
            record.show()
            
    def row_distance(self, row1, row2) :
        distance = 0
        index = 0
        for index in xrange(len(self.cols) - 1):
            col = self.cols[index]
            distance += (col.dist(row1[index], row2[index]))
        return math.sqrt(distance)
        
    def find_nearest(self, row) :
        nearest = None
        distance = sys.maxint
        for r in self.rows:
            if r != row:
                current_distance = self.row_distance(row, r)
                if distance >= current_distance:
                    nearest = r
                    distance = current_distance
        return nearest
        
    def find_furthest(self, row) :
        furthest = None
        distance = -sys.maxint - 1
        for r in self.rows:
            if r != row:
                current_distance = self.row_distance(row, r)
                if distance <= current_distance:
                    furthest = r
                    distance = current_distance
        return furthest
        
if __name__ == "__main__" :
    table = TableReader(sys.argv[1])
    print table.rows[0]
    print "Closest : ",table.find_nearest(table.rows[0])
    print "Furthest : ",table.find_furthest(table.rows[0])
    print ""
    print table.rows[1]
    print "Closest : ",table.find_nearest(table.rows[1])
    print "Furthest : ",table.find_furthest(table.rows[1])