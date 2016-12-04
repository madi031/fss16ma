from __future__ import division
import math, numpy, tableReader, crossValidation

def max(x,y) : return x if x>y else y
def min(x,y) : return x if x<y else y

class Num:
  def __init__(i):
    i.mu,i.n,i.m2,i.up,i.lo = 0,0,0,-10e32,10e32

  def is_number(s):
    try:
      float(s)
    except:
      return False
    else:
      return True
    
  def add(i,x):
    i.n += 1
    x = float(x)
    if x > i.up: i.up=x
    if x < i.lo: i.lo=x
    delta = x - i.mu
    i.mu += delta/i.n
    i.m2 += delta*(x - i.mu)
    return x 
    
  def sub(i,x):
    i.n   = max(0,i.n - 1)
    delta = x - i.mu
    i.mu  = max(0,i.mu - delta/i.n)
    i.m2  = max(0,i.m2 - delta*(x - i.mu))
    
  def sd(i):
    return 0 if i.n <= 2 else (i.m2/(i.n - 1))**0.5
    
  def show(i):
    print "Mean: " + str(i.mu) + "\tStandard deviation: " + str(i.sd())
    
  def norm(i,x):
    tmp= (x - i.lo) / (i.up - i.lo + 10**-32)
    if tmp > 1: return 1
    elif tmp < 0: return 0
    else: return tmp
    
  def dist(i,x,y):
    return i.norm(x) - i.norm(y)
    
  def furthest(i,x) :
    return i.up if x <(i.up-i.lo)/2 else i.lo

  def like(i,x,*_):
        var   = i.sd()**2
        result = 1 if x == i.mu else 0.001
        if var != 0:
            denom = (2*math.pi*var)**.5
            num   = math.exp(-(x-i.mu)**2/(2*var))
            result = num / denom
            result = result if result < 1 else 1
        return result if result > 0 else 10**-32

  def equalWidthBin(table):        
  for colPos in range(len(table.cols)-1):
    allValues = [row[colPos] for row in table.rows]
    maxValue = __builtins__.max(allValues)
    minValue = __builtins__.min(allValues)

    binWidth = (maxValue - minValue)/5
    bins = [minValue + binWidth * i for i in range(10)]

    allValues = numpy.digitize(allValues, bins)

    for i, actual_value in enumerate(allValues):
      table.rows[i][colPos] =  actual_value 
  return bins, table

  def equalWidthTestBin(bins, table):
    for colPos in range(len(table.cols)-1):
      allValues = [row[colPos] for row in table.rows]
      allValues = numpy.digitize(allValues, bins)

      for i, actual_value in enumerate(allValues):
        table.rows[i][colPos] = actual_value
    return table

  def updateBinMaps(binMaps, binId, val):
  if binId not in binMaps:
    binMaps[binId] = (float('inf'), float('-inf'))
  if val < binMaps[binId][0]:
    val1 = binMaps[binId][1]
    binMaps[binId] = (val, val1)
  if val > binMaps[binId][1]:
    val1 = binMaps[binId][0]
    binMaps[binId] = (val1, val)
  return binMaps

def updateEdgeBins(binMaps):
  for key, value in binMaps.items():
    if value[0] == float('inf'):
      val = value[1]
      value = (float('-inf'), val)
    if value[1] == float('-inf'):
      val = value[0]
      value[1] = (val, float('inf'))

def equalFreqBin(table):
  numOfInstances = len(table.rows)
  binMaps = {}
  for colPos in range(len(table.cols)-1):
    allValues = {} 
    for i, row in enumerate(table.rows):
      allValues[i] = row[colPos]

      sortedIndex = sorted(allValues, key=allValues.__getitem__)

    for i, index in enumerate(sortedIndex):
      binId = math.floor(i/math.ceil(numOfInstances/10.0)) + 1
      binMaps = updateBinMaps(binMaps, binId, table.rows[index-1][colPos])
      table.rows[index-1][colPos] = binId
  updateEdgeBins(binMaps)
  return binMaps, table

def findBin(binMaps, val):
  for key, value in binMaps.items():
    if val >= value[0] and val <= value[1]:
      return key

def equalFreqTestBin(binMaps, table):
  allValues = {}
  for colPos in range(len(table.cols)-1):
    for i, row in enumerate(table.rows):
      allValues[i] = row[colPos]
      sortedIndex = sorted(allValues, key=allValues.__getitem__)
    for i, index in enumerate(sortedIndex):
      table.rows[index-1][colPos] = findBin(binMaps, table.rows[index-1][colPos])
  return table

if __name__ == "__main__":
    table = tableReader.Table('segment.arff')
    n = Num()
    newTable = n.equalWidthBin(table)

