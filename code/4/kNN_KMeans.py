import sys, kNN, tableReader, random

class kNN_KMeans:
    
    def __init__(self, training_table, k = 1, cluster_count = 5):
        self.cluster = None
        C = randomGenerator(training_table, cluster_count)
        kMeans(training_table, test_table, 10, 20, k)
        
    def kMeans(self, training_table, test_table, iteration_t, b, k):
        M = []
        d = []
        nearestNeighbor = []
        center_counts = [1] * cluster_count
        for iterations in range(0,t):
            M = randomGenerator(training_table, k)
            for i in range(0, M.len): 
                nearestNeighbor[i] = C.find_nearest(M[i])
                d[i] = training_table.row_distance(M[i],C[nearestNeighbor[i]])
                 
            for i in range(0,M.len):
                center = d[i]
                center_counts[i] += 1
                center_learning_rate = float(1/center_counts[i])
                C[nearestNeighbor[i]] = (1 − center_learning_rate) * center + center_learning_rate * M[i]
        
    def randomGenerator(contentTable, count):
        randomContent = random.sample(range(0,len(contentTable)),count)
        C = []
        for i in randomContent:
            C.append(contentTable[i])
        return C
        
    def find_nearest(self, row) :
        nearest = None
        distance = sys.maxint
        rows = self.Row()
        
        for r in range(0, rows.len):
            if rows[r] != row:
                current_distance = self.row_distance(row, r)
                if distance >= current_distance:
                    nearestID = r
                    distance = current_distance
        return nearestID