whr=read.csv("/Users/zhenganlyu/Library/Mobile Documents/com~apple~CloudDocs/Code/whr.csv")
whr
summary(whr)


library("DataExplorer")

whr = na.omit(whr) #remove missing values 
plot_correlation(whr) #create correlation heatmap to directly see the correlation between any two variables


#new data 
file.choose()
whr_alternate=read.csv("/Users/zhenganlyu/Library/Mobile Documents/com~apple~CloudDocs/whr_alternate.csv")
library(dplyr)
library("DataExplorer")

#select whr_alternate data frame that only includes 2017 year 
whr=read.csv("/Users/zhenganlyu/Library/Mobile Documents/com~apple~CloudDocs/Code/whr.csv")
whr
Year1=select(filter(whr_alternate, Year=="2017"), 
       "Country.name","Life.Ladder",
       "Log.GDP.per.capita","Social.support",
       "Healthy.life.expectancy.at.birth",
       "Freedom.to.make.life.choices","Generosity",
       "Perceptions.of.corruption","Positive.affect",
       "Negative.affect","Confidence.in.national.government",
       "Democratic.Quality","Delivery.Quality",
       "Standard.deviation.of.ladder.by.country.year",
       "Standard.deviation.Mean.of.ladder.by.country.year",
       "gini.of.household.income.reported.in.Gallup..by.wp5.year")
Year1

Year1 = na.omit(Year1) #remove missing values 
plot_correlation(Year1)
