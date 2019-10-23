# ALY6015-Module 2 Project – Danlin Shen – 1st Version
# 23 April 2019

# Part A
# First, load the MASS library in R. 

# A. Package ‘MASS’ which provides a description of the datasets available in the MASS package.
# Then, complete the following analysis of the identified data from the library.
# to gain the package before the program could use the data.
require(MASS)

# B. One-sample t-test: 
# Use the “chem” dataset to answer the question, “is the flour production company producing whole meal flour with greater than 1 part per million copper in it?” 

# Solution: Right-tailed t-test
# Let's take the Company X call time example
# H0: mean copper <=  1/1000000
# H1: mean copper >  1/1000000
summary(chem)
t.test(chem, mu = 1/1000000, alternative = c("greater"), conf.level = 0.95) #where mu is the assumed population mean, included in our H0
# Conclusion: We have 95% confidence to reject H0 since p-value > alpha, which means the flour production company producing whole meal flour with greater than 1 part per million copper in it.


# C. Two-sample t-test: 
# Use the “cats” dataset to answer the question, “do male and female cat samples have the same body weight?” 
# Hint: one way to get separate vectors for male and female cat body weight is to use the subset function as follows: “male <-subset(cats, subset=(cats$Sex=M))” 
# Format
# Sex: sex: Factor with evels "F" and "M".
# Bwt: body weight in kg.
# Hwt: heart weight in g.

# Solution: Independent 2-group t-test
# H0: no difference between two groups
# H1: there is different body weight in two groups
summary(cats)
female <-subset(cats, subset=(cats$Sex=='F'))
summary(female)
male <-subset(cats, subset=(cats$Sex=="M"))
summary(male)
t.test(male$Bwt, female$Bwt, alternative = c("two.sided"), conf.level = 0.95)
# Conclusion: We have 95% confidence to reject H0 since p-value < alpha, which means there is different body weight in two groups.


# D. Paired t-test: 
# Use the “shoes” dataset to answer the question, “did material A wear better than material B?” 

# Solution: Paired t-test
# H0: material A - material B = 0
# H1: material A - material B = 0 != 0
summary(shoes)
t.test(shoes$A, shoes$B, paried = T, conf.level = 0.95)
# Conclusion: We have 95% confidence to accept H0 since p-value > alpha, which means material A wear is equal to material B.


# E. Test of equal or given proportions: 
# Use the “bacteria” data set to answer the question, “did the drug treatment have a significant effect of the presence of the bacteria compared with the placebo?” 
# Format:
# y: presence or absence: a factor with levels n and y.
# ap: active/placebo: a factor with levels a and p.
# hilo: hi/low compliance: a factor with levels hi amd lo.
# week: numeric: week of test.
# ID: subject ID: a factor.
# trt: a factor with levels placebo, drug and drug+, a re-coding of ap and hilo.

# Solution: Test of equal or given proportions
# H0: bacteria in drup group = bacteria in placebo group
# H1: bacteria in drup group != bacteria in placebo group
summary(bacteria)
bacteria_2 <- matrix(c(length(which(bacteria$trt=='placebo' & bacteria$y=='y')), length(which(bacteria$trt=='placebo' & bacteria$y=='n')), length(which(bacteria$trt!='placebo' & bacteria$y=='y')), length(which(bacteria$trt!='placebo' & bacteria$y=='n'))), ncol=2, byrow=T) # byrow: logical. If FALSE (the default) the matrix is filled by columns, otherwise the matrix is filled by rows.
print(bacteria_2)
colnames(bacteria_2) <- c('Placebo', 'Drug')
rownames(bacteria_2) <- c('Bacteria Present', 'Bacteria Absent')
print(bacteria_2)
prop.test(bacteria_2, p = NULL, alternative = c("two.sided"), conf.level = 0.95, correct = T)
# Conclusion: We have 95% confidence to reject H0 since p-value < alpha, which means the drug treatment have a significant effect of the presence of the bacteria compared with the placebo.


# F. F-test: 
# Use the “cats” data set to test for the variance of the body weight in male and female cats.

# Solution: F-test
# H0: the variance of the body weight in male cats = it in female cats
# H1: the variance of the body weight in male cats != it female cats
summary(cats)
var.test(male$Bwt, female$Bwt, alternative = c("two.sided"))
# Conclusion: We have 95% confidence to reject H0 since p-value < alpha, which means the variance of the body weight in male cats is not equal it in female cats.
  
  

# Part B
# Use the "Rubber" and "oddbooks" data sets, or choose two use other appropriate data sets, in R. 
# Then use the functions in section 5.4 of “Using R for Data Analysis and Graphics ” to build multiple regression models. 
# In addition, you need to install the DAAG package before you can complete this part of the assignment. Follow the steps below: 

# 1. Load the MASS and ggplot2 libraries and use the "Rubber" data set 
require(ggcorrplot)
require(ggplot2)
require(datasets)
# require(MASS)
data("Rubber")

# 2. Load the DAAG library and use the "oddbooks" data set 
install.packages("ggcorrplot")
install.packages("DAAG")
require(DAAG)
data("oddbooks")

# 3. Build multiple regression models using summary(), lm() and ggcorrplot() 

# Rubber
# Format:
# loss: the abrasion loss in gm/hr.
# hard: the hardness in Shore units.
# tens: tensile strength in kg/sq m.
summary(Rubber)
summary(lm(loss ~ hard + tens , data = Rubber))
plot(lm(loss ~ hard + tens, data = Rubber))
ggcorrplot(Rubber)

# oddbooks
summary(oddbooks)
summary(lm(weight ~ thick + height + breadth, data = oddbooks))
plot(lm(weight ~ thick + height + breadth, data = oddbooks))
ggcorrplot(oddbooks)
