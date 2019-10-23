################################################################################
# Title: ALY6070 - Module 4 Project - Danlin Shen.R                            #
# Created Date: June 20, 2019, 4:24:04 pm                                      #
# Author: Danlin Shen(shen.da@husky.neu.edu)                                   #
# Github: https://github.com/ZacksAmber/R                                      #
# Copyright (c) 2019 Danlin Shen                                               #
################################################################################

library(ggplot2)
library(shiny)

################
# Assignment 1 #
################
getwd()
setwd("/Users/zack/Desktop/Code/R/ALY 6070")

# Field Name	Field Description
# CLAIM_ID	Unique identifier for the insurance paid claims
# PATIENT_ID	De-identified ID for the patient
# PATIENT_STATE	The state in the USA where the patient currently resides
# PRODUCT_LINE	ACO includes Commercial and Medicare patients
# DATE_OF_SERVICE	The date of service on the insurance claim
# CPT_CODE	Current Procedural Terminology (CPT) code for the service rendered on the patient on the claim
# CPT_DESCRIPTION	Current Procedural Terminology (CPT) description for the service rendered on the patient on 
# the claim
# PROVIDER_NPI	Providers National Provider Identification (NPI) number, uniquely assigned to every provider 
# practicing medicine in the US
# PROVIDER_SPECIALTY	Providers specialty indicator
# TOTAL_PAID_BY_INSURANCE	Provider bills for service is typically split between the amount charged to insurance 
# and the rest is collected as copay from the patient. This field is the insurance paid amount.
# PATIENT_DEDUCTIBLE	Provider bills for service is typically split between the amount charged to insurance and 
# the rest is collected as deductible from the patient. This field is the patient paid deductible amount.

abc <- read.csv("ABC Healthcare Company Claims Dataset(1).csv")

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