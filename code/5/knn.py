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

def learners(training_table, testing_table):
    learner = KNN(training_table, 1)
    learner.train()

    return [learner.predict(row) for row in testing_table.rows]
