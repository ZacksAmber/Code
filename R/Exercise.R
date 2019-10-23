################################################################################
# Title: Exercise.R                                                            #
# Created Date: May 27, 2019, 4:38:44 am                                       #
# Author: Danlin Shen(shen.da@husky.neu.edu)                                   #
# Copyright (c) 2019 Danlin Shen                                               #
################################################################################

install.packages("NLP")
install.packages("tm")
library(tm)



install.packages("ggplot") 

print("Hello World")

x <- c(3, 2, 4)
y <- c(1, 2)

class(x)
class(y)
sort(x)

z <- NA
class(z)

class(x + z)
x + z

d <- "hhh"
class(d)
class(x)

f <- 5
class(f)
class(d+f)

df <- paste(d, f)
class(df)
fz <- paste(f, z)
class(fz)
fz
x
sort.data(x)
Order(x)

sort(x)

emp_age = 1
Emp_sal <- 2000 + 2.5*(emp_age)*2
class(Emp_sal)

a.list <- list(letters[1:3]) # contains "a", "b", "c"
another.list <- list(1:5) # contains 1,2,3,4,5
still.another.list <- list(TRUE,FALSE,TRUE)
I.am.a.list <- list(a.list,another.list,still.another.list)

I.am.a.list
sss <- unlist(I.am.a.list)
class(sss)
unlist(I.am.a.list, recursive = FALSE)

5:9
x <- list(c(5:8))
x
rm(x)
x[1] * c(1, 2, 3, 4)
x[[1]]
v <- c(1, 2, 3, 4)
v[2]

# shiny
library("shiny")
runExample("01_hello")
runExample("02_text")
runExample("03_reactivity")

library(shiny)

# Define UI for miles per gallon app ----
ui <- pageWithSidebar(
  
  # App title ----
  headerPanel("Miles Per Gallon"),
  
  # Sidebar panel for inputs ----
  sidebarPanel(),
  
  # Main panel for displaying outputs ----
  mainPanel()
)

# Define server logic to plot various variables against mpg ----
server <- function(input, output) {
  
}

shinyApp(ui, server)

# Define UI for miles per gallon app ----
ui <- fluidPage(

  # App title ----
  titlePanel("Miles Per Gallon"),

  # Sidebar layout with input and output definitions ----
  sidebarLayout(

    # Sidebar panel for inputs ----
    sidebarPanel(

      # Input: Selector for variable to plot against mpg ----
      selectInput("variable", "Variable:",
                  c("Cylinders" = "cyl",
                    "Transmission" = "am",
                    "Gears" = "gear")),

      # Input: Checkbox for whether outliers should be included ----
      checkboxInput("outliers", "Show outliers", TRUE)

    ),

    # Main panel for displaying outputs ----
    mainPanel(

      # Output: Formatted text for caption ----
      h3(textOutput("caption")),

      # Output: Plot of the requested variable against mpg ----
      plotOutput("mpgPlot")

    )
  )
)

# Data pre-processing ----
# Tweak the "am" variable to have nicer factor labels -- since this
# doesn't rely on any user inputs, we can do this once at startup
# and then use the value throughout the lifetime of the app
mpgData <- mtcars
mpgData$am <- factor(mpgData$am, labels = c("Automatic", "Manual"))

# Define server logic to plot various variables against mpg ----
server <- function(input, output) {

  # Compute the formula text ----
  # This is in a reactive expression since it is shared by the
  # output$caption and output$mpgPlot functions
  formulaText <- reactive({
    paste("mpg ~", input$variable)
  })

  # Return the formula text for printing as a caption ----
  output$caption <- renderText({
    formulaText()
  })

  # Generate a plot of the requested variable against mpg ----
  # and only exclude outliers if requested
  output$mpgPlot <- renderPlot({
    boxplot(as.formula(formulaText()),
            data = mpgData,
            outline = input$outliers,
            col = "#75AADB", pch = 19)
  })

}

shinyApp(ui, server)

# Drawing histograms for iris dataset in R using Shiny
#UI.R
library(shiny)
shinyUI(fluidPage(
  titlePanel("Iris Dataset"),
  sidebarLayout(
    sidebarPanel(
      radioButtons("p", "Select column of iris dataset:",
                   list("Sepal.Length"='a', "Sepal.Width"='b', "Petal.Length"='c', "Petal.Width"='d')),
      sliderInput("bins",
                  "Number of bins:",
                  min = 1,
                  max = 50,
                  value = 30)
    ),
    mainPanel(
      plotOutput("distPlot")
    )
  )
))

