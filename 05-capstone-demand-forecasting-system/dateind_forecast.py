# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:13:23 2020

@author: Arjun
"""
import dateutil.parser as parser
def dind(c,p):
 li=[]
 year = parser.parse(c).year
 if (year % 400 == 0):
     leap_year = True
 elif (year % 100 == 0):
     leap_year = False
 elif (year % 4 == 0):
     leap_year = True
 else:
     leap_year = False
 month = parser.parse(c).month
 if month in (1, 3, 5, 7, 8, 10, 12):
     month_length = 31
 elif month == 2:
     if leap_year:
         month_length = 29
     else:
         month_length = 28
 else:
     month_length = 30
 day = parser.parse(c).day
 for p in range(p):
     if day < month_length:
         day += 1
     else:
         day = 1
         if month == 12:
             month = 1
             year += 1
         else:
             month += 1
     pi=("%d-%d-%d" % (year, month,day))
     li.append(pi)
 return(li)