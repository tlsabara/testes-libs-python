#Código localizado em um fórum.. não lembro qual
#modificado por Thiago Luca em 14/01/2022 - 22:12
#alterado novamente em 15/01/2022 - 16:30

from tkinter.tix import Tree


def eNumero(num):
    #função para verificar se a input é um numero.
     try:
         #Tentando converter o numero imputado. 
         float(num)
         
         #Se conseguir retorna true
         return True
         
     except:
         #Ignora qqr outra coisa
         pass
     
     #se tudo der errado ele retorna false
     return False
 
def not_eNumero(num): 
    #mesma coisa do codigo acima só que ao inverso.. rsrs... pra eu não usar o not
        
     try:
         float(num)
         return False
         
     except:
         pass
     return True