#SERVER.R
library(shiny)
shinyServer(function(input, output) {
  output$distPlot <- renderPlot({
    if(input$p=='a'){
      i<-1
    }

    if(input$p=='b'){
      i<-2
    }

    if(input$p=='c'){
      i<-3
    }

    if(input$p=='d'){
      i<-4
    }

    x    <- iris[, i]

    bins <- seq(min(x), max(x), length.out = input$bins + 1)
    hist(x, breaks = bins, col = 'darkgray', border = 'white')
  })
})

shinyApp(ui, server)

sidebarPanel:
- radioButtons
- sliderInput
- selectInput
- textInput

#UI.R
#loading shiny
library(shiny)

ui <- shinyUI(fluidPage(
  titlePanel("Loan Prediction III"),
  sidebarLayout(
    sidebarPanel(
      #input using radiobuttons
      radioButtons("s", "Select X-axis:",
                   list("Loan_ID"='a', "Gender"='b', "Married"='c', "Dependents"='d',"Education"='e', "Self_Employed"='f', "ApplicantIncome"='g', "CoapplicantIncome"='h', "LoanAmount"='i', "Loan_Amount_Term"='j', "Credit_History"='k', "Property_Area"='l', "Loan_Status"='m'))
    ),   

# Show a plot of the generated distribution
      mainPanel(
        plotOutput("distPlot")
    )
    )
  ))

#SERVER.R
library(shiny)

#loading shiny
server <- shinyServer(function(input, output) {

#writing server function
  output$distPlot <- renderPlot({

#creating distPlot
    if(input$s=='a') { i<-1 }
    if(input$s=='b') { i<-2 }
    if(input$s=='c') { i<-3 }
    if(input$s=='d') { i<-4 }
    if(input$s=='e') { i<-5 }
    if(input$s=='f') { i<-6 }
    if(input$s=='g') { i<-7 }
    if(input$s=='h') { i<-8 }
    if(input$s=='i') { i<-9 }
    if(input$s=='j') { i<-10 }
    if(input$s=='k') { i<-11 }
    if(input$s=='l') { i<-12 }
    if(input$s=='m') { i<-13 }
  
    #reading training dataset
    train<-read.csv("train_u6lujuX_CVtuZ9i.csv")
    X    <- train[, i]
    plot(X)
  })
})

shinyApp(ui, server)


########## 6040 Final
library(ggplot2)
library(shiny)

# Load data
getwd()
setwd("/Users/zack/Desktop/Code/R/ALY 6040")
bj.raw <- read.csv("bj.csv")

# price vs. square
ggplot(data = bj.raw, aes(x = square, y = price))+
geom_point()+
ylim(0, 150000)


# average price vs. livingRoom
bj_livingRoom <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$livingRoom),FUN = "mean")
names(bj_livingRoom) = c("livingRoom", "averge price")
ggplot()+
geom_point(data = bj_livingRoom, aes(x = livingRoom, y = `averge price`))+
geom_line(data = bj_livingRoom, aes(x = livingRoom, y = `averge price`))+
ggtitle("average price vs. livingRoom")+
xlab("livingRoom")+
ylab("average price")

# average price vs. drawingRoom
bj_drawingRoom <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$drawingRoom),FUN = "mean")
names(bj_drawingRoom) = c("drawingRoom", "averge price")
ggplot()+
geom_point(data = bj_drawingRoom, aes(x = drawingRoom, y = `averge price`))+
geom_line(data = bj_drawingRoom, aes(x = drawingRoom, y = `averge price`))+
ggtitle("average price vs. drawingRoom")+
xlab("drawingRoom")+
ylab("average price")

# average price vs. kitchen
bj_kitchen <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$kitchen),FUN = "mean")
names(bj_kitchen) = c("kitchen", "averge price")
ggplot()+
geom_point(data = bj_kitchen, aes(x = kitchen, y = `averge price`))+
geom_line(data = bj_kitchen, aes(x = kitchen, y = `averge price`))+
ggtitle("average price vs. kitchen")+
xlab("kitchen")+
ylab("average price")

