import re

def rows(file,prep       = None,
              whitespace = '[\n\r\t]',
              comments   = '#.*',
              sep        = ","
              ):
    doomed = re.compile('(' + whitespace + '|' +  comments + ')')
    with open(file) as fs:
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
    headers = []
    
    for row in rows(file, prep = atoms):
        if(re.match('@ATTRIBUTE', row, flags=0)):
            headers.append(row.split()[1])
        yield headers
	
	for row in rows(file, prep=atoms):
	    yield row