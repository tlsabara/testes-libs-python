#Aprendendo listas
#Controle de nota com listas
#sbKing 18/12/2021 23:48
#v1.0

#variáveis de listas
listaNomes = []
listaNotas = []
listaPesos = []

#insert do numero de notas e pesos
NumeroDeAlunos = int(input('Qual a quantidade de ALUNOS que você irá inserir?'))
NumeroDeNotas = int(input('Qual a quantidade de NOTAS (para cada ALUNO) que você irá inserir?'))

idAluno = 0 #ponteiro da lista de alunos para inserção
idNotas = 0 #ponteiro da lista de notas para inserção

#Função insere pesos
def inserePeso(b):
    a = int(input('Digite o peso da nota {}:  '.format(b)))
    #preciso de uma tratativa de erro para o caso do usuário não inserir uma nota do tipo inteiro
    return a

#Função insere Notas
def insereNotas(b,n):
    a = int(input('Digite a nota {} do aluno {}:  '.format(b,n)))
    while a > 10:
        a = int(input('Valor acima do permitido!(max: 10)\n\nDigite a nota {} do aluno {}:  '.format(b,n)))
    return a

#Função insere nome de Alunos
def insereAlunos(b):
    a = input('Digite o nome do Aluno Nr.{}:  '.format(b))
    while a in listaNomes:
        a = input('{} já existe nos registros. Digite um outro nome para o Aluno Nr.{}:  '.format(a,b))
    return a


#populando os pesos
print('---- |Inserindo os pesos| ----')
if NumeroDeNotas > len(listaPesos):
    while NumeroDeNotas > len(listaPesos):
        pesoInserido = inserePeso(len(listaPesos)+1)
        listaPesos.append(pesoInserido)
else:
    print('Sem pesos de notas a serem inseridas')

#retorno para o usuário
print('<<<<<<<<<<<<<<<<<| Fim da inserção de Pesos')

#populando os alunos e notas
print('---- |Inserindo Alunos e Notas| ----')
if NumeroDeAlunos > len(listaNomes):
    while NumeroDeAlunos > len(listaNomes):
        print('<Novo aluno>')
        NomeAlunoInserido = insereAlunos(len(listaNomes)+1)
        listaNomes.append(NomeAlunoInserido)
        NotasDoAluno = 0
        #populando as notas
        print('------ |Inserindo as notas do aluno: {}| ------'.format(NomeAlunoInserido))
        while NotasDoAluno < NumeroDeNotas:
            NotaInserida = insereNotas(NotasDoAluno+1,NomeAlunoInserido)
            listaNotas.append(NotaInserida)
            NotasDoAluno = NotasDoAluno + 1
else:
    print('Sem notas a serem inseridas')

# impressão dos dados
menu = int(input('Digite 1 para selecionar apenas 1 aluno, digite 0 para imprimir todos os alunos: '))

while menu == 1:
    srchValue = input('Digite o valor a ser procurado: ')
    if srchValue in listaNomes:

        posNome = listaNomes.index(srchValue)
        print('O nome foi localizado!')
        print(listaNomes[posNome])
         
        t=1
        n=[]
        while t <= NumeroDeNotas:
            print('A nota {} foi: {}'.format(t,listaNotas[posNome * NumeroDeNotas+(t-1)]))
            n.append((listaNotas[posNome * NumeroDeNotas+(t-1)])*listaPesos[(t-1)])
            t = t+1
        mediaAluno =sum(n)/sum(listaPesos)
        n.clear()
        print('a Média foi de: {}'.format(mediaAluno))
        if mediaAluno >= 6:
            print('o aluno foi aprovado!')
        else:
            print('o aluno foi reprovado!')
    else:
        print('O nome não existe na lista')
    menu = int(input('Digite 1 para selecionar apenas 1 aluno, digite 0 para imprimir todos os alunos: '))
#Imprimindo todas as notas
for AluNome in listaNomes:
    vposNome = listaNomes.index(AluNome)
    print('Nome do aluno: {}'.format(listaNomes[vposNome]))
    t=1
    n=[]
    while t <= NumeroDeNotas:
        print('A nota {} foi: {}'.format(t,listaNotas[vposNome * NumeroDeNotas+(t-1)]))
        n.append((listaNotas[vposNome * NumeroDeNotas+(t-1)])*listaPesos[(t-1)])
        t = t+1
    #Cálculo da média
    mediaAluno =sum(n)/sum(listaPesos)
    n.clear()
    print('a Média foi de: {}'.format(mediaAluno))
    if mediaAluno >= 6:
        print('o aluno foi aprovado!')
    else:
        print('o aluno foi reprovado!')

#Fim da impressão de notas
print('Fim do programa!')