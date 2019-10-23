# ALY6015-Module 5 Project – Danlin Shen – 1st Version
install.packages("TTR")
library(TTR)
install.packages("tseries")
library(tseries)
install.packages("forecast")
library(forecast)


##########
# Part A #
##########
# 1. Load data
data("AirPassengers")
# The classic Box & Jenkins airline data. Monthly totals of international airline passengers, 1949 to 1960.
a <- AirPassengers
a

# 2. Analyze data
plot.ts(a)
abline(reg=lm(a ~ time(a)))
plot(aggregate(a, FUN=mean))
cycle(a)
boxplot(a ~ cycle(a))
# Conclusion: 1. The annual trend shows that the number of passengers is increasing every year.
# Conclusion: 2. The average and variance of July and August are much higher than in other months.
# Conclusion: 3. The average for each month is not the same, but the difference in variance is small. 
# Therefore, it can be seen that there is a strong periodicity. One cycle is 12 months or less.

# 3. Decompose data
a.d <- decompose(a)
plot(a.d)
# The plot shows the original time series (top), the estimated trend component (second from top), 
# the estimated seasonal component (third from top), and the estimated irregular component (bottom). 
# We see that the estimated trend component shows continuous increase from about 100 in 1949 to about 450 in 1960.
a.a <- a - a.d$seasonal
plot(a.a)
# The plot shows the original time series without seasonal time series.


##########
# Part B #
##########
plot.ts(a)
adf.test(diff(log(a)), alternative="stationary", k=0) # Stationary series

acf(log(a))
pacf(log(a))
# The blue line above shows significantly different values than zero. Clearly, the graph above has a cut off 
# on PACF curve after 2nd lag which means this is mostly an AR(2) process.

a.d1 <- diff(log(a), differences = 1)
plot(a.d1)

acf(a.d1, lag.max = 20) #  q = 1 or 2
# an ARMA(0,1) model, that is, a moving average model of order q=1, since the autocorrelogram is zero after 
# lag 1 and the partial autocorrelogram tails off to zero.
acf(a.d1, lag.max = 20, plot = F)

pacf(a.d1, lag.max = 20) 
# p = 0, an ARMA(0,0) model, that is, an autoregressive model of order p=0, since the partial autocorrelogram 
# is zero after lag 0, and the autocorrelogram tails off to zero (although perhaps too abruptly for this model 
# to be appropriate)
pacf(a.d1, lag.max = 20, plot = F)

fit <- arima(log(a), c(0, 1, 1),seasonal = list(order = c(0, 1, 1), period = 12))
pred <- predict(fit, n.ahead = 10*12)
ts.plot(a,2.718^pred$pred, log = "y", lty = c(1,3))
