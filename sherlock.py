#!/usr/bin/env python

import pandas as pd 
import quandl as data


class Sherlock():

    def __init__(self):
        pass



    def GetSampleData(self, ticker):
        # ticker: "WIKI/GOOGL"
        self.data_frame = data.get(ticker)



    def PrintDataHead(self):
        print(self.data_frame.head())



    def PrintDataTail(self):
        print(self.data_frame.tail())



    def StripData(self):
        self.data_frame = self.data_frame[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]
        # now we just have the adjusted columns, and the volume column


    
    def CalculateNewColumnBasedOnCrudeVolatility(self, label):
        # use any calculation here, and replace with formula
        # a crude way of calculating volatility: high - low / low 
        self.data_frame[label] = (self.data_frame['Adj. High'] - self.data_frame['Adj. Low']) / self.data_frame['Adj. Close'] * 100.0



    def CalculateNewColumnBasedOnDailyPercentageChange(self, label):
        # use any calculation here, and replace with formula
        # a crude way of calculating volatility: high - low / low 
        self.data_frame[label] = (self.data_frame['Adj. Close'] - self.data_frame['Adj. Open']) / self.data_frame['Adj. Open'] * 100.0


    
    def DefineNewDataFrame(self):
        self.data_frame = self.data_frame
        



    
sherlock = Sherlock()
sherlock.GetSampleData("WIKI/GOOGL")
sherlock.PrintDataHead()
sherlock.StripData()

print('\n\nNow printing stripped data >>> >>>\n\n')
sherlock.PrintDataHead()

print('\n\nNow calculating new column based on volatility delta >>> >>>\n\n')
sherlock.CalculateNewColumnBasedOnCrudeVolatility('volatility delta')
sherlock.PrintDataHead()

print('\n\nNow calculating new column based on daily delta >>> >>>\n\n')
sherlock.CalculateNewColumnBasedOnDailyPercentageChange('daily delta')
sherlock.PrintDataHead()









