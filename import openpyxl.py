import openpyxl as op

caminho = r'C:\Users\root_main\Desktop\01.xlsx'

excel = op.load_workbook(filename = caminho)
aba = excel['Plan1']

aba['B1'] = 10
aba['B10'] = 10
aba['B100'] = 10
aba['C1'] = 10
aba['C2'] = 10
aba['C3'] = 10

aba['A1'] = '=SUM(B:B,C1:C10)'

excel.save(filename = caminho)