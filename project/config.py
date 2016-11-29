
#Cross-validation
#For leave-one-out crossvalidation, put crossval.n='LOOCV'

# crossval_m = 5
# #crossval_n='LOOCV'
# crossval_n = 5

#Solos

solos = [ 'norm cartNo','none cartNo', 'log cartNo', 'log abe0_1NN', 'pca plsr', \
'none plsr', 'pca pcr', 'none pcr', 'pca cartNo', 'norm abe0_1NN','none abe0_1NN',\
 'freq5bin cartNo','freq5bin abe0_5NN', 'width5bin cartNo', 'norm abe0_5NN', \
 'none abe0_5NN', 'log abe0_5NN', 'pca abe0_5NN', 'width5bin abe0_1NN',\
 'none lReg', 'norm plsr', 'width5bin abe0_5NN', 'norm lReg', 'freq5bin abe0_1NN', 'pca abe0_1NN']
# solos = ['none abe0_1NN', 'freq5bin cartNo']

#Datasets. Give a comma-separated paths to the datasets for which the learners are to be run

#working => 
datasets= [ "data/desharnais.arff", "cocomo81.arff", "data/albrecht.arff", "data/china.arff", "data/kemerer.arff", "data/maxwell.arff"]
# not working => datasets = ["data/miyazaki94.arff"]
