import stats
def generateScottKnott(data_fileName):
    data = open(data_fileName)
    sk_dict = {}
    for line in data :
        if len(line) > 0 :
            solo, error = line.split(",")
            v = sk_dict.get(solo, [])
            v.append(float(error))
            sk_dict[solo] = v
    
    stats.rdivDemo([ [k] + v for k,v in sk_dict.items() ])