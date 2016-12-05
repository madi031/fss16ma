import math
def max(x,y) : return x if x>y else y
def min(x,y) : return x if x<y else y

class Num:
  def __init__(i):
    i.mu,i.n,i.m2,i.up,i.lo = 0,0,0,-10e32,10e32
    
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
    
  def norm(i, x):
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