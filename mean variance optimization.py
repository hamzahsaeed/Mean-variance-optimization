# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 00:07:46 2021

@author: Hamzah
"""
import yfinance as yf
import xlsxwriter
import matplotlib.pyplot as plt
import pandas as pd
import xlrd
import os
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv
import scipy
import random
import itertools
import datetime
from datetime import date


# Directory for files
os.chdir(r"C:\Users\Hamzah\Documents\Python files")
wb = xlrd.open_workbook(r'C:\Users\Hamzah\Documents\Python files\NASDAQ_tickers.xls')

wb_tickers=wb.sheet_by_index(0)
N=wb_tickers.nrows
pd.set_option('display.max_columns', None)  

#create start and end dates
start_date="2020-01-01"
end_date="2020-12-10"

#Create tickers subset to create combinations
n_tickers=5
total_tickers=[]
for a in range(1,n_tickers+1):
    total_tickers.append(wb_tickers.row_values(a)[0])

market_data=pd.DataFrame()
for j in range(0,n_tickers):
    data=yf.download(total_tickers[j],start_date,end_date)
    market_data[total_tickers[j]]=data.Close

RMBK=market_data.dropna(axis=1)    

class portfolio_sd:
    def __init__(self,combo,RMBK,return_target):
        self.combo=combo
        self.RMBK=RMBK
        self.return_target=return_target
    def portfolio_return(self):
        ones_list=[]
        mean_returns=[]
        for x in range(0,len(combo)):
            ones_list.append(1)
            mean_returns.append((RMBK[combo[x]].iloc[-1]-RMBK[combo[x]].iloc[0])/RMBK[combo[x]].iloc[0])
        A=np.array([ones_list,mean_returns])
        b=np.array([[1],[self.return_target]])
        return A, b
    def portfolio_var(self):
        #Generate upper triangular
        data=pd.DataFrame()
        for ticker in combo:
            data[ticker]=RMBK[ticker]
        cov_m=np.triu(data.pct_change().cov().values)
        return cov_m
    def weights(self):
        A_matrix=self.portfolio_return()[0]
        b_matrix=self.portfolio_return()[1]
        sigma=self.portfolio_var()
        sigma_a=np.matmul(inv(sigma),A_matrix.transpose())
        a_sigma=np.matmul(A_matrix,sigma_a)
        a_sigma_b=np.matmul(inv(a_sigma),b_matrix)
        a_a_sigma_b=np.matmul(A_matrix.transpose(),a_sigma_b)
        weights=np.matmul(inv(sigma),a_a_sigma_b)
        return weights
    def sigma(self):
        sd=(self.stock_var()+self.cov())**(1/2)
        return sd
