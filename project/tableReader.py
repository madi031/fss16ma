import sys, math, collections
import num, sym, csvReader, arffReader, preprocess, learners, errorMeasurement, crossValidation, config, report
import numpy, random, os
import shutil

class Row :
    rid = 0
    def __init__(self, values):
        self.rid = Row.rid = Row.rid + 1
        self.contents = values

    def __repr__(self):
        return '#%s,%s' % (self.rid, self.contents)

    def __getitem__(self, key):
        return self.contents[key]

    def __setitem__(self, key, value):
        self.contents[key] = value

    def __len__(self):
        return len(self.contents)

    def __hash__(self):
        return self.rid

    def __eq__(self, other):
        return self.rid == other.rid

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return str(self.contents)

class Column:
    UNKNOWN = "?"
    def __init__(self, index, name):
        self.name = name or index
        self.name = str(self.name)
        self.col = None
        self.pos = index

    def add(self, val) :
        if val != Column.UNKNOWN:
            if self.col is None:
                val, valtype = self.what(val)
                self.col = valtype()
            self.col.add(val)

    def what(self, val):
        try: return float(val), num.Num
        except ValueError: return val, sym.Sym 

    def dist(self, row1, row2):
        return self.col.dist(row1, row2)

class Table :
    def __init__(self, fileName=None):
        self.rows = []
        self.cols = []
        self.current_row = -1;
        if fileName is not None:
            self.fileToTable(fileName)

    def fileToTable(self, fileName):
        filetype = fileName.split(".")[-1]
        if filetype == "arff" :
            self.rowsGenerator = arffReader.arffReader(fileName).read()
        # elif filetype == "csv" :
        #     self.rowsGenerator = CSVReader.CSVReader(fileName).read()
        self.generateTable()

    def next_row(self):
        self.current_row += 1
        if self.current_row >= len(self.rows):
            self.current_row = 0
        return self.rows[self.current_row]

    def add_row(self, row) :
        if len(self.cols) == 0:
            for index, val in enumerate(row) :
                col = Column(index, None)
                col.add(val)
                self.cols += [col]
            row = Row(row)
            self.rows += [row]
            return row.rid
        else :
            row = Row(row)
            self.rows += [row]
            for i, val in enumerate(row) :
                self.cols[i].add(val)
            return row.rid


    def generateTable(self):
        headers = self.rowsGenerator.next()
        for i, val in enumerate(headers) :
            col = Column(i, val)
            self.cols += [ col ]
            
        for row in self.rowsGenerator :
            self.add_row(row)

    def showStats(self) :
        for col in self.cols :
            print col.name
            col.col.show()

    def row_distance(self, row1, row2) :
        distance = 0
        for col in self.cols[:-1]:
            distance += (col.col.dist(row1[col.pos], row2[col.pos]) ** 2)
        return math.sqrt(distance)

    def find_nearest(self, row) :
        nearest = None
        distance = sys.maxint
        for r in self.rows:
            if r.rid != row.rid:
                current_distance = self.row_distance(row, r)
                if distance >= current_distance:
                    nearest = r
                    distance = current_distance
        return nearest
        
    def find_furthest(self, row) :
        furthest = None
        distance = -sys.maxint - 1
        for r in self.rows:
            if r.rid != row.rid:
                current_distance = self.row_distance(row, r)
                if distance <= current_distance:
                    furthest = r
                    distance = current_distance
        return furthest

def clone(table):
    newTable = Table()
    for col in table.cols:
        c = Column(col.pos, col.name)
        newTable.cols += [c]
    return newTable



