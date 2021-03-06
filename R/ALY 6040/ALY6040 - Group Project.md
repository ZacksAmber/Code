

# Introduction
As we all know, Japan used to be the richest country in Asia. In its most prosperous period, it could buy the whole US with only one Tokyo. However, we already know that this was caused by the huge real estate bubble resulting from the rapid increase of the exchange rate of Japanese yen to the US dollar.

Now, China has surpassed Japan to become the world's second-largest economy. Research shows that the ratio of China's first-tier cities and local per capita wages have exceeded four times that of Tokyo at the time. But China's per capita GDP is far less than that of Japan. In other words, In the case of China's first-tier cities, the relative housing prices in the first-tier cities are higher than those in Japan at the time. Does this mean that China's housing prices are too high? Will China's housing prices continue to grow? What are the factors related to China's housing prices? Is any economy bubble in China real estate? These questions are very attractive to me. Therefore, we want to study the relationships between housing prices and other factors in China's capital (one of the first-tier cities).

The raw data is collected by lianjia.com, the biggest housing agency in China.
All trade time was in January 2018. This dataset has 14 factors.

Factors:
[numerical - continuous] price: Housing price per squared meter(unit: ¥, RMB)
[numerical - continuous] square: The area of the apartment (unit: square meters).
[numerical - discrete] livingRoom: The number of living rooms.
[numerical - discrete] drawingRoom: The number of drawing rooms.
[numerical - discrete] kitchen: The number of kitchens.
[numerical - discrete] bathRoom: The number of bathrooms.
[numerical - discrete] floor: The number of the floor of the apartment.
[categorical - nominal] buildingType: including tower(1) , bungalow(2)，combination of plate and tower(3), and plate(4).
[numerical - discrete] constructionTime: the time of construction.
[categorical - nominal] renovationCondition: including other(1), rough(2),Simplicity(3), and hardcover(4)
[categorical - nominal] buildingStructure: including unknown(1), mixed(2), brick and wood(3), brick and concrete(4),steel(5) and steel-concrete composite (6).
[categorical - nominal] elevator: Is there an elevator?
[categorical - nominal] subway: Is there a subway nearby?
[categorical - nominal] district: District code of Beijing.

###################################
# Data Presentation - Danlin Shen #
###################################
plot_correlation is a function from "DataExplorer". It could create a correlation heatmap for all discrete categories and avoid the error caused by different scales. And we can find  out that some variable have strong relationships with other variables.

For example, the floor and the elevator, it means with the floor increase, there will be an elevator. Back to the price, I noticed that price may have strong relationships with constructionTime and subway.

```R
plot_correlation(bj.raw)
```

# R Shiny - Relationships in Beijing Housing Price of Each Variable - UI
bj_ui <- shinyUI(fluidPage(
  # Give the page a title
  titlePanel("Relationships in Beijing Housing Price of Each Variable"),
  
  sidebarLayout(
    sidebarPanel(
      
      radioButtons("select", label = "Select Variable vs. price:",
                  choices = c("price vs. square" = 1,
                              "average price vs. livingRoom" = 2,
                              "average price vs. drawingRoom" = 3,
                              "average price vs. kitchen" = 4,
                              "average price vs. bathRoom" = 5,
                              "average price vs. floor" = 6,
                              "average price vs. buildingType" = 7,
                              "average price vs. constructionTime" = 8,
                              "average price vs. renovationCondition" = 9,
                              "average price vs. buildingStructure" = 10,
                              "average price vs. elevator" = 11,
                              "average price vs. subway" = 12,
                              "average price vs. district" = 13),
                  selected = 1) # Default Selection
    ),   
    mainPanel(
      h3(textOutput("caption")),
      plotOutput("plot")
      
      
    )
  )
)
)

