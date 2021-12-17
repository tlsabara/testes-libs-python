#programa de controle de notas
#sbKing 16/12/2021 23:48
#v1.0

print('---| PROGRAMA DE CONTROLE DE NOTAS - 1.0 |---')

#Função para inserir e verificar a nota
def insertNota(a):
    vNotaInformada = float(input('Digite a nota {}: '.format(a)))
    while vNotaInformada < 0 or vNotaInformada > 10:
        print('Nota fora dos parametros!!!')
        vNotaInformada = float(input('A nota precisa estar entre 0 e 10: '.format(a)))
    print('Nota inserida!!')
    return vNotaInformada

#load das notas
vNota1 = insertNota(1)
vNota2 = insertNota(2)
vNota3 = insertNota(3)
vNota4 = insertNota(4)

#parametros de peso das notas
#deixei todas as notas com o mesmo peso.
vPesoN1 = 2.5
vPesoN2 = 2.5
vPesoN3 = 2.5
vPesoN4 = 2.5

#Cálculo das notas
vNota1 = vNota1 * vPesoN1
vNota2 = vNota2 * vPesoN2
vNota3 = vNota3 * vPesoN3
vNota4 = vNota4 * vPesoN4

#Cálculo da nota final
vNotaFinal = (vNota1 + vNota2 + vNota3 + vNota4)/(vPesoN1 + vPesoN2 + vPesoN3 + vPesoN4)

#retorno na tela para o usuário
print('A nota final foi de: {}'.format(vNotaFinal))

#apresentação se o aluno foi aprovado ou não
if vNotaFinal < 6:
    print('A nota é insuficiente, aluno reprovado!!!')
else:
    print('Nota mínima de aprovação atingida, aluno aprovado!')

print('!--- FIM DO PROGRAMA ---!')
