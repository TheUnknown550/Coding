from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws['A2'].value = "Test"

wb.save('Python/3.9/Excel/Excels/NewExcel.xlsx')