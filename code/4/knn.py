import sys, tableReader, collections, math
import random
from time import time
import num

class KNN :
    def __init__(self, table, k) :
        self.table = table
        self.k = k

    def knn(self, row) :
        distances = [(self.table.row_distance(row, data), data[-1]) for data in self.table.rows]
        distances = sorted(distances, key = lambda x : x[0])
        classCounts = {}
        max_class = None
        for cl in distances[ : self.k] :
            cl = cl[1]
            if max_class is None:
                max_class = cl
            count = classCounts.get(cl, 0)
            classCounts[cl] = count = count + 1
            if classCounts[max_class] < count :
                max_class = cl
        return row[-1], max_class

    def train(self):
        pass

    def predict(self, row) :
        return self.knn(row)

class KNNKMeans :
    def __init__(self, table, batch_size, n, k):
        self.clusters = None
        self.table = table
        self.batch_size = batch_size
        self.iterations = len(self.table.rows) // self.batch_size
        self.k = k
        self.number_of_clusters = n
        self.cluster_contents = {}

    def train(self):
        self.kmeans()

    def kmeans(self) :
        if self.clusters is None:
            self.clusters = tableReader.Table()
            c = random.sample(self.table.rows, self.number_of_clusters)
            for i, con in enumerate(c):
                r = self.clusters.add_row(con.contents)
                self.cluster_contents[r] = (i, tableReader.Table())
                self.cluster_contents[r][1].add_row(con.contents)

        for h in xrange(self.iterations):
            batch_start = h * self.batch_size
            batch_end = batch_start + self.batch_size
            batch_end = len(self.table.rows) if batch_end > len(self.table.rows) else batch_end

            batch = self.table.rows[batch_start : batch_end]
            closest_centroid = {}
            for row in batch:
                close = self.clusters.find_nearest(row)
                closest_centroid[row.rid] = close

            for row in batch:
                center = closest_centroid[row.rid]
                self.cluster_contents[center.rid][1].add_row(row)

                learning_rate = 1 / len(self.cluster_contents[center.rid][1].rows)
                centroid = center.contents

                new_center = center[:]
                for col in self.table.cols :
                    if col.col.__class__ == num.Num :
                        new_center[col.pos] = (1 - learning_rate) * centroid[col.pos] + learning_rate * row[col.pos]
                    else :
                        new_center[col.pos] = col.col.mode

                cluster_index = self.cluster_contents[center.rid][0]
                self.clusters.rows[cluster_index][:] = new_center

    def predict(self, row) :
        nearest_cluster = self.clusters.find_nearest(row)
        innerKNN = KNN(self.cluster_contents[nearest_cluster.rid][1], self.k)
        return innerKNN.predict(row)

class KDTree :
    def __init__(self, table, k, m):
        self.table = table
        self.k = min(len(self.table.cols) - 1, k)
        self.m = m                     # Minimum number of examples required to split the node
        self.root = None
        self.Node = collections.namedtuple("Node", 'point axis left right')

    def train(self) :
        self.root = self.kdtree(0, len(self.table.rows))

    def kdtree(self, start, end, axis = 0) :
        if (end - start <= self.m):
            return None
        if axis >= self.k:
            return None;

        temp_rows = self.table.rows[start:end]
        sorted(temp_rows, key = lambda x: x[axis])
        self.table.rows[start:end] = temp_rows

        median = len(temp_rows) // 2
        median_point = self.table.rows[start + median]
        return self.Node( median_point, axis, self.kdtree(start, median, axis + 1), self.kdtree(median + 1, end, axis + 1))


    def predict(self, row) :
        best = [None, float('inf')]

        def recursive_search(here):
            if here is None:
                return
            point, axis, left, right = here

            here_sd = self.table.row_distance(point, row) ** 2
            if here_sd < best[1]:
                best[:] = point, here_sd
            diff = self.table.cols[axis].dist(row[axis], point[axis])
            close, away = (left, right) if diff <= 0 else (right, left)

            recursive_search(close)
            if diff ** 2 < best[1]:
                recursive_search(away)

        recursive_search(self.root)
        return row[-1], best[0][-1]

'''
python <training dataset> <testing dataset> <optimization>
'''
def learners(training_table, testing_table, optimization_func):
    # optimization_func = None
    learner = None
    if optimization_func == "KMeans":
        learner = KNNKMeans(training_table, 100, 20, 1)
    elif optimization_func == "KDTree":
        learner = KDTree(training_table, 10, 2)
    else:
        learner = KNN(training_table, 1)
    learner.train()

    return [learner.predict(row) for row in testing_table.rows]
