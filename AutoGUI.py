#importação da biblioteca
import pyautogui as tela

#click no menu inciar
tela.click(x=24, y=1061);
tela.sleep(0.5);

#usando a pesquisa para chamar o chrome
tela.typewrite('chrome');
tela.sleep(0.5);
tela.press('enter');
tela.sleep(1.5);

#clicando na barra de endereços, na tela maximizada
tela.click(x=2705, y=148);

#digitando o endereço na barra
tela.typewrite('google.com.br');
tela.press('enter');
tela.sleep(0.5);

#a pesquisa ja fica com o cusrsor então é só digitar diretamente
tela.typewrite('dolar hoje');
tela.press('enter');

#aguardar carregar a pgna
tela.sleep(1.5);

#clicar no campo de valor do dolar
tela.click(x=2160, y=588);

#selecionar tudo
tela.hotkey('ctrl','a');

#copiar
tela.hotkey('ctrl','c');
tela.sleep(0.5);

#chamar a tela de "Executar do windows" via hotkeys
tela.hotkey('win','r');
tela.sleep(0.5);

#abrir o notepad
tela.typewrite('notepad');
tela.press('enter');
tela.sleep(0.5);

#apresentar o resultado
tela.typewrite('Valor do dólar hoje: '); #ERRO: caractéres especiais não estão aparecendo.
tela.hotkey('ctrl', 'v');
tela.sleep(0.5);
tela.press('enter');
tela.typewrite('Copiado do Google');

#aprendi que o pyautogui tmb localiza trechos de imagens.
tela.locateOnScreen(img)