# average price vs. bathRoom
bj_bathRoom <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$bathRoom),FUN = "mean")
names(bj_bathRoom) = c("bathRoom", "averge price")
ggplot()+
geom_point(data = bj_bathRoom, aes(x = bathRoom, y = `averge price`))+
geom_line(data = bj_bathRoom, aes(x = bathRoom, y = `averge price`))+
ggtitle("average price vs. bathRoom")+
xlab("bathRoom")+
ylab("average price")

# average price vs. floor
bj_floor <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$floor),FUN = "mean")
names(bj_floor) = c("floor", "averge price")
ggplot()+
geom_point(data = bj_floor, aes(x = floor, y = `averge price`))+
geom_line(data = bj_floor, aes(x = floor, y = `averge price`))+
ggtitle("average price vs. floor")+
xlab("floor")+
ylab("average price")

# average price vs. buildingType
bj_buildingType <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$buildingType),FUN = "mean")
names(bj_buildingType) = c("buildingType", "averge price")
ggplot()+
geom_point(data = bj_buildingType, aes(x = buildingType, y = `averge price`))+
geom_line(data = bj_buildingType, aes(x = buildingType, y = `averge price`))+
ggtitle("average price vs. buildingType")+
xlab("buildingType")+
ylab("average price")

# average price vs. constructionTime
bj_constructionTime <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$constructionTime),FUN = "mean")
names(bj_constructionTime) = c("constructionTime", "averge price")
ggplot()+
geom_point(data = bj_constructionTime, aes(x = constructionTime, y = `averge price`))+
geom_line(data = bj_constructionTime, aes(x = constructionTime, y = `averge price`))+
xlab("constructionTime")+
ylab("average price")+
ylim(0, 150000)

# average price vs. renovationCondition
bj_renovationCondition <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$renovationCondition),FUN = "mean")
names(bj_renovationCondition) = c("renovationCondition", "averge price")
ggplot()+
geom_point(data = bj_renovationCondition, aes(x = renovationCondition, y = `averge price`))+
geom_line(data = bj_renovationCondition, aes(x = renovationCondition, y = `averge price`))+
ggtitle("average price vs. renovationCondition")+
xlab("renovationCondition")+
ylab("average price")

# average price vs. buildingStructure
bj_buildingStructure <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$buildingStructure),FUN = "mean")
names(bj_buildingStructure) = c("buildingStructure", "averge price")
ggplot()+
geom_point(data = bj_buildingStructure, aes(x = buildingStructure, y = `averge price`))+
geom_line(data = bj_buildingStructure, aes(x = buildingStructure, y = `averge price`))+
ggtitle("average price vs. buildingStructure")+
xlab("buildingStructure")+
ylab("average price")

# average price vs. elevator
bj_elevator <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$elevator),FUN = "mean")
names(bj_elevator) = c("elevator", "averge price")
ggplot()+
geom_point(data = bj_elevator, aes(x = elevator, y = `averge price`))+
geom_line(data = bj_elevator, aes(x = elevator, y = `averge price`))+
ggtitle("average price vs. elevator")+
xlab("elevator")+
ylab("average price")

# average price vs. subway
bj_subway <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$subway),FUN = "mean")
names(bj_subway) = c("subway", "averge price")
ggplot()+
geom_point(data = bj_subway, aes(x = subway, y = `averge price`))+
geom_line(data = bj_subway, aes(x = subway, y = `averge price`))+
ggtitle("average price vs. subway")+
xlab("subway")+
ylab("average price")

# average price vs. district
bj_district <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$district),FUN = "mean")
names(bj_district) = c("district", "averge price")
ggplot()+
geom_point(data = bj_district, aes(x = district, y = `averge price`))+
geom_line(data = bj_district, aes(x = district, y = `averge price`))+
ggtitle("average price vs. district")+
xlab("district")+
ylab("average price")+
ylim(0, 150000)













