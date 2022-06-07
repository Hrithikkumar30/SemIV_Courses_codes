setwd("H:/Semester4/Statistic/ANOVA")

dataset <- read.csv("H:/Semester4/Statistic/ANOVA/Insects Spray")

View(dataset)

head(dataset.3)
nrow(dataset)
names(dataset)


attach(dataset)

fit <- aov(count~Spray , data = dataset)

summary(fit)


