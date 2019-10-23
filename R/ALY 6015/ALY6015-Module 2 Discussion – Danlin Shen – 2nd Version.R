# ALY6015-Module 2 Discussion – Danlin Shen – 2nd Version
# April 19, 2019
# Danlin Shen

# Load the data
uscars <<- read.table("Desktop/NEU/Quarter 2/ALY 6015/1/Assignment/uscars.csv", header=TRUE, sep=",") [1:318 ,1:3]
summary(uscars)


# Independent 2-group t-test
# H0: Households with vehicles in 2016 <= Households without vehicles in 2015
# H1: Households with vehicles in 2016 > Households without vehicles in 2015
# Automakers want to know if the US auto market in 2016 is shrinking compared to 2015. If the market shrinks, they will appropriately reduce vehicle production to avoid excessive market expansion.
t.test(uscars$X2015.Vehicles.per.Household, uscars$X2016.Vehicles.per.Household, alternative = c("greater"), conf.level = 0.95)
