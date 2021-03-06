#

install.packages("datasets")
require(datasets)



# DESCRIPTIVE STATISTICS

# a) Exploratory: head()
head(mtcars)

# b) Selecting individual fields: $
mtcars$mpg

# c) Measures of central tendency: Mean, Median, Mode
mean(mtcars$hp)
median(mtcars$hp)

# Create the function.
getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}

getmode(mtcars $hp)

# d) Measure of variability: Variance, Standard Deviation, Range, Quartiles

var(mtcars$hp)
sd(mtcars$hp)
range(mtcars$hp)
quantile(mtcars $hp, probs=seq(0,1,0.25))
quantile(mtcars $hp, probs=0.5)

# e) What does the summary() function do?
summary(mtcars)

sum(is.na(mtcars$hp))

sum(!is.na(mtcars$hp))


# Get the number of rows in the dataset
nrow(mtcars)

# Get the number of colums in the dataset
ncol(mtcars)

# Get coulmn names
names(mtcars)
colnames(mtcars)

# Subsetting - which, tapply, indexing
which(mtcars$cyl > 4)
mtcars[which(mtcars$cy1 > 4),]
mtcars[,which(colnames(mtcars)=="hp")]

# tapply - for grouping
tapply(mtcars$qsec, mtcars$gear)

# indexing - for selecting specific values
mtcars[1,6:8]
mtcars[5:9, 'qsec']
mtcars[5:9, c('qsec','vs')]
mtcars[7, !is.na('cyl')]

# Object assignment - you can use '=' or '<-'
x = 7
x <- 7

# Vector Operations

# Let's create a numeric, a character, and a factor vector
w <- c(0, 2, 4, 9)
x <- c(5, 6, 2, 1)
y <- c('yellow', 'green', 'red', 'greeen')
z <- factor(c('banana', 'gradpe', 'apple', 'grape'), levels=c('grape', 'apple', 'banana'))
t <- c(0, 2, 4)

# use the class() function to dinf the type of data you have
class(x)
class(y)
class(z)
class(mtcars$hp)

# Factors can be numbers or words, but they have an intrinsic ordering and grouping:
# Set the order of the fruites to be smllest to largest and compare the summaries of y and z
summary(y)
summary(z)

# Add the w and x vectors to produce a new vector with the operation aligned by indices
w + x
# Bectors should be of the same 
w*t

# Create a dataframe by combining vectors of the same length
df <- data.frame(w, x)

# VISUALIZTIONS

# a) Historam
hist(mtcars$hp, breaks=6, density=TRUE, main='Histogram of mtcars HP',
     xlab='HP', ylab='Frequency')

# b) Boxplot
plot(mtcars$hp ~ mtcars$cyl, main='Horspower by Cylinders',
     xlab='cyl', ylab='HP')

# d) Adding the normal curve (see: curve)
plot (qnorm)
curve(x^3 - 3*x, from=-2, to=2)

# e) Check for normal distribution (see: qq)
qqplot(mtcars$hp)

# f) Scatter plots
plot(mtcars$hp, mtcars$vs, main='HP by vs',
     xlab='HP', ylab='VS')

# Checking working directory
getwd()
setwd('..')
getwd()

dataset_name <- read.csv('example_data.csv')


names(mtcars)

# Which fields are best for this analysis> How about subsetting (see: which)> Grouping (see:

# 