#!/usr/bin/python
import xlrd as xd

data = xd.open_workbook("002.xls")
shrange  = range(data.nsheets);
sh = data.sheet_by_index(0)
nrows = sh.nrows;
ncols = sh.ncols
for i in range(1,nrows):

    print sh.row_values(i)[3]
# for j in  range(1,ncols):
#     print sh.col_values(j)[10]