# R Shiny - ABC Healthcare Company Claims Dataset - UI
abc_ui <- shinyUI(fluidPage(
  titlePanel("Dynamic Chart of ABC Healthcare Company Claims Dataset"),
  sidebarLayout(
    sidebarPanel(
      # Provide two options for showing different types of chart
      radioButtons("s", "Select Metric Type of Chart:",
                  list("Total Paid by Insurance" = 'a',
                  "Total Paid by Insurance on the y axis, vs. Patient’s Deductible on the x axis. " = 'b'))
    ),
    mainPanel(
      h3(textOutput("caption")),
      plotOutput("plot")
    )
  )
))

# R Shiny - ABC Healthcare Company Claims Dataset - SERVER
abc_server <- shinyServer(function(input, output) {
      output$plot <- renderPlot({
        # Bar chart
        if(input$s=='a') {
            abc_sum <- aggregate.data.frame(abc$TOTAL_PAID_BY_INSURANCE, by=list(abc$PROVIDER_SPECIALTY),FUN = "sum")
            names(abc_sum) = c("Provider Specialty", "Total Paid by Insurance")
            m <- abc_sum$`Provider Specialty`
            n <- abc_sum$`Total Paid by Insurance`
        
            # G is varible to transfer the option from user
            G <- ggplot(abc_sum, mapping = aes(x = reorder(m, n), y = n))+
                geom_bar(stat = 'identity')+
                xlab("Provider Specialty")+
                ylab("The Sum of Total Paid by Insurance by Provider Specialty")+
                expand_limits(y = seq(0, 140000, by = 20000))+
                coord_flip()
        }
        
        # Scatter plot
        if(input$s=='b') {
            # G is varible to transfer the option from user
            G <- ggplot(data = abc)+
            geom_point(mapping = aes(x = PATIENT_DEDUCTIBLE, y = TOTAL_PAID_BY_INSURANCE, color = PROVIDER_SPECIALTY, size = TOTAL_PAID_BY_INSURANCE))+
            xlab("Patient Deductible")+
            ylab("Total Paid by Insurance")+
            ggtitle("Total Paid by Insurance on the y axis, vs. Patient’s Deductible on the x axis. ")
        }

        plot(G)
  })
})

shinyApp(abc_ui, abc_server)

################
# Assignment 2 #
################
getwd()
# setwd("/Users/zack/Desktop/Code/R/ALY 6070")

d <- read.csv("Global Superstore Orders 2016(1).csv")

# R Shiny - Global Superstore Orders 2016 - UI
d_ui <- shinyUI(fluidPage(    
  # Give the page a title
  titlePanel("Global Superstore Orders 2016"),
  
  sidebarLayout(
    sidebarPanel(
      
      selectInput("select", label = "Select type of chart:",
                  choices = c("The Sum of Total Paid by Insurance by Provider Specialty" = 1,
                              "Sum of Quantity Ordered by Category by Year" = 2),
                  selected = 1) # Default Selection
    ),   
    mainPanel(
      h3(textOutput("caption")),
      plotOutput("plot")
      
      
    )
  )
)
)

# R Shiny - Global Superstore Orders 2016 - SERVER
d_server <- shinyServer(function(input, output) {
  output$plot <- renderPlot({
    # Bar chart
    if(input$select == 1) {
      # Get the sum of sales by market
      dsum <- aggregate.data.frame(d$Sales,by=list(d$Market),FUN = "sum")
      
      # Name the columnes
      names(dsum) = c("Market", "Total Sales")
      
      m <- dsum$Market
      n <- dsum$`Total Sales`
      G <- ggplot(dsum, mapping = aes(x = reorder(m, n), y = n))+
        geom_bar(stat = 'identity')+
        xlab("Provider Specialty")+
        ylab("The Sum of Total Paid by Insurance by Provider Specialty")+
        coord_flip()
    }
    
    # Scatter plot
    if(input$select == 2) {
      dsum3 <- aggregate.data.frame(d$Sales,by=list(d$Category,d$Order.Year),FUN = "sum")
      names(dsum3) = c("Category","Order.Year","Total.Sales")
      
      G <- ggplot(data = dsum3, aes(x = Order.Year, y = Total.Sales, group = Category))+
        geom_point(aes(color = Category))+
        geom_line(aes(color = Category))+
        ggtitle("Sum of Quantity Ordered by Category by Year")+
        xlab("Year")+
        ylab("Sum of Quantity")
    }
    
    plot(G)
  })
})

shinyApp(d_ui, d_server)