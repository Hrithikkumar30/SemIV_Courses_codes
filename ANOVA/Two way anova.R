
###############################################################
#                                                             #
#                          TWo way ANOVA                      #
#                                                             #
###############################################################
#                                                             #
# Credit: Dr.Keerti Jain                                      #
# Email : keerti2401@gmail.com                                #
#                                                             #
#                                                             #

#--------------------------------------------------------------
# Step 0: Get or Set Directory
#--------------------------------------------------------------
cat("\nStep 0: Get Directory")
getwd()

#--------------------------------------------------------------
# Step 1: Variable Declaration
#--------------------------------------------------------------
cat("\nStep 1: Variable Declaration")
modelName <- "Two Way ANOVA"
modelName


#--------------------------------------------------------------
# Step 3: Data Loading
#--------------------------------------------------------------
cat("\nStep 3: Data Loading")
dataset <- read.csv("F:/Workshop(Data Analytics)/ANOVA/Insects.csv")      # Read the datafile
dataset 

head(dataset)   # Show Top 6 records
nrow(dataset)   # Show number of records
names(dataset)  # Show fields names or columns names



#--------------------------------------------------------------
# Step 4: Count total number of observations/rows.
#--------------------------------------------------------------
cat("\nStep 4: Counting dataset")
totalDataset <- nrow(dataset)
totalDataset



#--------------------------------------------------------------
# Step 5: Choose Target variable
#--------------------------------------------------------------
cat("\nStep 5: Choose Target Variable")
target  <- names(dataset)[1]  # i.e count
target



#--------------------------------------------------------------
# Step 6: Choose Input Variable
#--------------------------------------------------------------
cat("\nStep 6: Choose Input Variable")
inputs <- setdiff(names(dataset),target)
inputs
length(inputs)



#--------------------------------------------------------------
# Step 7: Applying ANOVA
#--------------------------------------------------------------

cat("\nStep 7: Applying ANOVA")
summary(dataset)

Model_1 <-aov(Count~Spray+type, data=dataset)

summary(Model_1)

Model_2<-aov(Count~Spray+type+Spray:type, data=dataset)
summary(Model_2)


#--------------------------------------------------------------
#                           END 
#--------------------------------------------------------------
