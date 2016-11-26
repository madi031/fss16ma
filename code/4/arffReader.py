import re
class arffReader:
    def __init__(self, fileName):
        self.fileName = fileName
    
    def rows(self, prep       = None,
              whitespace = '[\n\r\t]',
              comments   = '#.*',
              sep        = ","
              ):
        """
        Walk down comma seperated values, 
        skipping bad white space and blank lines
        """
        doomed = re.compile('(' + whitespace + '|' +  comments + ')')
        with open(self.fileName) as fs:
            for line in fs:
                line = re.sub(doomed, "", line)
                if line:
                    row = map(lambda z:z.strip(), line.split(sep))
                    if len(row)> 0:
                        yield prep(row) if prep else row

    def read(self):
        """
        Convert rows of strings to ints,floats, or strings
        as appropriate
        """
        def atoms(lst):
            return map(atom,lst)
        def atom(x)  :
            try: return int(x)
            except:
                try: return float(x)
                except ValueError: return x
        
        rowsGenerator = self.rows(prep = atoms)
        header = []
        for row in rowsGenerator:
            if "@data" in row[0].lower():
                break
            elif "@attribute" in row[0].lower():
                attr = row[0].split(" ")[1]
                header.append(attr)
        yield header
        
        for row in rowsGenerator:
            yield row