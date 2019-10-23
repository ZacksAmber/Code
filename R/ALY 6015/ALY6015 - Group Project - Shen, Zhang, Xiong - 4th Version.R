# ALY6015 - Group Project – Shen, Zhang, Xiong – 4th Version
# Group member: Danlin Shen, Pengfei Zhange, Gugu Xiong

# Install & Load
install.packages("factoextra")
install.packages("NbClust")
install.packages("party")
install.packages("randomForest")
install.packages("dbscan")
install.packages("fpc")
install.packages("glmnet")
library("glmnet") 
library("party")
library("MASS")

# price: Price per suqared meter(unit: ¥, Yuan)
# subway: Is there a subway nearby?
# district: Distance from the city center (unit: km).
# square: Housing area (unit: square meters).
# livingRoom: Number of living rooms.
# drawingRoom: Number of drawing rooms.
# kitchen: Number of kitchens.
# bathRoom: Number of bathrooms.
Housing.original <- read.table("Desktop/Beijing Price.csv", head=TRUE, sep=",") # The working diriction maybe changed
Housing.original # Housing.original is the data that should not be modified.


###########################################
# Distripitive Statistics - Pengfei Zhang #
###########################################
# Summary of Bejing Housing
head(Housing.original)
summary(Housing.original)
# R doesn't have a function for calcuating mode so we will quote a function
getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}

getmode(Housing.original$price)

# Our destination is to find out the relationships between price of Beijing Housing and others variables.
Housing.original$price


# VISUALIZATIONS
# a) Histogram
hist(Housing.original$price, breaks=100, main='Histogram of Price',
     xlab='Price', ylab='Frequency')

# Check for normal distribution (see: qq)
qqnorm(Housing.original$price)
qqline(Housing.original$price)
plot(Housing.original$price ~ Housing.original$district)


####################################
# Data Preprocessing - Danlin Shen #
####################################
# 1. Convert all of the data: All of the matrix will be standardized to have unit L1 norm in each column and 
# zero mean. L1 norm is uesd for Lasso and descision tree.
Housing.norm <- apply(Housing.original, 2, function(x) scale(x, center = T, scale = T)/norm(scale(x, center = T, scale = T), "1"))
Housing.norm # Housing.norm is the data have been standardized to have unit L1 norm in each column and zero mean.

# Exlanation & Testing
# Before we start analyzing the data, we have to preprocess the data -- if you don't, the data won't be in the 
# same range. For example, in this program, we can't directly compare the relationships in the numbers of the 
# bathroom, the price per squared meter, and the distance from the city center, because they have huge differences
# in position and scale that in the coordinate system. Therefore, through data preprocessing, we can put all of 
# the variables near the origin of the coordinate system without changing the data distribution. I will use 
# z-mean and L1 normalization. Step 1 is to move the data to the origin. Step 2 is to compress the range 
# of the data to [0, 1].
sub.o <- Housing.original$subway
sub.1<- sub.o - mean(sub.o) # Step 1
sub.2 <- (sub.o - mean(sub.o))/(sd(sub.o)) # Step 2
sub.2/norm(as.matrix(sub.2), "1")  # Step 2

# 2. Add the discription of the price
price <- Housing.original$price
summary(price) # Find out the minmum, the 1st quantile, the median, the mean, the 3
boxplot(price)
# We can notice that there are some points above the boxplot which are larger than the maximum of the 
# boxplot(about 90,000). Therefore, I set 90,000 as the luxury level.

# Description: Classify Beijing's house prices according to the price quartiles.
# Testing
for (i in 1:100) {
  if (price[i] < 27806) {cat(i, ":", price[i], "Poor","\n")}
  if (27806 <= price[i] & price[i]  < 38292) {cat(i, ":", price[i], "Cheap","\n")}
  if (38292 <= price[i] & price[i]  < 54240) {cat(i, ":", price[i], "Medium","\n")}
  if (54240 <= price[i] & price[i]  < 90000) {cat(i, ":", price[i], "Expensive","\n")}
  if (90000 <= price[i]) {cat(i, ":", price[i], "Luxary","\n")}
}

