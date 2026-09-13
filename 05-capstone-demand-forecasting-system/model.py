# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 08:30:49 2019

@author: Arjun
"""
import pandas as pd

def fast(pf): 
    z=pf[['Item','Code']]
    a=pf['Item'].unique()
    item=[]
    for i in range (len(a)):   
     item.append(a[i])
    b=pf['Code'].unique()
    code=[]
    for i in range (len(b)):   
     code.append(b[i])
    df=pf
    #pf.sort_values(by=['Date'],inplace = True, ascending=True)
    # Give the item name
    print("\n The available items codes in the Restaurant are:\n",code)  
    search=input("\nEnter the item Code:")
    search=search.upper()
    # check whether the given code is matching
    for i in range (len(z)):
       if search == z.Code[i]:
            print("Your item is :",z.Item[i])
            break
    # BUG 1 if the code  is invalid ?
    # Filter and create a dataframe
    fltd_df= pf[pf.Code == search]
    t=fltd_df.Time_Stamp # time stamp of new df
    t_in=t.index #index values of time stamp
    time=[]
    for z in range (len(t_in)): # list of time stamp
        time.append(t[t_in[z]])
        
    # creating new column in data frame
    fltd_df.insert(4,'Time_cat',' ')
    for x in range(len(time)):
        if '10:00:00'< time[x] < '15:00:00':
                fltd_df.Time_cat[t_in[x]]='Till 3.P.M' 
        if '15:00:00'<time[x]<'18:00:00':
            fltd_df.Time_cat[t_in[x]]='3.P.M to 6.P.M'
        if '18:00:00'<time[x]<'21:00:00':
            fltd_df.Time_cat[t_in[x]]='6.P.M to 9.P.M'
        if '18:00:00'<time[x]<'24:00:00':
            fltd_df.Time_cat[t_in[x]]='9.P.M to 12.A.M'
        if '00:00:00'<time[x]<'03:00:00' :
            fltd_df.Time_cat[t_in[x]]='After 12 A.M'
    
    ##############################################  
            
      
        
    import matplotlib.pyplot as plt
    import seaborn as sns
    import math
    #plotting Mode
    
    fltd_df_1= fltd_df[['Mode','Quantity']]
    fltd_df_2=fltd_df_1.groupby('Mode')['Quantity'].sum().reset_index()
    mode_met=fltd_df_2.Mode.tolist()
    
    #Group  the data into Dine In and Take Away
    dinein = [s for s in mode_met if s.isdigit()]
    dineout=[d for d in mode_met if d.isalpha()]
    dinein_quant=[]
    dineout_quant=[]
    for i in range(len(dinein)):
        if fltd_df_2.Mode[i]== dinein[i]: 
            dinein_quant.append(fltd_df_2.Quantity[i])
    for i in range(len(dineout)):
        if fltd_df_2.Mode[len(dinein)+i]== dineout[i]: 
                dineout_quant.append(fltd_df_2.Quantity[len(dinein)+i]) 
    #dineIn          
    dinein_df=pd.DataFrame(list(zip(dinein,dinein_quant)),columns=['Table','Quantity'])
    #dineOut
    dineout_df=pd.DataFrame(list(zip(dineout,dineout_quant)),columns=['Table','Quantity'])
    
    #combined            
    tot_qn_t=sum(dinein_quant)
    tot_qn_ot=sum(dineout_quant)
    tot_df=[['Table',tot_qn_t],['OUT',tot_qn_ot]]
    fltd_co=pd.DataFrame(tot_df,columns=['Type','Number'])
    
    #plotting Quantity vs Date
    x=fltd_df['Date']
    y=fltd_df['Quantity']
    
    
    ##PLOTS
    #
    #
    #
    #plotting rent figure
    ax = plt.gca()
    # ylim max value to be setTime_cat
    sns.countplot(x='Time_cat',data= fltd_df)   
    # Set plotting style
    sns.set_style('whitegrid')
    # Rounding the integer to the next hundredth value plus an offset of 100
    def roundup(x):
        return  (int(math.ceil(x / 100.0)) * 100)
    # Get current axis on cur
    y_max = fltd_df['Time_cat'].value_counts().max() 
    ax.set_ylim([0, roundup(y_max)])
    # Iterate through the list of axes' patches
    for p in ax.patches:
        ax.text(p.get_x() + p.get_width()/2., p.get_height(), '%d' % int(p.get_height()), 
                fontsize=15, color='black', ha='center', va='bottom')
    
    #combined 
    fltd_co.plot(kind='bar',x='Type',y='Number')
    plt.suptitle('TOTAL_FOOD_SERVE', fontsize=20)
    plt.show()
    #dineIN
    dinein_df.plot(kind='bar',x='Table',y='Quantity')
    plt.suptitle('DINE_IN', fontsize=20)
    plt.show()
    #DINEOUT
    dineout_df.plot(kind='bar',x='Table',y='Quantity')
    plt.suptitle('DINE_OUT', fontsize=20)
    plt.show()
    #visualization WHOLE
    fltd_df_2.plot(kind='bar',x='Mode',y='Quantity') 
    plt.suptitle('FOOD_SERVE', fontsize=20)
    plt.show()
    
    #plotting Quantity vs Date
    plt.plot(x,y)
    plt.suptitle('Food_Consumed', fontsize=20)
    plt.show()
    
    import os
    cwd = os.getcwd()
    os.chdir("C:\\Users\\Arjun\\Documents\\Trimester 5\\DEMAND_ANALYSIS [ PY ]")
    ####################################################################
    ####################################################################
    fltd_df_3= fltd_df[['Date','Quantity']]
    date_qn=fltd_df_3.groupby('Date')['Quantity'].sum()
    date_qndf= date_qn.to_frame()
    prd=int(input("Enter  the forecast period in days: "))
    
    ############################# AUTO ARIMA ############################
    import forecast_arima_model_function as famf
    
    famf.lgraph(date_qn)
    famf.ac_plot(date_qndf)
    famf.adf_test(date_qn)
    famf.my_a_arima(date_qn,date_qndf,prd)
    #########################################################################
    
