getwd()
setwd("/Users/zack/Desktop/Code/R/ALY 6040")
bj.raw <- read.csv("bj.csv")

library(ggplot2)
library(shiny)

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
        ylab("average price")
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
        ylab("average price")
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
        ylab("average price")
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
        ylab("average price")
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
        ylab("average price")
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
        ylab("average price")
    }
    
    
    # average price vs. constructionTime
    if(input$select == 8) {
      bj_constructionTime <- aggregate.data.frame(bj.raw$price, by=list(bj.raw$constructionTime),FUN = "mean")
      names(bj_constructionTime) = c("constructionTime", "averge price")
      
      G <- ggplot()+
        geom_point(data = bj_constructionTime, aes(x = constructionTime, y = `averge price`))+
        geom_line(data = bj_constructionTime, aes(x = constructionTime, y = `averge price`))+
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
        ylab("average price")
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
        ylab("average price")
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
        ylab("average price")
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
        ylab("average price")
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

shinyApp(bj_ui, bj_server)

# plot_correlation could create a correlation heatmap for all discrete categories. And we can find out that some 
# variable has a strong relationship with other variable. For example, the floor and the elevator, it means with
# the floor increase, there will be a elevator. Back to the price, I notcie that price may have some relationships
# with constructionTime and subway. And I will analyze them in next step.
plot_correlation(bj.raw)


# We can make a simple conclusion