if __name__ == "__main__":
    # for dataset in config.datasets:
    #     table = Table(dataset)
    #     table = preprocess.preprocess().missingValue(table)
    #     result = preprocess.preprocess().freq5bin(table)
    #     for row in result.rows:
    #         print row
    directory = os.getcwd() + "/temp/"
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)

    mar_report = {} 
    mmre_report = {}
    mmer_report ={}
    mbre_report = {}
    mibre_report = {}
    mdmre_report = {}
    pred25_report = {}

    report_datasets = {}



    for dataset in config.datasets:
        print '-------' + dataset.split('/')[-1].split(".")[0] + '--------'

        dataset_name = dataset.split('/')[-1].split(".")[0]
        report_datasets[dataset_name] = {}

        for solo in config.solos:


            table = Table(dataset)
            solo_preprocess = solo.split(' ')[0]
            solo_learner = solo.split(' ')[1]

            print "solo:" + solo

            table = preprocess.preprocess().missingValue(table)
            
            if solo_preprocess == "norm":
                newTable = preprocess.preprocess().norm(table) 
            elif solo_preprocess == "pca": 
                newTable = preprocess.preprocess().pca(table, len(table.cols)-1)
            elif solo_preprocess == "freq5bin":
                newTable = preprocess.preprocess().freq5bin(table)
            elif solo_preprocess == "log":
                newTable = preprocess.preprocess().logarithm(table)
            elif solo_preprocess == "width5bin":
                newTable = preprocess.preprocess().width5bin(table)
            else:
                newTable = table

            if solo_learner == "pcr":
                newTable = preprocess.preprocess().pca(newTable)

            if config.crossval_loocv:
                errors = crossValidation.crossValidation().cv(newTable, solo_learner, m = 1, n= len(newTable.rows))
            else:
                errors = crossValidation.crossValidation().cv(newTable, solo_learner, m = config.crossval_m, n = config.crossval_n)

            

            crossValidation.crossValidation.error_metrics_to_file(directory + dataset_name, solo, errors)     

        
        print "MAR:"
        reportContent = report.generateScottKnott(directory + dataset_name + "_mar.txt")
        
        for line in reportContent : 
            if str(line[1]) in mar_report:
                mar_report[str(line[1])] = mar_report.get(str(line[1])) + int(line[0]) 
            else:
                mar_report[str(line[1])] = int(line[0])
            
            if str(line[1]) in report_datasets[dataset_name]:
                report_datasets[dataset_name][str(line[1])] = report_datasets[dataset_name][str(line[1])] + int(line[0])
            else:
                report_datasets[dataset_name][str(line[1])] = int(line[0])


        print "MMRE:"
        report.generateScottKnott(directory + dataset_name + "_mmre.txt")

        for line in reportContent : 
            if str(line[1]) in mmre_report:
                mmre_report[str(line[1])] = mmre_report.get(str(line[1])) + int(line[0]) 
            else:
                mmre_report[str(line[1])] = int(line[0])

            if str(line[1]) in report_datasets[dataset_name]:
                report_datasets[dataset_name][str(line[1])] = report_datasets[dataset_name][str(line[1])] + int(line[0])
            else:
                report_datasets[dataset_name][str(line[1])] = int(line[0])

        print "MDMRE:"
        report.generateScottKnott(directory + dataset_name + "_mdmre.txt")

        for line in reportContent : 
            if str(line[1]) in mdmre_report:
                mdmre_report[str(line[1])] = mdmre_report.get(str(line[1])) + int(line[0]) 
            else:
                mdmre_report[str(line[1])] = int(line[0])

            if str(line[1]) in report_datasets[dataset_name]:
                report_datasets[dataset_name][str(line[1])] = report_datasets[dataset_name][str(line[1])] + int(line[0])
            else:
                report_datasets[dataset_name][str(line[1])] = int(line[0])

        
        print "MMER:"
        report.generateScottKnott(directory + dataset_name + "_mmer.txt")

        for line in reportContent : 
            if str(line[1]) in mmer_report:
                mmer_report[str(line[1])] = mmer_report.get(str(line[1])) + int(line[0]) 
            else:
                mmer_report[str(line[1])] = int(line[0])

            if str(line[1]) in report_datasets[dataset_name]:
                report_datasets[dataset_name][str(line[1])] = report_datasets[dataset_name][str(line[1])] + int(line[0])
            else:
                report_datasets[dataset_name][str(line[1])] = int(line[0])

        
        print "MBRE:"
        report.generateScottKnott(directory + dataset_name + "_mbre.txt")

        for line in reportContent : 
            if str(line[1]) in mbre_report:
                mbre_report[str(line[1])] = mbre_report.get(str(line[1])) + int(line[0]) 
            else:
                mbre_report[str(line[1])] = int(line[0])

            if str(line[1]) in report_datasets[dataset_name]:
                report_datasets[dataset_name][str(line[1])] = report_datasets[dataset_name][str(line[1])] + int(line[0])
            else:
                report_datasets[dataset_name][str(line[1])] = int(line[0])


        
        print "MIBRE:"
        report.generateScottKnott(directory + dataset_name + "_mibre.txt")

        for line in reportContent : 
            if str(line[1]) in mibre_report:
                mibre_report[str(line[1])] = mibre_report.get(str(line[1])) + int(line[0]) 
            else:
                mibre_report[str(line[1])] = int(line[0])

            if str(line[1]) in report_datasets[dataset_name]:
                report_datasets[dataset_name][str(line[1])] = report_datasets[dataset_name][str(line[1])] + int(line[0])
            else:
                report_datasets[dataset_name][str(line[1])] = int(line[0])

        
        print "Pred25:"
        report.generateScottKnott(directory + dataset_name + "_pred25.txt")

        for line in reportContent : 
            if str(line[1]) in pred25_report:
                pred25_report[str(line[1])] = pred25_report.get(str(line[1])) + int(line[0]) 
            else:
                pred25_report[str(line[1])] = int(line[0])

            if str(line[1]) in report_datasets[dataset_name]:
                report_datasets[dataset_name][str(line[1])] = report_datasets[dataset_name][str(line[1])] + int(line[0])
            else:
                report_datasets[dataset_name][str(line[1])] = int(line[0])

    
    # print "********* MAR **********"  
    # sortedIndex = sorted(mar_report, key=mar_report.__getitem__)        
    # for i, index in enumerate(sortedIndex):
    #     print index, mar_report[index]
    
    # print "********* MMER **********" 
    # sortedIndex = sorted(mmer_report, key=mmer_report.__getitem__)        
    # for i, index in enumerate(sortedIndex):
    #     print index, mmer_report[index]

    # print "********* MDMRE **********"  
    # sortedIndex = sorted(mdmre_report, key=mdmre_report.__getitem__)        
    # for i, index in enumerate(sortedIndex):
    #     print index, mdmre_report[index]

    # print "********* MMRE **********"  
    # sortedIndex = sorted(mmre_report, key=mmre_report.__getitem__)        
    # for i, index in enumerate(sortedIndex):
    #     print index, mmre_report[index]

    # print "********* MBRE **********"  
    # sortedIndex = sorted(mbre_report, key=mbre_report.__getitem__)        
    # for i, index in enumerate(sortedIndex):
    #     print index, mbre_report[index]

    # print "********* MIBRE **********"  
    # sortedIndex = sorted(mibre_report, key=mibre_report.__getitem__)        
    # for i, index in enumerate(sortedIndex):
    #     print index, mibre_report[index]

    # print "********* PRED25 **********"  
    # sortedIndex = sorted(pred25_report, key=pred25_report.__getitem__)        
    # for i, index in enumerate(sortedIndex):
    #     print index, pred25_report[index]

    final_report = {}
    
    for i in report_datasets.keys():
    #    print "*********** dataset- " + i + " ******"
        sortedIndex = sorted(report_datasets[i], key=report_datasets[i].__getitem__)        
        for index in sortedIndex:
            #print index, report_datasets[i][index]
            if index in final_report:
                final_report[index] = final_report[index] + report_datasets[i][index]
            else:
                final_report[index] = report_datasets[i][index]

    print final_report
