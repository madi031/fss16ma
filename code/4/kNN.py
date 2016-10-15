import sys, tableReader

class kNN:
    def oneNN(self, training_table, test_table): 
        for r in test_table: 
            print "Row : ", r
            nearest_neighbor = training_table.find_nearest(r)
            print "Nearest neighbor : ", nearest_neighbor
            print "Predicted class : ", nearest_neighbor[-1]
            
if __name__ == "__main__" : 
    training_table = tableReader.TableReader(sys.argv[1])
    test_table = tableReader.TableReader(sys.argv[2])
    k = kNN()
    k.oneNN(training_table, test_table)