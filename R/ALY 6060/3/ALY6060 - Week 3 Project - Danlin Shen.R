# ALY6060 - Week 3 Project – Danlin Shen
# 1015

#############
# Questions #
#############
# Using the provided dataset, please answer the following questions:
  
# 1. Create a set of simple linear regressions of each covariate against the outcome variable.
# Based on your simple linear models, rank order the covariates by the strongest R^2 association to the outcome.  
# Answer:
# The Rank of R^2(From high to low):
# 
# Rating
# Multiple R-squared:  0.7458,	Adjusted R-squared:  0.7452 
# 
# Limit
# Multiple R-squared:  0.7425,	Adjusted R-squared:  0.7419 
# 
# Income
# Multiple R-squared:  0.215,	Adjusted R-squared:  0.213 
# 
# Student
# Multiple R-squared:  0.06709,	Adjusted R-squared:  0.06475 
# 
# Education
# Multiple R-squared:  6.499e-05,	Adjusted R-squared:  -0.002447 
# 
# Married
# Multiple R-squared:  3.219e-05,	Adjusted R-squared:  -0.00248
# 
# Age
# Multiple R-squared:  3.368e-06,	Adjusted R-squared:  -0.002509 

# What are the top two covariates?
# Anwser: Rating and Limit

# 2. Generate the Full model (Hint: In your code, list the covariate with the strongest association first, 
# second strongest associate listed second, etc.)
# Which of the covariates have significant association with the outcome in the full model? 
# Answer: Rating and Income

# Are these the same covariates you would have expected based on your simple linear models?
# Answer: No. After summary fits on Rating + Limit + Income vs. Balance. The Limit has too big p-value.
#         Therefore, I removed the Limit.

# Answer:

# 3. Senior Leadership states that the acquisition of third party credit scores is a significant expense for the 
#    Bank, and is asking if this data is valuable? 
#    Explain you data-driven recommendation to Senior Leadership, as to whether or not the Credit Ratings add 
#    significant value to the model’s predictive power.
# Answer: Yes, I think the Credit Scores from the thrid party is VALUABLE. Because Rating is the crucial factor
#         for impacting on the balance. If Northeastern Bank wants to accomplish its targe, this cost is inevitable.
#         However, I highly recommend the CEO should consider associate with other banks, the insurance companies,
#         online shopping platforms, and etc. to collect the credit scores leading to reduce the cost and improve the
#         veracity.

#############
# Load data #
#############
# setwd("")
setwd("~/Desktop/NEU/Quarter 3/ALY 6060 Decision Support & Business Intelligence/Assignments/3/Analytics Assignment")

Credit<- read.csv("Credit.csv")

####################
# Summary of  data #
####################
head(Credit)

summary(Credit)

hist(Credit$Balance)

install.packages("DataExplorer")
library(DataExplorer)

plot_intro(Credit)

plot_bar(Credit)

plot_histogram(Credit)

install.packages("corrplot")
install.packages("Hmisc")
library("Hmisc")
library(corrplot)
source("http://www.sthda.com/upload/rquery_cormat.r")
rcorr(as.matrix(Credit), type = c("pearson","spearman"))

rquery.cormat(Credit)

######################
# Data Preprocessing #
######################
# Replace the nominal data "No" as 0, "Yes" as 1.
Credit$Student <- as.character(Credit$Student)
Credit$Student[Credit$Student == "No"] <- 0
Credit$Student[Credit$Student == "Yes"] <- 1
Credit$Student <- as.integer(Credit$Student)

Credit$Married <- as.character(Credit$Married)
Credit$Married[Credit$Married == "No"] <- 0
Credit$Married[Credit$Married == "Yes"] <- 1
Credit$Married <- as.integer(Credit$Married)

head(Credit)

# L2 Normalization
# Credit.norm <- apply(Credit, 2, function(x) scale(x, center = T, scale = T)/norm(scale(x, center = T, scale = T), "1"))
# Credit.norm <- as.data.frame(Credit.norm)

# head(Credit.norm)

##############
# Question 1 #
##############
plot_qq(Credit)

plot_correlation(Credit)

# summary fits on Income vs. Balance

lm.fit.Income<- lm(Balance~Income,data = Credit)

summary(lm.fit.Income) # p-value: < 2.2e-16

confint(lm.fit.Income)

plot(Balance~Income,data = Credit, main = 'Balance vs. Income')
abline(lm.fit.Income)

# summary fits on Limit vs. Balance

lm.fit.Limit<- lm(Balance~Limit,data = Credit)

summary(lm.fit.Limit) # p-value: < 2.2e-16

confint(lm.fit.Limit)

plot(Balance~Limit,data = Credit, main = 'Balance vs. Limit')
abline(lm.fit.Limit)

# summary fits on Rating vs. Balance

lm.fit.Rating<- lm(Balance~Rating,data = Credit)

summary(lm.fit.Rating) # p-value: < 2.2e-16

confint(lm.fit.Rating)

plot(Balance~Rating,data = Credit, main = 'Balance vs. Rating')
abline(lm.fit.Rating)

# summary fits on Age vs. Balance

lm.fit.Age<- lm(Balance~Age,data = Credit)

summary(lm.fit.Age) # p-value: 0.9708

confint(lm.fit.Age)

plot(Balance~Age,data = Credit, main = 'Balance vs. Age')
abline(lm.fit.Age)

# summary fits on Education vs. Balance

lm.fit.Education<- lm(Balance~Education,data = Credit)

summary(lm.fit.Education) # p-value: 0.8723

confint(lm.fit.Education)

plot(Balance~Education,data = Credit, main = 'Balance vs. Education')
abline(lm.fit.Education)

# summary fits on Student vs. Balance

lm.fit.Student<- lm(Balance~Student,data = Credit)

summary(lm.fit.Student) # p-value: 1.488e-07
 
confint(lm.fit.Student)

plot(Balance~Student,data = Credit, main = 'Balance vs. Student')
abline(lm.fit.Student)

# summary fits on Married vs. Balance

lm.fit.Married<- lm(Balance~Married,data = Credit)

summary(lm.fit.Married) # p-value: 0.9099

confint(lm.fit.Married)

plot(Balance~Married,data = Credit, main = 'Balance vs. Married')
abline(lm.fit.Married)

##############
# Question 2 #
##############
# summary fit full model
lm.fit.full<-lm(Balance~Rating+Limit+Income+Student+Education+Married+Age+Rating*Limit*Income*Student*Education*Married*Age,data = Credit)

summary(lm.fit.full) 

confint(lm.fit.full)

# summary fits on Rating + Limit + Income vs. Balance
lm.fit.RatingLimitIncome<-lm(Balance~Rating+Limit+Income,data = Credit)

summary(lm.fit.RatingLimitIncome)

confint(lm.fit.RatingLimitIncome)

# Notice that Limit actually has too big p value, therefore the final regression should remove Limit.
# key points: Limit, Student, Education, Married, Age are no longer significant.
# use Rating and Income no Student, Education, Married, Age to build final model
lm.fit.interaction<-lm(Balance~Rating+Income+Rating*Income,data = Credit)
summary(lm.fit.interaction)