# R Shiny - Relationships in Beijing Housing Price of Each Variable - SERVER
bj_server <- shinyServer(function(input, output) {
  output$plot <- renderPlot({
    # price vs. square
    if(input$select == 1) {
      G <- ggplot(data = bj.raw, aes(x = square, y = price))+
        geom_point()+
        ggtitle("price vs. square")+
        ylim(0, 150000)+
        xlab("square")
        ylab("price")+
        ylim(0, 150000)
    }
    
    # average price vs. livingRoom
    if(input$select == 2) {
      bj_livingRoom <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$livingRoom),FUN = "mean")
      names(bj_livingRoom) = c("livingRoom", "averge price")
      
      G <- ggplot()+
        geom_point(data = bj_livingRoom, aes(x = livingRoom, y = `averge price`))+
        geom_line(data = bj_livingRoom, aes(x = livingRoom, y = `averge price`))+
        ggtitle("average price vs. livingRoom")+
        xlab("livingRoom")+
        ylab("average price")+
        ylim(0, 150000)
    }
    
    # average price vs. drawingRoom
    if(input$select == 3) {
      bj_drawingRoom <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$drawingRoom),FUN = "mean")
      names(bj_drawingRoom) = c("drawingRoom", "averge price")
      
      G <- ggplot()+
        geom_point(data = bj_drawingRoom, aes(x = drawingRoom, y = `averge price`))+
        geom_line(data = bj_drawingRoom, aes(x = drawingRoom, y = `averge price`))+
        ggtitle("average price vs. drawingRoom")+
        xlab("drawingRoom")+
        ylab("average price")+
        ylim(0, 150000)
    }
    
    
    # average price vs. kitchen
    if(input$select == 4) {
      bj_kitchen <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$kitchen),FUN = "mean")
      names(bj_kitchen) = c("kitchen", "averge price")
      
      G <- ggplot()+
        geom_point(data = bj_kitchen, aes(x = kitchen, y = `averge price`))+
        geom_line(data = bj_kitchen, aes(x = kitchen, y = `averge price`))+
        ggtitle("average price vs. kitchen")+
        xlab("kitchen")+
        ylab("average price")+
        ylim(0, 150000)
    }
    
    
    # average price vs. bathRoom
    if(input$select == 5) {
      bj_bathRoom <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$bathRoom),FUN = "mean")
      names(bj_bathRoom) = c("bathRoom", "averge price")
      
      G <- ggplot()+
        geom_point(data = bj_bathRoom, aes(x = bathRoom, y = `averge price`))+
        geom_line(data = bj_bathRoom, aes(x = bathRoom, y = `averge price`))+
        ggtitle("average price vs. bathRoom")+
        xlab("bathRoom")+
        ylab("average price")+
        ylim(0, 150000)
    }
    
    
    # average price vs. floor
    if(input$select == 6) {
      bj_floor <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$floor),FUN = "mean")
      names(bj_floor) = c("floor", "averge price")
      
      G <- ggplot()+
        geom_point(data = bj_floor, aes(x = floor, y = `averge price`))+
        geom_line(data = bj_floor, aes(x = floor, y = `averge price`))+
        ggtitle("average price vs. floor")+
        xlab("floor")+
        ylab("average price")+
        ylim(0, 150000)
    }
    
    
    # average price vs. buildingType
    if(input$select == 7) {
      bj_buildingType <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$buildingType),FUN = "mean")
      names(bj_buildingType) = c("buildingType", "averge price")
      
      G <- ggplot()+
        geom_point(data = bj_buildingType, aes(x = buildingType, y = `averge price`))+
        geom_line(data = bj_buildingType, aes(x = buildingType, y = `averge price`))+
        ggtitle("average price vs. buildingType")+
        xlab("buildingType")+
        ylab("average price")+
        ylim(0, 150000)
    }
    
    
    # average price vs. constructionTime
    if(input$select == 8) {
      bj_constructionTime <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$constructionTime),FUN = "mean")
      names(bj_constructionTime) = c("constructionTime", "averge price")
      
      G <- ggplot()+
        geom_point(data = bj_constructionTime, aes(x = constructionTime, y = `averge price`))+
        geom_line(data = bj_constructionTime, aes(x = constructionTime, y = `averge price`))+
        ggtitle("average price vs. constructionTime")+
        xlab("constructionTime")+
        ylab("average price")+
        ylim(0, 150000)
    }
    
    
    # average price vs. renovationCondition
    if(input$select == 9) {
      bj_renovationCondition <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$renovationCondition),FUN = "mean")
      names(bj_renovationCondition) = c("renovationCondition", "averge price")
      
      G <- ggplot()+
        geom_point(data = bj_renovationCondition, aes(x = renovationCondition, y = `averge price`))+
        geom_line(data = bj_renovationCondition, aes(x = renovationCondition, y = `averge price`))+
        ggtitle("average price vs. renovationCondition")+
        xlab("renovationCondition")+
        ylab("average price")+
        ylim(0, 150000)
    }
    
    
    # average price vs. buildingStructure
    if(input$select == 10) {
      bj_buildingStructure <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$buildingStructure),FUN = "mean")
      names(bj_buildingStructure) = c("buildingStructure", "averge price")
      
      G <- ggplot()+
        geom_point(data = bj_buildingStructure, aes(x = buildingStructure, y = `averge price`))+
        geom_line(data = bj_buildingStructure, aes(x = buildingStructure, y = `averge price`))+
        ggtitle("average price vs. buildingStructure")+
        xlab("buildingStructure")+
        ylab("average price")+
        ylim(0, 150000)
    }
    
    
    # average price vs. elevator
    if(input$select == 11) {
      bj_elevator <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$elevator),FUN = "mean")
      names(bj_elevator) = c("elevator", "averge price")
      
      G <- ggplot()+
        geom_point(data = bj_elevator, aes(x = elevator, y = `averge price`))+
        geom_line(data = bj_elevator, aes(x = elevator, y = `averge price`))+
        ggtitle("average price vs. elevator")+
        xlab("elevator")+
        ylab("average price")+
        ylim(0, 150000)
    }
    
    
    # average price vs. subway
    if(input$select == 12) {
      bj_subway <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$subway),FUN = "mean")
      names(bj_subway) = c("subway", "averge price")
      
      G <- ggplot()+
        geom_point(data = bj_subway, aes(x = subway, y = `averge price`))+
        geom_line(data = bj_subway, aes(x = subway, y = `averge price`))+
        ggtitle("average price vs. subway")+
        xlab("subway")+
        ylab("average price")+
        ylim(0, 150000)
    }
    
    
    # average price vs. district
    if(input$select == 13) {
      bj_district <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$district),FUN = "mean")
      names(bj_district) = c("district", "averge price")
      
      G <- ggplot()+
        geom_point(data = bj_district, aes(x = district, y = `averge price`))+
        geom_line(data = bj_district, aes(x = district, y = `averge price`))+
        ggtitle("average price vs. district")+
        xlab("district")+
        ylab("average price")+
        ylim(0, 150000)
    }
    plot(G)
  })
})

