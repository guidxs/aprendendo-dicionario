'''
dicio = {'chave': 'valor'}

print(type(dicio))
-
dicio_2={'primeiro': 1, 'segundo': 2, 'terceiro': 3}
-
dicio = dict(primeiro=1, segundo=2, terceiro=3)
-
dicio_3 = dict(zip(['primeiro','segundo','terceiro'],[1,2,3]))
-
dicio_4 = dict([('primeiro', 1), ('segundo',2),('terceiro',3)])
-
dicio_6 = {name: idx + 1 for idx, name in enumerate(('primeiro','segundo','terceiro'))}
-
dicio_5 = dict({'primeiro':1,'segundo':2,'terceiro':3})
-
pessoa = {'nome': 'Pythonico', 'altura': 1.65, 'idade': 21}

print(pessoa['nome'])

print(pessoa.get('nome'))

print(pessoa.get('peso', 'Chave não encontrada'))
-
computador = {'CPU': 'Intel', 'RAM': '8gb', 'SSD': '250gb'}

print(computador.keys())
-
notas = {'Mat': 5, 'Por': 7, 'His': 8}

print(notas.values())
-
computador = {'CPU': 'Intel', 'RAM': '8gb', 'SSD': '250gb'}

for chave in computador.keys():
    print(f'Chave = {chave} e Valor = {computador[chave]}')
-
notas = {'Mat': 5, 'Por': 7, 'His': 8}

for valor in notas.values():
    print(f'Valor: {valor}')    
-
frutas = {'pera': 10, 'uva': 2, 'maça': 55}

print(frutas.items())
-
dicio_cores = {'amarelo': 10, 'vermelho': 2, 'cinza': 55}

# Verificando se chave existe
if 'amarelo' in dicio_cores:
    print(f"Como a cor desejada existe: {dicio_cores ['amarelo']}")
   
# Verificando se valor existe
if 10 in dicio_cores.values():
    print('O valor desejado existe')
-    
dicio = {'nome': 'Erick'}

dicio['idade'] = 20

print(dicio)

dicio = {'nome': 'Erick'}

#Atualiza o elemento de chave 'nome'
dicio.update({'nome': 'Matheus'})

#Cria os elementos da chave 'idade' e 'tamanho'
dicio.update({'idade': 18})
dicio.update(tamanho = 1.60)

print(dicio)

pessoa = {'nome': 'Matheus', 'idade': 18, 'tamanho': 1.60}

del pessoa ['tamanho']

print(pessoa)

sacola = {'maça': 2, 'ovos': 6, 'farinha': 2}
ovos = sacola.pop('ovos')

print(ovos)
print(sacola)

sacola = {'maça': 2, 'ovos': 6, 'farinha': 2}

farinha = sacola.popitem()

print(farinha)
print(sacola)

dicio = {'nome': 'F9', 'motor': 'V8', 'ano': 2019}
dicio.clear()

print(dicio)

dicio = {"operacao": "web scrapping", "dados": 250}

copia = dicio.copy()

print(copia)
print(dicio)

dicio = {'coleta': 'scrappy', 'dados': 200}

set_dados = dicio.setdefault('dados')

print(set_dados)
print(dicio)
-
dicio = {'coleta': 'scrappy', 'dados': 200}

set_data = dicio.setdefault('data')
set_teste = dicio.setdefault('teste', 1)

print(set_data)
print(set_teste)
print(dicio)
-
chaves = ['chave1', 'chave2', 'chave3']
valor = 0

dicio = dict.fromkeys(chaves , valor)

print(dicio)
-
def funcao(argumento):
    print(argumento)

dicionario = {'argumento': 1}

funcao(dicionario)
funcao(**dicionario)
-
regulagem = {'max': 10, 'meio': 5, 'min': 0}

def funcao(max, meio, min):
    print(max)
    print(meio)
    print(min)
   
funcao(**regulagem)
-
# Definição de Função recebendo kwargs
def funcao(**kwargs):
    # Percorrendo argumento nomeados
    for chave in kwargs:
        print (f"Acessando Chave '{chave}', valor = {kwargs.get(chave)}")
       
regulagem = {'max': 10, 'meio': 5, 'min': 0}

funcao(**regulagem)

def funcao (*args):
    for chave in args:
        print(chave)
       
funcao(*regulagem)
-
regulagem = {'max': 10, 'meio':5, 'min':0}
extra = {'passo': 2}

# Junção de dicionario com **
juncao_dicio = {**regulagem, **extra}

print(juncao_dicio)
-

#Exercicio 31 - Crie um dicionario vazio e imprima

dictio = {}
print(dictio)

#Exercicio 32 - Crie um enunciado com três frutas pares chava-valor representando nomes de frutas es suas quantidades

frutas = {'maca': 2, 'banana': 3, 'laranja': 7}
print(frutas)

#Exercicio 33 - Adicione uma nova fruta ao dicionario do exercicio 32 com sua respectiva quantidade.

frutas['uvas'] = 9
print(frutas)

#Exercicio 34 - Dado um dicionario de notas do alunos, calcule a média das notas e imprima o resultado

notas = {'José': 8, 'Marcos': 6, 'Caio': 9, 'Erick': 7}
media = sum(notas.values()) / len(notas)
print(f"A média das notas é: {media:.2f}")

#Exercicio 35 - Crie um dicionario de palavras e suas traduções em outro idioma. Peça ao usuário para digitar uma palavra e retornar a tradução.

trads = {'Olá': 'Hello', 'Oi': 'Hi', 'Tchau': 'Bye', 'Cachorro': 'Dog', 'Gato': 'Cat'}
palavra = input("Digite uma palavra: ")
trad = trads.get(palavra, "Tradução não encontrada!")
print(trad)

#Exercicio 36 - Crie um dic com nome de cidades como keys e suas populações como valores.

cidades = {'New York': 8623000, 'Caieiras': 110000, 'Los Angeles': 3990000}
cidade = input("Digite o nome da sua cidade: ")
populacao = cidades.get(cidade, "Cidade não encontrada!")
print(f"A população de {cidade} é {populacao}")

#Exercicio 37 - Crie um dicionario com nomes de produtos e seus preços

produtos = {'maca': 1.00, 'carne': 45.00, 'refri': 5.00, 'chocolate': 7.00}
lista = input("Digite seus produtos da lista (separados por virgula): ").split(', ')
total = sum(produtos[item] for item in lista if item in produtos)
print(f"O custo total é: R${total:.2f}")

#Exercicio 38 - Crie um programa que simule um dicionario de contatos

while True:
    print("1. Adicionar contato")
    print("2. Remover contato")
    print("3. Buscar contato")
    print("4. Sair")
    choice = int(input("Escolha uma opção: "))
   
    if choice == 1:
        nome = input("Digite o nome do contato: ")
        numero = input("Digite o número do contato: ")
        contatos[nome] = numero
    elif choice == 2:
        nome = input("Digite o nome do contato a ser removido: ")
        if nome in contatos:
            del contatos[nome]
            print(f"Contato {nome} removido.")
        else:
            print("Contato não encontrado.")
    elif choice == 3:
            nome = input("Digite o nome do contato a ser buscado: ")
            numero = contatos.get(nome, "Contato não encontrado")
            print(f"Número de {nome}: {numero}")
    elif choice == 4:
        break

#Exercicio 39 - Dic de quiz de capital de paises

import random

paises = {'Brasil': 'Brasilia', 'EUA': 'Washington', 'France': 'Paris'}
pais = random.choice(list(paises.keys()))
guess = input(f"Qual é a capital de {pais}? ")
if guess == paises[pais]:
    print("Resposta Correta!")
else:
    print(f"Resposta incorreta. A capital do {pais} é {paises[pais]}")

#Exercicio 40 -

import random

definicoes = {'Python': 'Linguagem de programação de alto nivel', 'database': 'Conjunto organizacional'}
palavra_chave = random.choice(list(definicoes.keys()))
definicao = input (f"Qual é a definição de '{palavra_chave}'? ")
if definicao == definicoes[palavra_chave]:
    print("Resposta Correta!")
else:
    print(f"A Resposta esta incorreta. A definição de '{palavra_chave}' é {definicoes[palavra_chave]}'.")
   
#Exercicio 41 - Crie um programa de cadastro de funcionario.

empregados = []
while True:
    print('1. Cadastrar Funcionário')
    print('2. Listar Funcionários')
    print('3. Sair')
    choice = int(input("Escolha uma opção: "))
   
    if choice == 1:
        empregado = {}
        empregado['nome'] = input("Nome: ")
        empregado['cargo'] = input("Cargo: ")
        empregado['salario'] = input("Salário: ")
        empregados.append(empregado)
        print("Funcionário cadastrado.")
    elif choice == 2:
        for empregado in empregados:
            print(f"Nome: {empregado{'nome'}}, Cargo: {empregado{'cargo'}}, Salário: {empregado{'salario'}}")
    elif choice == 3:
        break
'''
#Exercicio 42 - Crie um dicionário com nomes de filmes e seus anos de lançamento. Peça ao usuário para digitar um ano e exiba os filmes lançado naquele ano.

filmes = {'Matrix': 1999, 'Senhor dos Anéis': 2001, 'Avatar': 2009}
ano = int(input("Digite um ano: "))
filmes_no_ano = [movie for movie, release_ano in filmes.items() if release_ano == ano]
if filmes_no_ano:
    print(f"Filmes lançados em {ano}: {', '.join(filmes_no_ano)}")
else:
    print(f"Nenhum filme lançado em {ano}.")