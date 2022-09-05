import openpyxl

libro = openpyxl.Workbook()
hoja = libro.active

hoja['A1'] = 10
hoja['B1'] = 20
hoja['C1'] = 30
hoja['A2'] = 1000

libro.save('nuevo2.xlsx')