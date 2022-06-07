#a
#getwd()
dataset <- read.csv("H:/Semester4/Statistic/london_merged.csv")
View(dataset)





head(dataset)
tail(dataset)
attach(dataset)
sd(dataset$weather)
dataset$weather<- as.factor(dataset$weather)
summary(dataset)
mean(dataset$wind_speed)
mean(dataset$T1)
mean(dataset$T2)
mean(dataset$hum)
median(dataset$T2)
median(dataset$T1)
median(dataset$hum)
median(dataset$wind_speed)
median(dataset$weather)
median(dataset$season)
mode(dataset$season)
mode(dataset$T2)


#b)
boxplot(dataset$wind_speed)
boxplot(dataset$hum)

#c)
barplot(dataset$weather)
barplot(dataset$season)

#d)
cor.test(dataset$T1 , dataset$T2)
cor.test(dataset$hum , dataset$wind_speed)

#e

model_linear <- lm( formula = wind_speed ~ T1+T2+hum  )

#f



#2)
before <- vector(10 , 15, 9, 3, 7, 12, 16, 17 , 4)
after <- vector(12 , 17, 8, 5, 6, 11, 18 ,20 ,3)

mean_before <- mean(before)
mean_after <- mean(after)






