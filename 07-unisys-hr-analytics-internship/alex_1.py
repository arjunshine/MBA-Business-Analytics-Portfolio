# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:44:32 2019

@author: 
"""

import xlrd
import xlwt 
from xlwt import Workbook 
import os
# Workbook is created

directory =r"C:\Users\ShineArj\Documents\HEAT_MAP\DATA_BASE\New folder"
wb1 = Workbook()
array = []
for filename in os.listdir(directory):
    if filename.endswith(".xlsx"): 
        array.append(os.path.join(directory, filename))
#opening the workbook
val = 0
o = 0
sheet1 =wb1.add_sheet('Master',cell_overwrite_ok=True)
dum = 140
#index of the sheet you are working in
for excel in range(len(array)):
    if excel%8 == 0:
        wb1 = Workbook()
        sheet1 =wb1.add_sheet('Master',cell_overwrite_ok=True)
        val = 0
        o = 0
    o = val
    print(array[excel].split('\\')[len(array[excel].split('\\')) - 1].split('.xlsx')[0])
    wb = xlrd.open_workbook(array[excel])
    sheet = wb.sheet_by_index(1) #sheet = wb.sheet_by_index(z)
    array1 = []
    for w in range(1,len(sheet.row_values(0)),2):
        for y in range(1,6):
            sheet = wb.sheet_by_index(y) #sheet = wb.sheet_by_index(z)
            
            for t in range(int(13 * o),int((o + 1)*13)):
                if t%13 == 0:
                    t += 1
                
                sheet1.write(t,4,sheet.col_values(w)[int(t%13)])
                sheet1.write(t,0,array[excel].split('\\')[len(array[excel].split('\\')) - 1].split('.xlsx')[0])
                sheet1.write(t,1,sheet.col_values(w)[0])
                sheet1.write(t,3,sheet.col_values(0)[int(t%13)])
                sheet1.write(t,2,wb.sheet_names()[y].split(' (')[0])
            
            o += 1
    val += dum  
    wb1.save('xlwt example'+ str(int(excel/8)) + '.xls')
##open and read the file after the appending:








