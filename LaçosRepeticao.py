#Programa de teste de numeros primos v1.0
#sBking
#17/12/2021

def testaPrimo(a):
    verific = 0
    for x in range(1,a+1):
        resto = a % x
        if resto == 0:
            verific = verific+1
        #print('Divisao por: {}, resultado: {}'.format(x,resto))
    if verific == 2:
        print('o numero {} é primo.'.format(a))
        primo = 1
    else:
        print('o Numero {} não é primo.'.format(a))
        primo = 0
    return primo

vQtdPrimos = 0

vNum = int(input('Digite o numero desejado:'))

for z in range(1,vNum):
    vQtdPrimos = vQtdPrimos + testaPrimo(z)


print('.')
print('No intervalo selecionado é um total de: {} numero(s) primo(s)'.format(vQtdPrimos))
print('Fim do código..........')
