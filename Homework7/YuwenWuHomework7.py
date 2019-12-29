#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yuwen Wu Homework 7 (Individual Project)
@author: wuyuwen

This python document is wroten in Spyder. 
Hope professor could run it well.
If any run error unexpected in running process, I can response immediately 
as soon as been informed.

This py file is used to download several stock data from Yahoo Finance, 
and plot their trend of close price.
Also, This file could be used to input the ticker of stock name and response
the close price trend of one specific stock.
Additioanlly, This file also could calculate the days up and down in one year 
of specific stock.

The disadvantage of this file is that I only claw 10 stocks.

"""
# Import package

import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab


### Import data from Yahoo Finance

# Using String Data Type

start_date = '10/1/2006'
end_date = '10/1/2018'

# Using List 
stock = ['AAPL','MSFT','AMZN','GOOG','FB','C','JPM','BAC','HSBC','CIT']

# Using str[] function
IT = stock[0:5]
Bank = stock[5:10]

# Using Dictionary
itstockdata = {}

# Using for loop
for i in IT:
    itstockdata[i] = web.DataReader(i, data_source='yahoo', start = start_date, end = end_date)
    
bankstockdata = {}
for i in Bank:
    bankstockdata[i] = web.DataReader(i, data_source='yahoo', start = start_date, end = end_date)
    

### Check data
    
print(itstockdata)
print(bankstockdata)

### Ask user for stock search

# Using input
# Using list
# Using while / if / else
# Using pylab package plot time series picture
Check = input("Do you want to search IT stock?(y or n)\n>>")
ans = ['y','yes','ok','Y']
while Check in ans:
    stock_search = input(" Which IT stock you want to search? \n>>")
    if stock_search in stock:
        pylab.plot(itstockdata[stock_search]["Adj Close"],label=[stock_search],linewidth = 1.5)
        pylab.ylabel('Close Price')
        pylab.xlabel('Date')
        pylab.title('Stock Price of '+stock_search+' Stocks')
        pylab.plot(grid = True) 
        pylab.legend()
        plt.show()
        check = input('Do you want to search continue?(y or n)\n>>')
        if check not in ans:
            break
        else:
            continue
    else:
        print ("This stock is not in our database, Please Enter Again")
    
else:
    print("Thanks!")

### Plot close price of total IT data downloaded to check the trend of IT stock

# Using for loop

for i in range(5):
    pylab.plot(itstockdata[IT[i]]["Adj Close"],label=IT[i],linewidth = 1.5)
    
### Using pylab to plot picture and give label, title, legend to plot 
    
pylab.ylabel('Close Price')
pylab.xlabel('Date')
pylab.title('Stock Price of IT Stocks')
pylab.plot(grid = True) 
pylab.legend()
plt.show()

### plot the close price of Bank data 

for i in range(5):
    pylab.plot(bankstockdata[Bank[i]]["Adj Close"],label=Bank[i],linewidth = 1.5)
    
pylab.ylabel('Close Price')
pylab.xlabel('Date')
pylab.title('Stock Price of IT Stocks')
pylab.plot(grid = True) 
pylab.legend()
plt.show()


### calculate day up and day down in each year of each stock in stock list

### Since the Facebook stock price data begins from 2012, I adjusted code to begin from 2012

# Write function
def Day_Up_Down(name):
    # Using for loop 
    for i in range(2012,2018):
        j=str(i)
        sumUp = 0
        sumDown = 0
        df_year = itstockdata[name][j]
        # The following code came from CISC Financial Programming Course Slide
        S_i=df_year['Adj Close']
        S_i_minus_1 = df_year['Adj Close'].shift(1)
        stockReturn= np.log(S_i/S_i_minus_1)     
        length=stockReturn.shape[0]
        # End of code from CISC Financial Programming Course Slide
        # Using for loop
        for n in range(0, length):
             if(stockReturn[n]>0):
                 sumUp += 1
             if (stockReturn[n]<0):
                 sumDown += 1

        print(name, "has", sumUp, "days up and", sumDown, "days down in year ",i, "\n")
        i=i+1
        # End of for loop
        
# Using for loop
for i in IT:
    Day_Up_Down(i)
    
### Since the city bank data begins from 2009, I adjust the code from 2009
    
# Write function
def Day_Up_Down(name):
    for i in range(2009,2018):
        j=str(i)
        sumUp = 0
        sumDown = 0
        df_year = bankstockdata[name][j]
        # The following code came from CISC Financial Programming Course Slide
        S_i=df_year['Adj Close']
        S_i_minus_1 = df_year['Adj Close'].shift(1)
        stockReturn= np.log(S_i/S_i_minus_1) 
        length=stockReturn.shape[0]
        # End of code from CISC Financial Programming Course Slide
        for n in range(0, length):
             if(stockReturn[n]>0):
                 sumUp += 1
             if (stockReturn[n]<0):
                 sumDown += 1

        print(name, "has", sumUp, "days up and", sumDown, "days down in year ",i, "\n")
        i=i+1
        
        
for j in Bank:
    Day_Up_Down(j)
    
    
## if we want to store all stock name into txt document 
## some errors would occured  

### Store stock name to txt document
    
newFile = open(r'Stock Name List.txt', 'w',encoding='utf8')

try:
    newFile.write(stock)
except TypeError:
    print('write() argument must be str, not list')
finally :
    newFile.close()
    
## Therefore  we use pandas package to write data to csv document
## Write data to csv document
## Write file
aapl = pd.DataFrame(itstockdata['AAPL'])  
aapl.to_csv('AAPL.csv')

## If we want to find the end price of AAPL during this period 
# Using while loop 
# Reading file
with open(r'AAPL.csv', 'r', encoding='utf8') as file:
    line = file.readline().replace('\n', '')
    while line != '':
        line = file.readline().replace('\n', '')
        lineList = line.split(',')
        print(lineList[4:5])
## All document are wroten and stored in the same path of this py document.



    