# The decision tree can only predict data using numerical data or categorical data. Essentially, 
# this is a data classification. Therefore categorical data must be used as the y value. Since the original 
# data does not have a y value, I use a piece of code to generate the y value.
Housing.tree <- Housing.original
for (i in 1:nrow(Housing.tree)) {
  if (Housing.tree$price[i] < 27806) {Housing.tree$Description[i] <- "Poor"}
  if (27806 <= Housing.tree$price[i] & price[i]  < 38292) {Housing.tree$Description[i] <- "Cheap"}
  if (38292 <= Housing.tree$price[i] & price[i]  < 54240) {Housing.tree$Description[i] <- "Medium"}
  if (54240 <= Housing.tree$price[i] & price[i]  < 90000) {Housing.tree$Description[i] <- "Expensive"}
  if (90000 <= Housing.tree$price[i]) {Housing.tree$Description[i] <- "Luxury"}
}
Housing.tree # Housing.tree is the data that has extral label to dscribe the price


###############################
# Decision Tree - Danlin Shen #
###############################
# Generate Tree dataset
Housing.norm <- as.data.frame(Housing.norm)
Tree <- Housing.norm
Tree$Description <- factor(Housing.tree$Description) # Convert the Description from character to factor.

# split into training and test Housing.originals
set.seed(100) # set.seed(): Generate random numbers in a specific order for simple verification.
Tree.index <- sample(2, nrow(Tree), replace=TRUE, prob=c(0.7, 0.3))
Tree.train <- Tree[Tree.index==1, ]
Tree.test <- Tree[Tree.index==2, ]
str(Tree.train)
str(Tree.test)

# build a decision tree
Tree.formula <- Description ~ subway + district + square + livingRoom + drawingRoom + kitchen + bathRoom
Tree.ctree <- ctree(Tree.formula, data=Tree.train)
plot(Tree.ctree)

# predict on test data
pred <- predict(Tree.ctree, newdata = Tree.test) # check prediction result
table(pred, Tree.test$Description)
Tree.test
# Conclusion: From the statistical results, using the subway, district, square, livingRoom, drawingRoom, kitchen, 
# and bathRoom could predict the range of the housing price. Therefore, if new data has the same characteristics
# as the decision tree model, the category can be predicted.


######################
# Lasso - Gugu Xiong #
######################
Housing.original <- read.table("/Users/guxiongxiong/Desktop/BeijingPrice.csv", head=T,sep=",") # The working diriction maybe changed
head(Housing.original) 

Housing.norm <- apply(Housing.original, 2, function(x) scale(x, center = T, scale = T)/norm(scale(x, center = T, scale = T), "1"))
head(Housing.norm) 

pairs(Housing.norm)

Housing.norm <- as.data.frame(Housing.norm)
class(Housing.norm)
Housing.norm
model_OLS <- lm(price~subway+district+square+livingRoom+drawingRoom+kitchen+bathRoom, data=Housing.norm)
summary(model_OLS)
par(mfrow=c(2,2))
plot(model_OLS)

#Extraction regression coefficient:
coef.ols <- coef(model_OLS)

#Finding regression coefficients not equal to 0:
coef.ols[coef.ols!=0]

##ggcorrplot
corr_Housing <- round(cor(Housing.norm),1)
head(corr_Housing[,1:7])
install.packages("ggcorrplot")
library(ggcorrplot)
ggcorrplot(corr_Housing)

##first regularization
model_OLS1 <- lm(price~subway+drawingRoom+kitchen+bathRoom, data=Housing.norm)
summary(model_OLS1)
###do not work well


##When we try to figure out the coefficients that are not equal to 0, all the factors still exist.

##Lasso
install.packages("glmnet")
library("glmnet") 

lasso.1 <- glmnet(x = as.matrix(Housing.norm[1:400,2:8]), y = as.matrix(Housing.norm[1:400,1]),alpha=1)
plot.glmnet(lasso.1, xvar = "norm", label = T)

##We use the cv.glmnet function to get the cross-validation curve and the lambda value.

cvfit <- cv.glmnet(x=as.matrix(Housing.norm[1:400,2:8]), y=as.matrix(Housing.norm[1:400,1]), alpha=1, nlambda=1000)
plot.cv.glmnet(cvfit)

##To gain the value of lambda that minimizes the mean cross-validation error.

cvfit$lambda.min

###fit-min


fit1 <- glmnet(x=as.matrix(Housing.norm[1:400,2:8]), y=as.matrix(Housing.norm[1:400,1]),alpha = 1, lambda=cvfit$lambda.min)
fit1$beta

fit2 <- glmnet(x=as.matrix(Housing.norm[1:400,2:8]), y=as.matrix(Housing.norm[1:400,1]),alpha = 1, lambda=cvfit$lambda.1se)
fit2$beta

model_OLS2 <- lm(price~subway+kitchen+bathRoom, data=Housing.norm)
summary(model_OLS2)