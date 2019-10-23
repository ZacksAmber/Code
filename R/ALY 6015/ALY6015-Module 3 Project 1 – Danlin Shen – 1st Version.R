###############
# Exercise 1  #
###############
# Load the lars package and the diabetes dataset (Efron, Hastie, Johnstone and Tibshirani (2003) 
# “Least Angle Regression” Annals of Statistics). This has patient level data on the progression of diabetes. 
# Next, load the glmnet package that will be used to implement LASSO.

install.packages("lars")
library(lars)
library(glmnet)
data(diabetes)
attach(diabetes)
(diabetes$x)

data1 <- diabetes$x
data1
sex1 <- data1[,2]
lars

# Load the data
install.packages("lars")
library(lars)
library(glmnet)
data(diabetes)
attach(diabetes)
(diabetes$x)

# Extract the original data
data.original <- read.table("Desktop/diabetes.data.txt",head=TRUE);
data.



# Age
age1 <- data2[, 1]
age1
scale(data2, center = T, scale = F)
scale(data2)

age1.z <- (age1 - mean(age1))/sd(age1)
age1.z

# Sex
sex2 <- data2[, 2]
sex2

scale(sex2, center = TRUE, scale = FALSE)
scale(sex2, center = F, scale = F)
scale(sex2, center = T, scale = F)
z <- scale(sex2, center = T, scale = T)
norm(z, type = c("2"))
##################################
z/norm(z, type = c("2"))##########
##################################

data1 # age = 0.038
age1
scale(age1, center = T, scale = T)/norm(as.matrix(age1), type = c("2"))
age.z <- scale(age1, center = T, scale = T)
age.z/norm(age.z, type = c("2"))


data1 # bmi 0.06169
scale(data2[, 3], center = T, scale = T)/norm(scale(data2[, 3], center = T, scale = T), type = c("2"))
apply(data2, 2, function(x) scale(x, center = T, scale = T)/norm(scale(x, center = T, scale = T), type = c("2")))
tmp

y <- array(1:20, c(4,5))
y
#########
apply(data2, 2, function(x) scale(x)/norm(scale(x), type = c("2")))
#########

scale(x[, 4])/norm(scale(x[, 4]), type = c("2"))

# Z-Score
sex.z <- (sex2 - mean(sex2))/sd(sex2)
sex.z # scale(sex2, center = T, scale = T)
mean(sex.z)
sd(sex.z)

# Norm
sex.n <- norm(as.matrix(sex.z), type = c("1"))
sex.z/sex.n

sex.n <- norm(as.matrix(sex.z), type = c("1"))
sex.n
sex.z/sex.n

sum(sex3)


norm(sex3)
xp <- c(-1, 2, 3)
norm(as.matrix(xp), type = c("1"))


diabetes$x.sex
diabetes$Sex[1]
diabetes$x$sex
nrow(diabetes)
nrow(diabetes$sex which sex >1)
n = 0
n
for (i in 1:442){
  if (diabetes$sex[i] > 0) {n + 1}
}
n

# To avoid some variables in other programs that will interfere this program, we need to first remove the variables.

###############
# Exercise 2  #
###############
# The dataset has three matrices x, x2 and y. While x has a smaller set of independent variables, 
# x2 contains the full set with quadratic and interaction terms. y is the dependent variable which is 
# a quantitative measure of the progression of diabetes.
# It is a good idea to visually inspect the relationship of each of the predictors with the dependent variable. 
# Generate separate scatterplots with the line of best fit for all the predictors in x with y on the vertical axis. 
# Use a loop to automate the process.

# Make sure the variables are right.
length(x) # 4420
length(x2) # 28288
length(y) # 442
ncol(x) # 10
colnames(x) # "age" "sex" "bmi" "map" "tc"  "ldl" "hdl" "tch" "ltg" "glu"

summary(x)
# draw the plots in 2 rows and 5 columns
par(mfrow=c(2,5))
# using each attributes of x to draw the plots
for(i in 1:10){
  plot(x[,i], y)
  abline(lm(y~x[,i]))
}
layout(1)


###############
# Exercise 3  #
###############
# Regress y on the predictors in x using OLS. We will use this result as benchmark for comparison.

model_ols <- lm(y ~ x)
summary(model_ols)
# This is OLS. If it is a liner regression, we can see that age, bmi, map, and ltg as the features have strong relationship 
# with y, and others do not; however, if it is a multicollinearity, we cannot simpliy use the p-value to report
# the errors.



###############
# Exercise 4  #
###############
# Use the glmnet function to plot the path of each of x’s variable coefficients against the L1 norm of the 
# beta vector. This graph indicates at which stage each coefficient shrinks to zero.

model_lasso <- glmnet(x, y)
par(mfrow=c(1,1))
plot.glmnet(model_lasso, xvar = "norm", label = TRUE)
plot.glmnet(model_lasso, xvar = "lambda", label = TRUE)


###############
# Exercise 5  #
###############
# Use the cv.glmnet function to get the cross validation curve and the value of lambda that minimizes 
# the mean cross validation error.

cv_fit <- cv.glmnet(x=x, y=y, alpha = 1, nlambda = 1000)
plot.cv.glmnet(cv_fit)

# lambda.min is minimum lambda.
cv_fit$lambda.min


###############
# Exercise 6  #
###############
# Using the minimum value of lambda from the previous exercise, get the estimated beta matrix. 
# Note that some coefficients have been shrunk to zero. This indicates which predictors are important in 
# explaining the variation in y.
fit <- glmnet(x=x, y=y, alpha = 1, lambda=cv_fit$lambda.min)
fit$beta


###############
# Exercise 7  #
###############
# To get a more parsimonious model we can use a higher value of lambda that is within one standard error 
# of the minimum. Use this value of lambda to get the beta coefficients. Note that more coefficients are now 
# shrunk to zero.
cv_fit$lambda.1se
fit <- glmnet(x=x, y=y, alpha = 1, lambda=cv_fit$lambda.1se)
fit$beta


###############
# Exercise 8  #
###############
# As mentioned earlier, x2 contains a wider variety of predictors. Using OLS, regress y on x2 and evaluate results.
model_ols2 <- lm(y~x2)
summary(model_ols2)


###############
# Exercise 9  #
###############
# Repeat exercise-4 for the new model.

model_lasso1 <- glmnet(x2, y)
plot.glmnet(model_lasso1, xvar = "norm", label = TRUE)
plot.glmnet(model_lasso1, xvar = "lambda", label = TRUE)


###############
# Exercise 10 #
###############
# Repeat exercises 5 and 6 for the new model and see which coefficients are shrunk to zero. 
# This is an effective way to narrow down on important predictors when there are many candidates.

cv_fit1 <- cv.glmnet(x=x2, y=y, alpha = 1, nlambda = 1000)
plot.cv.glmnet(cv_fit1)
fit1 <- glmnet(x=x2, y=y, alpha = 1, lambda=cv_fit1$lambda.min)
fit1$beta
