import openpyxl as xl
import json
wb = xl.load_workbook('transactions.xlsx')
ws = wb.active
print(ws)
