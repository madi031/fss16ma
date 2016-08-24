#Week1

##Run something

###eg0

eg0 prints the attributes of the datset. It prints the records with 5 attributes sorted in a lexicographical order with proper spacing. It also gives the decision tree of a para 3 for modelling using j4810 algorithm, which does a 10-fold cross validation.

###eg1

eg1 prints the weather dataset which has 5 fields, sorted in a lexicographical order and prints the column by replacing the comma with tab space.

###eg2

eg2 prints the output using j4810 algorithm, which does a 10-fold cross validaton on the dataset. The ouput has the line numbers, followed by the decision tree and the number of records associated with each leaf node. It then prints the number of leaf nodes and the total number of nodes. It is followed by the total time taken to run the algorithm and train the learner. It is followed by the confusion matrix at last with true positive rate, true negative rate, accuracy, etc. These data can be used to decide whether to do prune or not. It again does all these calculations for stratified cross validation too.

###eg3

eg3 runs the j48 algorithm to show the prediction of the test data using training data. The problem here is that it uses the same data as training and test data giving the false impression that the learner works good.

###eg4

eg4 prints the actual and predicted classes of the eg3 solution, which can be used in the future.

###eg5

eg5 uses the eg4 solution and calculates various metrics like true positive, true negative, false positive, and false negative. We can calculate various metrics like true positive rate, false positive rate, accuracy, recall, and precision. The learner shows the accuracy as 100% since we have used the same data for both training data and test data (Remember eg3).

###eg6

eg6 does a 1 x 3 cross validation and passes the dataset to j48 and jrip algorithms.For each algorithm, 3 fold cross validation is done and the output is processed to obtain the displayed metrics. Since the rows are chosen randomly to run each iteration, it uses stratified cross validation.

###eg7

eg7 runs the 5 x 5 cross validation with j48 and jrip algorithms and the store in the variable. Then the data is searched to identify the columns 2 and 10, and 2 and 11, to identify the pd and pf values.

###eg8

eg8 is similar to the eg7 except that eg8 uses column names instead of column indices, to identify the pd and pf values. A named column is a column in the table which can be used directly to filter out the necessary columns.

###eg9

eg9 uses the output of the eg8 and provides the visualization of the data for j48 and jrip algorithms. The output contains the representation of the median along 10, 30, 50, 70 and the 90th percentile, rank of the algorithm and interquartile range for each algorithm. The algorithms have same rank here, as the values are similar.

The data mining is a time consuming one and if we separate the data mining and report, we can do the data mining once and run the reports any number of times. This is the advantage of seperating the reporting of a data mining run from the execution of that run as we did in eg9.

###eg10

eg10 does 5 x 5 cross validation, including the new algorithms nb,rbfnet, and bnet in addition to the previous two algorithms.The report shows a ranked list of algorithms based on the pd and pf values, and median and interquartile values for each algorithm.

nb is a Naive Bayes algorithm. nb calculates the likelihood of each outcome for each possible values. The class is predicted to be the class having highest probability.

JRip proceeds by treating all the examples of a particular judgement in the training data as a class, and finding a set of rules that cover all the members of that class. It repeats for all the classes until all classes have covered.
