from __future__ import division
import copy, tableReader, sys

class NaiveBayes: 
    def __init__(self,data):
        self.k = 1 
        self.m =2 
        
        self.table = data 
        self.tables = {} 
        
        for row in self.table.rows :
            row_class = row[-1]
            existing_table = self.tables.get(row_class, tableReader.clone(self.table))
            existing_table.add_row(row.contents)
            self.tables[row_class] = existing_table
        
    def predict(self,row):
        all = len(self.table.rows);
        guess, best, nh, k = None, -1*10**32, len(self.tables), self.k
        
        vals = {}
        for this, table in self.tables.items():
            like  = prior = (len(table.rows)  + k) / (all + k * nh)
            for col in table.cols[:-1]:
                if col.col:
                    x = row[col.pos]
                    if x != tableReader.Column.UNKNOWN:
                        like *= col.col.like( x, prior) # mult together all the likes
            vals[this] = like
            if like > best:
                guess, best = this, like
        return (row[-1], guess)
    

def learner(train_table, test_table):
    naive = NaiveBayes(train_table)
    results = [naive.predict(row) for row in test_table.rows]
    return results
        