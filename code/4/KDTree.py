import sys, tableReader as table

class KDTree :
    node = collections.namedtuple("Node", 'point axis left right')
    def kdTree(self, start, end, k, axis = 0) :
        if start == end or axis >= k :
            return None
        temp_rows = table.rows[start : end]
        sorted(temp_rows, key = lambda x : x[axis])
        table.rows[start : end] = temp_rows
        median = table.rows[start + len(temp_rows)//2]
        return self.node(median, axis, self.kdTree(start, median, axis + 1), self.kdTree(median+1, end, axis + 1))
        
    def kdTree_predict(self, row) :
        best = [None, float('Inf)]
        
        def recursive_search(here):
            if here is None :
                return
            point, axis, left, right = here
        
            here_sd = self.table.row_distance(point, row)
            if here_sd < best[1] :
                best[:] = point, here_sd
            
            diff = self.table.cols[axis].dist(point[axis], row[axis])
            close, away = (left, right) if diff <= 0 else (right, left)
        
            recursive_search(close)
            if diff ** 2 < best[1] :
                recursive_search(away)
                
        recursive_search(self.root)
        return best[0][-1]
        