# And I also make a shiny app to analyze the average price and every other variable.
# Before making a hypothesis, we must understand that some variables are not
# ordinal data which means the magnitude of their value are meaningless.
# We can make a simple conclusion that price has some relationships with 
# kitchen, constructionTime, renovationCondition, buildingStructure, subways, and district.
shinyApp(bj_ui, bj_server)

####################################
# Data Preprocessing - Danlin Shen #
####################################
# 1. Convert all of the data: All of the matrix will be standardized to have unit L1 norm in each column and 
# zero mean. L1 norm is uesd for Lasso and descision tree.
bj.norm <- apply(bj.raw, 2, function(x) scale(x, center = T, scale = T)/norm(scale(x, center = T, scale = T), "1"))
# bj.norm is the data have been standardized to have unit L1 norm in each column and zero mean.

bj.raw <- read.csv("bj.csv")
bj.norm <- apply(bj.raw, 2, function(x) scale(x, center = T, scale = T)/norm(scale(x, center = T, scale = T), "1"))
head(bj.raw)
head(bj.norm)

# Exlanation & Testing
# Before we start a deep analysis, we have to preprocess the data -- if you don't, the data won't be on the 
# same scale. For example, in this program, we can't directly compare the relationships in the numbers of the 
# bathroom and the price per squared meter, because they have a huge difference
# in position and scale in the coordinate system. Therefore, through data preprocessing, we can put all of 
# the variables near the origin of the coordinate system without changing the data distribution. I will use z-mean 
# and L1 normalization.

