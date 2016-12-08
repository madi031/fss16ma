#Cross-validation
#For leave-one-out crossvalidation, put crossval_loocv = True
crossval_loocv=False
crossval_m = 5
crossval_n = 5

learners = ['cartNo', 'abe0_1NN', 'abe0_5NN', 'plsr','pcr','lReg']
preprocess = ['freq3bin','width3bin','norm', 'none','log','pca','width5bin','freq5bin']

#Datasets. Give a comma-separated paths to the datasets for which the learners are to be run

datasets= [ "data/desharnais.arff", "data/cocomo81.arff", "data/albrecht.arff", "data/china.arff", \
"data/kemerer.arff", "data/maxwell.arff","data/diabetes.arff", "data/ivy-1.1.arff", "data/miyazaki94.arff",\
"data/jedit-4.1.arff"]

# datasets = ["data/miyazaki94.arff",\
# "data/jedit-4.1.arff"]

