#!/usr/bin/python

import csv
import xlrd
import os

# runs the csv_from_excel function:
def csv_from_excel(x,y):
    wb = xlrd.open_workbook(x)
    sh = wb.sheet_by_name('Data')
    your_csv_file = open(y, 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))


files = os.listdir('/root/converter/xlrd2csv/excel_files/')
i=1
for file in files:
    x="excel_files/"+file
    z=file.split('.')
    y="aditi/"+z[0]+".csv"
    csv_from_excel(x,y)
    print i, "file converted to csv..."
    i=i+1

