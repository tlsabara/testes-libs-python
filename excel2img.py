import excel2img
#------------------------| Variaveis
srcXLSX = 'T:\\OPERAÇÕES\\asd\\01.RELATÓRIOS\\01.AGENTE\\R2-0001_Indicadores Agente.xlsx'
planREL = 'Quadros'
printScreen1 = 'Q:\\OPERAÇÕES\\asd\\01.RELATÓRIOS\\01.AGENTE\\R2-0001_Indicadores Agente_Lojas.bmp'
printScreen2 = 'S:\\OPERAÇÕES\\asd\\01.RELATÓRIOS\\01.AGENTE\\R2-0001_Indicadores Agente_Agentes.bmp'
print1 = 'A7:C22'
print1 = 'A24:C22'
#------------------------| Salvar Prints
excel2img.export_img(srcXLSX, printScreen1, planREL, print1)
excel2img.export_img(srcXLSX, printScreen2, planREL, print2)
# São 02 prints de um mesmo arquivo.
