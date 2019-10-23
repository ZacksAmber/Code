# ALY6015-Module 1 Project – Danlin Shen – 2nd Version
# April 16, 2019


# DESCRIPTIVE STATISTICS
# Show the summary of the dataset (Quickly understand the structure of the dataset)
summary(trees)
# Get the numbers of the rows
nrow(trees)

# a) Measures of central tendency:Mode
# Customize a function that calculates the mode
getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}

getmode(trees$Girth)
getmode(trees$Height)
getmode(trees$Volume)

# b) Measure of variability: Variance, Standard Deviation, Range, Quartiles

var(trees$Girth, na.rm = 1)
var(trees$Height, na.rm = 1)
var(trees$Volume, na.rm = 1)

sd(trees$Girth, na.rm = 1)
sd(trees$Height, na.rm = 1)
sd(trees$Volume, na.rm = 1)

range(trees$Girth, na.rm = 1)
range(trees$Height, na.rm = 1)
range(trees$Volume, na.rm = 1)

quantile(trees$Girth, probs=seq(0,1,0.25), na.rm = 1)
quantile(trees$Height, probs=seq(0,1,0.25), na.rm = 1)
quantile(trees$Volume, probs=seq(0,1,0.25), na.rm = 1)


# GRAPHICAL DESCRIPTIVE
# a) Histogram & Desity
# hist is a function to draw the histogram of the data. Breaks is a parameter to design the width of each column; Main is the title of the histogram; Freq: if true, the histogram graphic is a representation of frequencies; xlab, ylab: to name the x-axis and y-axis.
hist(trees$Girth, breaks=30, main='Histogram of Girth of Trees', freq=T, 
     xlab='Girth of Trees', ylab='Frequency')
plot(density(trees$Girth))

hist(trees$Height, breaks=80, main='Histogram of Height of Trees', freq=T, 
     xlab='Height of Trees', ylab='Frequency')
plot(density(trees$Height))

hist(trees$Volume, breaks=80, main='Volume of Girth of Trees', freq=T, 
     xlab='Volume of Trees', ylab='Frequency')
plot(density(trees$Volume))

# b) Boxplot
boxplot(trees$Girth, main='Box Plot of Girth of Trees')
boxplot(trees$Height, main='Box Plot of Height of Trees')
boxplot(trees$Volume, main='Box Plot of Volume of Trees')

# c) Check for normal distribution. A normal distribution follows the straight line.
# Girth is not a normal distribution. col: col is a parameter to change the color of the line.
qqnorm(trees$Girth)
qqline(trees$Girth, col='red')
# Height is a normal distribution
qqnorm(trees$Height)
qqline(trees$Height, col='red')
# Volume is not a normal distribution
qqnorm(trees$Volume)
qqline(trees$Volume, col='red')

# d) Scatter plots
# Formula: Girth = 2π * Radius
# Formula: Radius = Girth/2π
# Formula: Volume = Height * π * Radius^2 = Height * π * (Girth/2π)^2 
plot(trees$Height, trees$Girth, main='Height by Girth (no directly relationship)',
     xlab='Girth', ylab='Height')

plot(trees$Girth, trees$Volume, main='Girth by Volume (directly relationship)',
     xlab='Girth', ylab='Volume')


plot(trees$Volume, trees$Height, main='Volume by Height (no directly relationship)',
     xlab='Volume', ylab='Height')

# e) Liner Regression
summary(lm(Height ~ Girth, data = trees))
plot(lm(Height ~ Girth, data = trees))

cor(trees)
plot(trees)
plot(lm(Volume ~ Height + Girth, data = trees))
qqplot(trees$Volume, trees$Height, simulate = TRUE)

install.packages("glmnet")
library(glmnet)
summary(lm(Volume ~ ., data = trees))
install.packages("car")
library(car)
vif(lm(Volume ~ ., data = trees))


#summary(lm(Height ~ Volume, data = trees))
#plot(lm(Height ~ Volume, data = trees))

#summary(lm(Girth ~ Volume, data = trees))
#plot(lm(Girth ~ Volume, data = trees))