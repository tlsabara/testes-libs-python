#Testando métodos
#Writed by sbKing
#14/01/22 - 23:48

from time import sleep #pra que isso???????
import verificadorNumeros #um outro método meu apenas para validar as entradas usando o input

#Classe Televisao onde suas funções são botões.
class ClasseTelevisao:
    def __init__(self,marca, modelo, maxVol, numCanais):
       self.statusTV = False;
       self.statusVolume = 0;
       self.statusCanal = 1;
       self.volumeMute = 0;
       self.volumeMaximo = maxVol;
       self.canalMaximo = numCanais;
       self.marcaTV = marca;
       self.modeloTV = modelo;
    
    #Botão para ligar e desligar a TV
    def btnPower(self):
        if self.statusTV == False:
            self.statusTV = True;
        else:
            self.statusTV = False;
    
    #Botão para aumentar o volume da TV
    def btnVolMais(self):
        if self.statusVolume < self.volumeMaximo:
            self.statusVolume +=1;
        else:
            print("volume max atingido!"); 
    
    #Botão para abaixar o volume da TV
    def btnVolMenos(self):
        if self.statusVolume > 0:
            self.statusVolume -=1;
        else:
            print("volume min atingido!"); 
    
    #Botão para avançar um canal
    def btnCanalMais(self):
        if self.statusCanal < self.canalMaximo:
            self.statusCanal +=1;
            print("CH atual: {}".format(self.statusCanal));
        else:
            print("Canal max atingido! CH atual: {}".format(self.statusCanal)); 
        
    #Botão para voltar um canal
    def btnCanalMenos(self):
        if self.statusCanal > 1:
            self.statusCanal -=1;
            print("CH atual: {}".format(self.statusCanal));
        else:
            print("Canal min atingido! CH atual: {}".format(self.statusCanal)); 
    
    #Botão para ir para um canal específico
    def btnCH(self):
        a = input('Digite o numero do CH: ');
        while verificadorNumeros.not_eNumero(a):
            a = input('Precisa ser um numero! Digite:');
        
        if a < self.canalMaximo:
            self.statusCanal = a;
            print("CH atual: {}".format(self.statusCanal));    
        else:
            print("Canal informado além do max permitido! CH atual: {}".format(self.statusCanal));
        
    
    #Botão para mutar a TV
    def btnMute(self):
        if self.statusVolume > 0:
            self.volumeMute = self.statusVolume
            self.statusVolume = 0
            print('A tv foi mutada!');
        else:
            self.statusVolume = self.volumeMute
    
    #coleta e printa o status da TV
    def statusdaTV(self):
        print('Marca: {}'.format(self.marcaTV));
        print('Modelo: {}'.format(self.modeloTV));
        if  self.statusTV == True: 
            print('A TV está ligada.')
            print('CH atual: {}'.format(self.statusCanal));
            print('Vol atual: {}'.format(self.statusVolume));
        else:
            print('A tv está desligada');
        

        
        
