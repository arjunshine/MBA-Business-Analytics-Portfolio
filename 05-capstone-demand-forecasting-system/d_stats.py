# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 02:53:48 2020

@author: Arjun
"""

import statistics as st
column_names=pf.columns
print(column_names[0],'means :',st.mean(pf[column_names[0]]))
print(column_names[0],'median :',st.median(pf[column_names[0]]))
print(column_names[0],'variance :',st.variance(pf[column_names[0]]))
print(column_names[0],'population std dev :',st.pstdev(pf[column_names[0]]))
print(column_names[0],'std dev :',st.stdev(pf[column_names[0]]))

print(column_names[5],'means :',st.mean(pf[column_names[5]]))
print(column_names[5],'median :',st.median(pf[column_names[5]]))
print(column_names[5],'variance :',st.variance(pf[column_names[5]]))
print(column_names[5],'population std dev :',st.pstdev(pf[column_names[5]]))
print(column_names[5],'std dev :',st.stdev(pf[column_names[5]]))

print(column_names[6],'means :',st.mean(pf[column_names[6]]))
print(column_names[6],'median :',st.median(pf[column_names[6]]))
print(column_names[6],'variance :',st.variance(pf[column_names[6]]))
print(column_names[6],'population std dev :',st.pstdev(pf[column_names[6]]))
print(column_names[6],'std dev :',st.stdev(pf[column_names[6]]))




for i in range(len(column_names)):
    print(column_names[i],'means',st.mean(pf[column_names[i]]))