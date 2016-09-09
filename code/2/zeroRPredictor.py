import sys

class ZeroRPredictor:
    def __init__(self, filename) :
        self.count = {}
        self.classNumber = {}
        self.train(filename)
    
    def train(self, filename) :
        self.prediction = None
        count = -1
        keyCount = 1
        file = open(filename)
        startData = False
        for record in file :
            record = record.strip()
            if record == None or record == "" :
                continue
            if startData == True :
                classCount = record.split(",")[-1]
                currentCount = self.count.get(classCount, 0)
                self.count[classCount] = currentCount + 1
                for key in self.count :
                    self.classNumber[key] = keyCount
                    keyCount += keyCount
                keyCount = 1
                if self.count[classCount] > count :
                    count = self.count[classCount]
                    self.prediction = classCount
            if record.lower() == "@data" :
                startData = True
            
    def predict(self, data) :
        predictions = []
        file = open(data)
        startData = False
        for record in file :
            record = record.strip()
            if record == None or record == "" :
                continue
            if startData == True :
                predictions.append((record.split(",")[-1], self.prediction))
            if record.lower() == "@data" :
                startData = True
        return predictions
        
    def display(self, predictions) :
        print "\n=== Predictions on test data ===\n"
        print "inst#    actual  predicted   error   prediction\n"
        index = 1
        for key in predictions :
            actual = str(self.classNumber[key[0]]) + ":" + key[0]
            predicted = str(self.classNumber[key[1]]) + ":" + key[1]
            prediction = (key[0] == key[1])
            print ("{: >6.0f}".format(index) + "{:>11}".format(actual) + "{:>11}".format(predicted) + "{:>8.0f}".format(prediction))
            index += 1
            
if __name__ == '__main__' :
    model = ZeroRPredictor(sys.argv[1])
    predictions = model.predict(sys.argv[2])
    model.display(predictions)