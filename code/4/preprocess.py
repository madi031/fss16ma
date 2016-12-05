import numpy, tableReader

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
