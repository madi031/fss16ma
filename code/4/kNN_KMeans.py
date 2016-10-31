import sys, kNN, Table, random, Num

class kNN_KMeans:
    
    def __init__(self, training_table, batch_size, k = 1, cluster_count = 5):
        self.cluster = None
        self.cluster_count = cluster_count
        self.k = k
        self.table = training_table
        self.batch_size = batch_size
        self.iterations = len(self.table.rows) // self.batch_size
        self.cluster_contents = {} 
        
    def train(self): 
        self.kMeans()
        
    def kMeans(self):
        if self.cluster is None: 
            self.cluster = Table.table()
            randomContent = random.sample(self.table.rows,self.cluster_count)
            for i, con in enumerate(randomContent):
                row = self.cluster.addRow(con.contents)
                self.cluster_contents[row] = (i, Table.table())
                self.cluster_contents[row][1].addRow(con.contents)
        
        for h in xrange(self.iterations):
            batch_start = h*self.batch_size
            batch_end = batch_start + self.batch_size
            batch_end = len(self.table.rows) if batch_end > len(self.table.rows) else batch_end
            
            batch = self.table.rows[batch_start : batch_end]
            closestCentroid = {}
            for i in batch: 
                nearestNeighbor = self.cluster.find_nearest(i)
                closestCentroid[i.rid] = nearestNeighbor
                 
            for row in batch:
                center = closestCentroid[row.rid]
                self.cluster_contents[center.rid][1].addRow(row)
                
                center_learning_rate = 1/len(self.cluster_contents[center.rid][1].rows)
                centroid = center.contents
                
                new_center = center[:]
                for col in self.table.cols :
                    if col.col.__class__ == Num.Num :
                        new_center[col.pos] = (1 - center_learning_rate) * centroid[col.pos] + center_learning_rate * row[col.pos]
                    else :
                        new_center[col.pos] = col.col.mode
                cluster_index = self.cluster_contents[center.rid][0]
                self.cluster.rows[cluster_index][:] = new_center
                
    def predict(self, row) :
        nearest_cluster = self.cluster.find_nearest(row)
        innerKNN = kNN.kNN(self.cluster_contents[nearest_cluster.rid][1], self.k)
        return innerKNN.predict(row)