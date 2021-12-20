
class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
        self.volume = 10
        self.maxVolume = 30
        self.maxCanal = 15

    def btn_power(self):
        if self.ligada == True:
            self.ligada = False
            print('A tv foi desligada')
        else:
            self.ligada = True
            print('A tv foi ligada')
    
    def btn_maisCanal(self):
        if self.ligada == True:
            if self.canal <= self.maxCanal and self.canal > 0:
                self.canal = self.canal+1
            else:
                print('Limite atingido!')
        else:
            print('A tv esta desligada')
    
    def btn_menosCanal(self):
        if self.ligada == True:
            if self.canal <= self.maxCanal and self.canal > 0:
                self.canal = self.canal-1
            else:
                print('Limite atingido!')
        else:
            print('A tv esta desligada')

    def btn_menosVolume(self):
        if self.ligada == True:
            if self.canal <= self.maxCanal and self.canal > 0:
                self.volume = self.volume -1
            else:
                print('Limite atingido!')
        else:
            print('A tv esta desligada')
    
    def btn_maisVolume(self):
        if self.ligada == True:
            if self.canal <= self.maxCanal and self.canal > 0:
                self.volume = self.volume +1
            else:
                print('Limite atingido!')
        else:
            print('A tv esta desligada')

tv = Televisao()

menu = 9

while menu != 0:
    menu = int(input(
        'Digite o numero do botão:\n - 1. Botão power\n - 2. Botão volume +\n - 3. Botão volume -\n - 4. Botão canal +\n - 5. Botão canal -\n - 0. Sair'
    ))
    match menu:
        case 1:#power
            print('[Power]')

        case 2:#vol +
            print('[Vol +]')

        case 3:#vol -
            print('[Vol -]')

        case 4:#canal +
            print('[Ch +]')

        case 5:#canal -
            print('[Ch -]')

        case 0:#sair
            print('[ Saindo da sala ]')

        case _:#tratamento
            print("Code not found")