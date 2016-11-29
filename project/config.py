#Cross-validation
#For leave-one-out crossvalidation, put crossval.n='LOOCV'

# crossval_m = 5
# #crossval_n='LOOCV'
# crossval_n = 5

#Solos
solos = ['norm cartNo','none cartNo', 'log cartNo', 'log abe0_1NN']

#Datasets. Give a comma-separated paths to the datasets for which the learners are to be run
# base_dir = '/home/vivek/Desktop/fss/fss16c/project/code/effort_estimators'
datasets= [ "../ninja/data/cocomo81.arff"]

#Output files
error_metrics = "/output/errors"
skott_knott = "/output/sk"

display_output = True