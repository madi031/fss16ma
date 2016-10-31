import sys, Table, collections

class KDTree :
    def __init__(self, t, k,m):
        self.table = t    
        self.root = None
        self.m = m
        self.k = min(len(self.table.cols)-1, k)
        self.node = collections.namedtuple("Node", 'point axis left right')
    
    
    def kdTree(self, start, end, axis = 0) :
        if (end - start <= self.m) or axis >= self.k :
            return None
            
        temp_rows = self.table.rows[start : end]
        sorted(temp_rows, key = lambda x : x[axis])
        self.table.rows[start : end] = temp_rows
        
        median = len(temp_rows) //2 
        median_point = self.table.rows[start + len(temp_rows)//2]
        return self.node(median, axis, self.kdTree(start, median, axis + 1), self.kdTree(median+1, end, axis + 1))
        
    def kdTree_predict(self, row) :
        best = [None, float('Inf')]
        
        def recursive_search(here):
            if here is None :
                return
            point, axis, left, right = here
        
            here_sd = self.table.row_distance(point, row) **2 
            if here_sd < best[1] :
                best[:] = point, here_sd
            
            diff = self.table.cols[axis].dist(row[axis], point[axis])
            close, away = (left, right) if diff <= 0 else (right, left)
        
            recursive_search(close)
            if diff ** 2 < best[1] :
                recursive_search(away)
                
        recursive_search(self.root)
        return (row[-1], best[0][-1])
        