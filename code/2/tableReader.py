import sys, num, sym, csvReader

class TableReader :
    def __init__(self, filename) :
        self.headers = []
        self.rows = []
        self.cols = []
        fileType = filename.split(".")[-1]
        if fileType == "csv" :
            self.rowsGenerator = csvReader.csv(filename)
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
            
if __name__ == "__main__" :
    table = TableReader(sys.argv[1])
    table.showStats()