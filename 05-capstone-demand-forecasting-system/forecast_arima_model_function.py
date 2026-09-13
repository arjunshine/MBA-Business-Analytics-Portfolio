# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 11:51:21 2020

@author: Arjun
"""
import pandas as pd
from pandas import datetime
import matplotlib.pyplot as plt
from matplotlib import pyplot         
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.arima_model import ARIMA
from pandas import DataFrame
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.stattools import adfuller 
from statsmodels.tsa.seasonal import seasonal_decompose
from numpy import log
import pmdarima as pm
from pmdarima import auto_arima
from math import sqrt
from sklearn.metrics import mean_squared_error
import dateind_forecast as difc

# MODEL 1

def lgraph(d_qn):
 #plotting the demand
 d_qn.plot(kind='line',x='Date',y='Quantity') 
 plt.suptitle('line_graph', fontsize=20)
 pyplot.show()

#auto correlation plot
def ac_plot(d_qndf):
 autocorrelation_plot(d_qndf)
 pyplot.show()
 
#check for stationarity
#adf test
def adf_test(d_qn):
 adf_test = adfuller(d_qn)
 print ("ADF = ",(adf_test[0]))
 print ("p-value = " ,(adf_test[1]))
 # if pvalue<0.05, we can  build the model
 if adf_test[1]>0.05:
     print("\nNOT STATIONARY\nTaking log\n")
     d_qn=log(d_qn)
     adf_test = adfuller(d_qn)
     print ("ADF = ",(adf_test[0]))
     print ("p-value = " ,(adf_test[1]))
 result = seasonal_decompose(d_qn, model='additive',freq=7)
 result.plot()
 pyplot.show()
 return(d_qn)   

def my_a_arima(d,df,p):
    l=len(d)
    test=df[l-p:l]
    #plotting the data
    #test.plot()
    #plt.show()
    model = auto_arima(d, trace=True, error_action='ignore', suppress_warnings=True)
    model.fit(d)
    forecast = model.predict(n_periods=p)
    d_in=difc.dind(d.index[l-1],p)
    d_in=pd.DataFrame(d_in,columns=['Date'])
    d_in.set_index('Date',inplace=True)
    forecast = pd.DataFrame(forecast,index=d_in.index,columns=['Prediction'])    
    #plot the predictions for validation set
    #print(d,'\nFORECAST:\n',forecast)
    #plt.plot(d, label='Date')
    #plt.show()
    plt.plot(forecast, label='Prediction')
    plt.show()    
    plt.plot(d)
    plt.plot(forecast)
    plt.show()
    #calculate rmse
    rms = sqrt(mean_squared_error(test,forecast))
    print("Error :",rms)
    f=0
    for q in range(len(forecast)):
        f=f+int(forecast.Prediction[q])
    print("Total forecast for a week:",int(f))
    print("Average forecast per day:",int(f/len(forecast)))    
    
'''

#divide into train and validation set

#train, test = date_qndf[0:70], date_qndf[70:74]
'''
