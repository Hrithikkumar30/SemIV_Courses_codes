getwd()
dataset<-read.csv("D:/CDAC/Day 2/ANOVA/Medication.csv")
dataset
attach(dataset)

painrating<-c(A,B,C)

types<-c(rep("A",9),rep("B", 9),rep("C",9))
types
bodypainrating<-data.frame(painrating, types)
bodypainrating
bodypainrating<-write.csv(bodypainrating, file="D:/CDAC/Day 2/ANOVA/bodypainrating.csv")

plot<-boxplot(painrating~types, data=bodypainrating)

plot

fit<-aov(painrating~types, data=bodypainrating)
summary(fit)

