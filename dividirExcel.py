import pandas as pd

def idSet():
    if operadores < countOperador:
        countOperador = 1
        return 'OP'+str(countOperador)
    else:
        countOperador +=1
        return 'OP'+str(countOperador)
    
print('Olá! Bem vindo ao divisor de bases Cleitinho!')

srcFileCobmais = str(input('Caminho do arquivo do Cobmais (Tem que ser de contratos): '))
dstFolder = str(input('Digite aqui o caminho de saida dos arquivos: (Tem que ter a barra no final "\\"): '))

ExcelCobmais = pd.ExcelFile(srcFileCobmais)

df_Contratos = pd.read_excel(ExcelCobmais, sheet_name='Contratos')
df_Contratos['TOTAL ABERTO'] = df_Contratos['TOTAL ABERTO'].apply(lambda x: str(x).replace(',','.'))
df_Contratos['TOTAL ABERTO'] = df_Contratos['TOTAL ABERTO'].astype('float')
df_Contratos.sort_values(by=['TOTAL ABERTO'], inplace=True, ascending=False)
df_Contratos.insert(20,'Operador','')

linhaDf = len(df_Contratos.index)+1

operadores = int(input('Quantidade de operadores para dividir a base:  \n'))

partDf = int(linhaDf/operadores)


countOperador = 0

for i in df_Contratos.index:    
    if operadores <= countOperador:
        
        countOperador = 1
        df_Contratos.at[i,'Operador'] =  'OP'+str(countOperador)
    else:
        countOperador +=1
        df_Contratos.at[i,'Operador'] =  'OP'+str(countOperador)
        
listaOperadores = df_Contratos['Operador'].unique().tolist()
for i in listaOperadores:
    dstFolderTmp = dstFolder
    dfTmp = df_Contratos[df_Contratos.Operador == i]
    dstFolderTmp += i+'.xlsx'
    writer = pd.ExcelWriter(dstFolderTmp, engine='xlsxwriter')
    dfTmp.to_excel(writer, sheet_name='Sheet1',index = False)
    writer.save()
    writer.close()

print('Feito! Creitinho Soluções agradece a preferência!')
