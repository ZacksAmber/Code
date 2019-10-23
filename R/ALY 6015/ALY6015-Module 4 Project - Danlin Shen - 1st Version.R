# ALY6015-Module 4 Project – Danlin Shen – 1st Version
# May 7, 2019

install.packages("factoextra")
install.packages("NbClust")
install.packages("party")
install.packages("randomForest")
install.packages("dbscan")
install.packages("fpc")
library(party)
library(MASS)

# Part A
str(Boston)
Boston

# crim: per capita crime rate by town.
# zn: proportion of residential land zoned for lots over 25,000 sq.ft.
# indus: proportion of non-retail business acres per town.
# chas: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise).
# nox: nitrogen oxides concentration (parts per 10 million).
# rm: average number of rooms per dwelling.
# age: proportion of owner-occupied units built prior to 1940.
# dis: weighted mean of distances to five Boston employment centres.
# rad: index of accessibility to radial highways.
# tax: full-value property-tax rate per \$10,000.
# ptratio: pupil-teacher ratio by town.
# black: 1000(Bk − 0.63)2 where Bk is the proportion of blacks by town.
# lstat: lower status of the population (percent).
# medv: median value of owner-occupied homes in \$1000s.
# Price: Classify Boston's house prices according to medv's quartile.

# The L1 norm that is calculated as the sum of the absolute values of the vector.
# The L2 norm that is calculated as the square root of the sum of the squared vector values.
# The max norm that is calculated as the maximum vector values.


# nB: new Boston data.
nB <- Boston
nB
class(nB)
nB.matraix <- as.matrix(Boston)
nB.matraix
class(nB.matraix)

nB.norm <- apply(nB, 2, function(x) scale(x, center = T, scale = T)/norm(scale(x, center = T, scale = T), "1"))
nB.norm

ncol(nB)
nrow(nB)
length(nB) == ncol(nB)
scale(Boston$crim, center = T, scale = T)
scale(Housing.original, center = T, scale = T)
as.matrix(nB)


nB
# Price: Classify Boston's house prices according to medv's quartile.
nB[, 5]
summary(nB)
cat(nB)
nB[490:506, ]

# Test
for (i in 1:10) {
  if (nB$medv[i] < 17.02) {cat(i, ":", nB$medv[i], "Poor","\n")}
  if (17.02 <= nB$medv[i] & nB$medv[i]  < 21.20) {cat(i, ":", nB$medv[i], "Cheap","\n")}
  if (21.20 <= nB$medv[i] & nB$medv[i]  < 22.53) {cat(i, ":", nB$medv[i], "Medium","\n")}
  if (22.53 <= nB$medv[i] & nB$medv[i]  < 25.00) {cat(i, ":", nB$medv[i], "Dear","\n")}
  if (25.00 <= nB$medv[i]) {cat(i, ":", nB$medv[i], "Luxary","\n")}
}


# Decision tree could only predict categorical data. Therefore, we should add categorical data according to medv.
for (i in 1:nrow(nB)) {
  if (nB$medv[i] < 17.02) {nB$Price[i] <- "Poor"}
  if (17.02 <= nB$medv[i] & nB$medv[i]  < 21.20) {nB$Price[i] <- "Cheap"}
  if (21.20 <= nB$medv[i] & nB$medv[i]  < 22.53) {nB$Price[i] <- "Medium"}
  if (22.53 <= nB$medv[i] & nB$medv[i]  < 25.00) {nB$Price[i] <- "Expensive"}
  if (25.00 <= nB$medv[i]) {nB$Price[i] <- "Luxury"}
}
# Convert the Price from character to factor.
nB$Price <- as.factor(nB$Price)


# split into training and test datasets
set.seed(100) # set.seed(): Generate random numbers in a specific order for simple verification.
index.nB <- sample(2, nrow(nB), replace=T, prob=c(0.7, 0.3))
nB.train <- nB[index.nB==1, ]
nB.test <- nB[index.nB==2, ]

str(nB.train)
str(nB.test)
class(nB.train)

# build a decision tree
nB.formula <- Price ~ crim + zn + indus + chas + nox + rm + age + dis + rad + tax + ptratio + black + lstat
nB.ctree <- ctree(nB.formula, data=nB.train)
plot(nB.ctree)
class(nB.formula)

class(nB.ctree)

# predict on test data
pred <- predict(nB.ctree, newdata = nB.test) # check prediction result
table(pred, nB.test$Price)
nB.test
# Conclusion: From the statistical results, using the crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio
# black, and lstat could predict the range of the housing price.


# Part B
set.seed(200)
nB2 <- nB.norm
# remove class IDs
nB2$Price <- NULL
# k-means clustering
nB.norm.kmeans <- kmeans(nB2, 5)
# check result
table(nB.norm$Price, nB.kmeans$cluster)
summary(nB)

nB.norm.kmeans
# plot clusters and their centers
plot(nB2[c("crim", "tax")], col=nB.norm.kmeans$cluster)
points(nB.kmeans$centers[, c("crim", "tax")],
       col=1:3, pch="*", cex=5)

library(fpc)
nB2 <- nB[-5] # remove class IDs
# DBSCAN clustering
ds <- dbscan(nB2, eps = 0.42, MinPts = 5) # compare clusters with original class IDs table(ds$cluster, iris$Species)

iris[-5]
iris
