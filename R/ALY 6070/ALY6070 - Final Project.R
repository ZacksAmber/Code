################################################################################
# Title: ALY6070 - Final Project.R                                             #
# Created Date: June 19, 2019, 3:42:54 pm                                      #
# Author: Danlin Shen(shen.da@husky.neu.edu)                                   #
# Github: https://github.com/ZacksAmber/R                                      #
# Copyright (c) 2019 Danlin Shen                                               #
################################################################################

library("tidyverse")
library("ggplot2")

getwd()
setwd("/Users/zack/Desktop/Code/R/ALY 6070")

cod_2 <- read.csv("Cause-of-Death-2017_Global_and_Regional_Estimates.csv")
cod_3 <- read.csv("Cause-of-Death-2017_Three_Countries.csv")

# Pre: Preterm
# Int: Intrapartum
# Sep: Sepsis
# Tet: Tetanus
# Con: Congenital
# Pne: Pneumonia
# Dia: Diarrhoea
# Mal: Malaria
# AID: AIDS       
# Mea: Measles
# Inj: Injury
# Men: Meningitis
# Oth: Other

# 2)	Prepare summary graph for your countries of 2016 under 5 mortality rates by cause of death using the second dataset: Cause-of-death 2017

# After each graph, provide your analysis and offer your insights and observations to guide the viewer to your key findings.

# a.	It is up to you whether you want to summarize for all children ages 5 and under (columns C thru P) or by age group Newborns vs. 1 – 59 months (columns Q thru AG) or both. You might consider analyzing both comparisons and identifying which version of your graph has the more compelling story. Justify your selection in your written section of your paper.
# Extract data of Deaths of children under 5 years of age due to (percentage) in 2016
cod_3_1 <- cod_3[1:13, 1:4]

ggplot(data = cod_3_1)+
  geom_point(aes(x = Type, y = CHN.2016, color = 'red'))+
  geom_point(aes(x = Type, y = USA.2016, color = 'blue'))+
  geom_point(aes(x = Type, y = SOM.2016, color = 'yellow'))+
  ggtitle("Deaths of children under 5 years of age due to (percentage)",
          subtitle = "2016")+
  ylab("Percentage")+
  scale_colour_hue(name = "Countries",
                   labels = c("China", "United States of America", "Somalia"))

# b.	Indicate visually on your graphs the top three causes of death utilizing the tools we discussed during lecture (e.g. highlight colors, size, shape, etc.)
ggplot(data = cod_3_1)+
  geom_point(aes(x = Type, y = CHN.2016, color = 'red', size = CHN.2016))+
  geom_point(aes(x = Type, y = USA.2016, color = 'blue', size = USA.2016))+
  geom_point(aes(x = Type, y = SOM.2016, color = 'yellow', size = SOM.2016))+
  ggtitle("Deaths of children under 5 years of age due to (percentage)",
          subtitle = "2016")+
  ylab("Percentage")+
  scale_colour_hue(name = "Countries",
                   labels = c("China", "United States of America", "Somalia"))+
  scale_size(name = "Death Rate: %")

# c.	Compare the top three causes of death for your selected countries in 2016 to the year 2000 which is also available in the same dataset. 
cod_4_1 <- cod_3[1:13, c(1, 5, 6, 7)]

ggplot()+
  geom_point(data = cod_4_1, aes(x = Type, y = CHN.2000, color = 'red', size = CHN.2000), shape = 17)+
  geom_point(data = cod_3_1, aes(x = Type, y = CHN.2016, color = 'red', size = CHN.2016))+
  geom_point(data = cod_4_1, aes(x = Type, y = USA.2000, color = 'blue', size = USA.2000), shape = 17)+
  geom_point(data = cod_3_1, aes(x = Type, y = USA.2016, color = 'blue', size = USA.2016))+
  geom_point(data = cod_4_1, aes(x = Type, y = SOM.2000, color = 'yellow', size = SOM.2000), shape = 17)+
  geom_point(data = cod_3_1, aes(x = Type, y = SOM.2016, color = 'yellow', size = SOM.2016))+
  ggtitle("Deaths of children under 5 years of age due to (percentage)",
          subtitle = "2000 to 2016")+
  ylab("Percentage")+
  scale_colour_hue(name = "Countries",
                   labels = c("China", "United States of America", "Somalia"))+
  scale_size(name = "Death Rate: %\nTriange = 2000\nCircle = 2016")

# Extract data from each continent
cod_2 <- cod_2[1:13, ]

ggplot()+
  geom_point(data = cod_4_1, aes(x = Type, y = CHN.2000, color = 'red', size = CHN.2000), shape = 17)+
  geom_point(data = cod_3_1, aes(x = Type, y = CHN.2016, color = 'red', size = CHN.2016))+
  geom_point(data = cod_2, aes(x = Region.Name, y = East.Asia.and.Pacific.2000, size = East.Asia.and.Pacific.2000, color = "orange"), shape = 17)+
  geom_point(data = cod_2, aes(x = Region.Name, y = East.Asia.and.Pacific.2016, size = East.Asia.and.Pacific.2016, color = "orange"))+
  geom_point(data = cod_2, aes(x = Region.Name, y = World.2000, size = World.2000, color = "gray"), shape = 17)+
  geom_point(data = cod_2, aes(x = Region.Name, y = World.2016, size = World.2016, color = "gray"))+
  ggtitle("Deaths of children under 5 years of age due to (percentage)",
          subtitle = "China vs. East Asia and Pacific vs. World")+
  ylab("Percentage")+
  scale_colour_hue(name = "Countries",
                   labels = c("China", "East Asia and Pacific", "World"))+
  scale_size(name = "Death Rate: %\nTriange = 2000\nCircle = 2016")
