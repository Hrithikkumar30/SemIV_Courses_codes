getwd()

dataset <- read.csv("H:/Semester4/Statistic/ANOVA/Insects Spray.csv")      # Read the data file

View(dataset) 

head(dataset,3)   # Show Top 6 records
nrow(dataset)   # Show number of records
names(dataset)  # Show fields names or columns names

attach(dataset)

#### H0: There is no significant different in the three types of sprays
#### H1: At least one of the spray is significantly different

fit <-aov(Count~Spray, data=dataset)

summary(fit)

posthoc<-TukeyHSD(fit,conf.level = 0.95)
posthoc

###############################################################
#                                                             #
#                          Two way ANOVA                      #
#                                                             #
###############################################################
modelName <- #"Two Way ANOVA"
modelName

getwd()
dataset <- read.csv("E:/D/CDAC/ANOVA/Insects1.csv")      # Read the datafile
dim(dataset)
View(dataset) 
class(dataset)
sapply(dataset, class)
head(dataset,3)   # Show Top 6 records
nrow(dataset)   # Show number of records
names(dataset)  # Show fields names or columns names




summary(dataset)

#### Without Interaction#######

Model_1 <-aov(Count~Spray+type, data=dataset)


summary(Model_1)

posthoc<-TukeyHSD(Model_1)
posthoc

#### With interaction ####

Model_2<-aov(Count~Spray+type+Spray:type, data=dataset)

summary(Model_2)

posthoc<-TukeyHSD(Model_2)
posthoc