sub.o <- bj.raw$subway
# Step 1 is to move the data to the origin.
sub.1<- sub.o - mean(sub.o)
# Step 2 is to compress the scale of the data to [0, 1].
sub.2 <- (sub.o - mean(sub.o))/(sd(sub.o))
sub.2/norm(as.matrix(sub.2), "1")
# Step 3, check data
head(sub.2/norm(as.matrix(sub.2), "1")) == head(as.data.frame(bj.norm)$subway)

# 2. Add the discription of the price
price <- bj.raw$price
# Find out the minmum, the 1st quantile, the median, the mean, the 3rd quantile.
summary(price) 

ggplot(data = bj.raw)+
  stat_boxplot(geom = "errorbar", width=0.15, aes(y = price))+
  geom_boxplot(mapping = aes(y = price))+
  ylim(0, 150000)

# We can notice that there are some points above the boxplot which are larger
# than the maximum of the boxplot(about 71,180) which actually are outliers.
# It may be caused by some policy of the Beijing government. Therefore, I set 71,180 as the luxury level.
# Description: Classify Beijing's house prices according to the price quartiles.

# Testing Code
for (i in 1:10) {
  if (price[i] < 42752) {cat(i, ":", price[i], "Poor","\n")}
  if (42752 <= price[i] & price[i]  < 54761) {cat(i, ":", price[i], "Cheap","\n")}
  if (54761 <= price[i] & price[i]  < 59666) {cat(i, ":", price[i], "Medium","\n")}
  if (59666 <= price[i] & price[i]  < 71180) {cat(i, ":", price[i], "Expensive","\n")}
  if (71180 <= price[i]) {cat(i, ":", price[i], "Luxary","\n")}
}

# Unlike Regression which tries to predict a continuous Y variable, in
# Classification we try to predict a categorical or a qualitative Y variable.
# Therefore, categorical data must be used as the y value. Since the raw
# data does not have categorical data, I use a piece of code to generate a description 
# as a label to describe the price.

bj.tree <- bj.raw
for (i in 1:nrow(bj.tree)) {
  if (bj.tree$price[i] < 42752) {bj.tree$Description[i] <- "Poor"}
  if (42752 <= bj.tree$price[i] & price[i]  < 54761) {bj.tree$Description[i] <- "Cheap"}
  if (54761 <= bj.tree$price[i] & price[i]  < 59666) {bj.tree$Description[i] <- "Medium"}
  if (59666 <= bj.tree$price[i] & price[i]  < 71180) {bj.tree$Description[i] <- "Expensive"}
  if (71180 <= bj.tree$price[i]) {bj.tree$Description[i] <- "Luxury"}
}

head(bj.tree) # bj.tree is the data that has extral label to dscribe the price


###############################
# Decision Tree - Danlin Shen #
###############################
# Generate Tree dataset
bj.norm <- as.data.frame(bj.norm)
Tree <- bj.norm
Tree$Description <- factor(bj.tree$Description) # Convert the Description from character to factor.
head(Tree)

# split into training and test bj.raws
set.seed(100) # set.seed(): Generate random numbers in a specific order for simple verification.
Tree.index <- sample(2, nrow(Tree), replace=TRUE, prob=c(0.7, 0.3))
Tree.train <- Tree[Tree.index==1, ]
Tree.test <- Tree[Tree.index==2, ]
str(Tree.train)
str(Tree.test)

# build a decision tree
Tree.formula <- Description ~ square + livingRoom + drawingRoom + kitchen + bathRoom + floor + buildingType + constructionTime + renovationCondition + buildingStructure + elevator + subway + district

Tree.ctree <- ctree(Tree.formula, data=Tree.train)
plot(Tree.ctree)

# predict on test data
pred <- predict(Tree.ctree, newdata = Tree.test) # check prediction result
table(pred, Tree.test$Description)

# Conclusion: From the statistical results, using the square, livingRoom, 
# drawingRoom, kitchen, bathRoom, floor, buildingType, constructionTime
# renovationCondition, buildingStructure, elevator, subway, and district
# could predict the range of the bj price. Therefore, if new data has
# the same characteristics as the decision tree model, the classificiation
# of price can be predicted.