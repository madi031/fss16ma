import sys, Table

class kNN:
    def oneNN(self, training_table, test_table): 
        for r in test_table: 
            print "Row : ", r
            nearest_neighbor = training_table.find_nearest(r)
            print "Nearest neighbor : ", nearest_neighbor
            print "Predicted class : ", nearest_neighbor[-1]
            
    def predict(self, row): 
        return self.oneNN(training_table, row)
            
if __name__ == "__main__" : 
    training_table = Table.table(sys.argv[1])
    test_table = Table.table(sys.argv[2])
    k = kNN()
    k.oneNN(training_table, test_table)
    
