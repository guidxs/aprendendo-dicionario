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

#Exercicio 42 - Crie um dicionário com nomes de filmes e seus anos de lançamento. Peça ao usuário para digitar um ano e exiba os filmes lançado naquele ano.

filmes = {'Matrix': 1999, 'Senhor dos Anéis': 2001, 'Avatar': 2009}
ano = int(input("Digite um ano: "))
filmes_no_ano = [movie for movie, release_ano in filmes.items() if release_ano == ano]
if filmes_no_ano:
    print(f"Filmes lançados em {ano}: {', '.join(filmes_no_ano)}")
else:
    print(f"Nenhum filme lançado em {ano}.")


ExercÃ­cio 43 - Enunciado: Crie um dicionário representando uma agenda de compromissos. 
Permita ao usuário adicionar e listar compromissos para um determinado dia.

compromissos = {}
while True:
    print("1. Adicionar compromisso")
    print("2. Listar compromissos")
    print("3. Sair")
    choice = int(input("escolha uma opção: "))
    
    if choice == 1:
        date = input("Digite a data (DD/MM/AAAA): ")
        compromisso = input("Digite o compromisso: ")
        if date in compromissos:
            compromissos[date].append(compromisso)
        else:
            compromissos[date] = [compromisso]
        print("Compromisso adicionado.")
    elif choice == 2:
        date = input("Digite a data para istar os compromissos: ")
        compromissos_list = compromissos.get(date, [])
        if compromissos_list:
            print(f"Compromissos em {date}:")
            for idx, compromisso in enumerate(compromissos_list, start=1):
                print(f"{idx}. {compromisso}")
        else:
            print(f"Nenhum compromisso marcado para {date}.")
    elif choice == 3:
        break


Exercício 44 - Enunciado: Crie um dicionário com nomes de animais como keys 
e suas características como valores. 
PeÃ§a ao usuário para adivinhar um animal a partir de uma característica.



animais = {'cachorro': 'late', 'gato': 'mia', 'elefante': 'trumpeta'}
caracteristica = input("Digite uma caracterÃ­stica: ")
matching_animais = [animal for animal, char in animais.items() if char == caracteristica]
if matching_animais:
    print(f"Animais que {caracteristica}: {', '.join(matching_animais)}")
else:
    print(f"Nenhum animal encontrado com a característica '{caracteristica}'.")


Exercício 45 - Enunciado: Crie um dicionário com nomes de pratos de 
diferentes países e suas receitas. 
Permita ao usuÃ¡rio escolher um prato e exibir a receita.


pratos = {'feijoada': 'Receita da feijoada...', 'sushi': 'Receita de sushi...', 'pasta': 'Receita de pasta...'}
prato = input("Digite o nome de um prato: ")
receita = pratos.get(prato, "Prato não encontrado")
print(f"Receita de {prato}: {receita}")



Exercício 46: - Enunciado: Crie um programa de quiz com perguntas sobre 
capitais de países. 
Use um dicionário para armazenar as perguntas e respostas corretas.


questoes = {'Qual é a capital do Brasil?': 'Brasília', 'Qual é a capital dos Estados Unidos?': 'Washington'}
score = 0
for questao, correct_answer in questoes.items():
    user_answer = input(questao + " ")
    if user_answer == correct_answer:
        print("Resposta correta!")
        score += 1
    else:
        print(f"Resposta incorreta. A resposta correta é: {correct_answer}")
print(f"Voce acertou {score}/{len(questoes)} perguntas.")



Exercício 47 - Enunciado: Crie um dicionÃ¡rio com palavras-chave relacionadas a
um tópico de interesse. Implemente um sistema de busca para exibir 
informações sobre a palavra-chave inserida pelo usuário.


palavra_keys = {'python': 'Linguagem de programação', 'machine learning': 'Técnica de aprendizado de máquina', 'web development': 'Desenvolvimento de sites'}
pesquisar_termo = input("Digite uma palavra-chave: ")
definicao = palavra_keys.get(pesquisar_termo, "Palavra-chave não encontrada")
print(f"{pesquisar_termo}: {definicao}")


Exercício 48 - Enunciado: Crie um jogo de adivinhação onde o programa escolhe 
uma palavra e o jogador precisa adivinhar as letras. 
Use um dicionário para controlar as letras corretas e incorretas.


import random

palavras = ['python', 'programming', 'dictionary', 'challenge']
palavra = random.choice(palavras)
correct_letters = set()
letras_incorretas = set()

while len(letras_incorretas) < 6:
    display_palavra = ''.join([letter if letter in correct_letters else '_' for letter in palavra])
    print(f"Palavra: {display_palavra}")
    print(f"Letras incorretas: {', '.join(letras_incorretas)}")
    
    guess = input("Digite uma letra: ")
    if guess in correct_letters or guess in letras_incorretas:
        print("Voce já¡ tentou essa letra.")
    elif guess in palavra:
        correct_letters.add(guess)
        if all(letter in correct_letters for letter in palavra):
            print(f"Parabéns! A palavra era '{palavra}'.")
            break
    else:
        letras_incorretas.add(guess)
else:
    print(f"VocÃª errou muito! A palavra era '{palavra}'.")


Exercício 49: - Enunciado: Crie um dicionário com nomes de ingredientees 
e suas quantidades em gramas. PeÃ§a ao usuário para digitar o nome de um ingredientee
e a quantidade desejada, e ajuste o dicionário.


ingredientes = {'farinha': 500, 'açúcar': 300, 'ovos': 4}
ingrediente = input("Digite o nome do ingredientee: ")
quantidade = int(input("Digite a quantidade desejada (em gramas): "))
ingredientes[ingrediente] = quantidade
print(f"ingrediente '{ingrediente}' atualizado para {quantidade}g.")



Exercí­cio 50 - Enunciado: Crie um programa que simule um carrinho de compras. 
Use um dicionário para armazenar os itens e suas quantidades. 
Permita ao usuário adicionar, remover e listar itens do carrinho.


carrinho_de_compras = {}
while True:
    print("1. Adicionar item ao carrinho")
    print("2. Remover item do carrinho")
    print("3. Listar itens do carrinho")
    print("4. Sair")
    choice = int(input("choice uma opção: "))
    
    if choice == 1:
        item = input("Digite o nome do item: ")
        quantidade = int(input("Digite a quantidade desejada: "))
        if item in carrinho_de_compras:
            carrinho_de_compras[item] += quantidade
        else:
            carrinho_de_compras[item] = quantidade
        print(f"{quantidade} {item}(s) adicionado(s) ao carrinho.")
    elif choice == 2:
        item = input("Digite o nome do item a ser removido: ")
        if item in carrinho_de_compras:
            del carrinho_de_compras[item]
            print(f"{item} removido do carrinho.")
        else:
            print(f"{item} não encontrado no carrinho.")
    elif choice == 3:
        print("Itens no carrinho:")
        for item, quantidade in carrinho_de_compras.items():
            print(f"{item}: {quantidade}")
    elif choice == 4:
        break


Exercí­cio 51 - Gerenciamento de Estoque
Enunciado - Voce é responsável por desenvolver um sistema de gerenciamento de estoque 
para uma loja. O sistema deve permitir a adição de novos produtos, 
atualização de quantidades em estoque, venda de produtos e exibição de relatários. 
Voce deve usar um dicionÃ¡rio para armazenar as informações dos produtos.
 - Implemente as seguintes funcionalidades:
*1* - Adicionar Produto: O usuário pode adicionar um novo produto ao estoque. Cada produto terá¡ um nome, preÃ§o unitÃ¡rio e quantidade inicial em estoque.
*2* - Atualizar Estoque: O usuário pode atualizar a quantidade em estoque de um produto existente.
*3* - Vender Produto: O usuÃ¡rio pode registrar uma venda de um produto, diminuindo a quantidade
      em estoque. Se a quantidade vendida for maior que a quantidade em estoque, 
      informe que não é possível realizar a venda.
*4* - Relatório de Estoque: Exiba um relatório com todos os produtos, 
      seus preços e quantidades em estoque.


estoque = {}  # DicionÃ¡rio para armazenar o estoque (nome do produto: {'preÃ§o': X, 'quantidade': Y})

#definicao de funcoes:
    
def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    price = float(input("Digite o preÃ§o unitÃ¡rio do produto: "))
    quantity = int(input("Digite a quantidade inicial em estoque: "))
    estoque[nome] = {'preço': price, 'quantidade': quantity}
    print(f"Produto '{nome}' adicionado ao estoque.")

def atualizar_estoque():
    nome = input("Digite o nome do produto para atualização: ")
    if nome in estoque:
        nova_quantidade = int(input(f"Atualize a quantidade de '{nome}' em estoque: "))
        estoque[nome]['quantidade'] = nova_quantidade
        print(f"Estoque de '{nome}' atualizado para {nova_quantidade}.")
    else:
        print(f"Produto '{nome}' nÃ£o encontrado no estoque.")

def vender_produto():
    nome = input("Digite o nome do produto vendido: ")
    if nome in estoque:
        quantidade_vendida = int(input(f"Digite a quantidade de '{nome}' vendida: "))
        if quantidade_vendida <= estoque[nome]['quantidade']:
            estoque[nome]['quantidade'] -= quantidade_vendida
            print(f"{quantidade_vendida} unidades de '{nome}' vendidas.")
        else:
            print(f"Não há¡ quantidade suficiente de '{nome}' em estoque para realizar a venda.")
    else:
        print(f"Produto '{nome}' não encontrado no estoque.")

def estoque_relatorio():
    print("Relatário de Estoque:")
    for product, info in estoque.items():
        print(f"Produto: {product} | Preço: R${info['preço']} | Quantidade em Estoque: {info['quantidade']}")


def linha_separacao():
    return print(' -'*30)


# Menu principal
while True:
    linha_separacao()
    print("\n=== Sistema de Gerenciamento de Estoque ===")
    linha_separacao()
    print("1. Adicionar Produto")
    linha_separacao()
    print("2. Atualizar Estoque")
    linha_separacao()
    print("3. Vender Produto")
    linha_separacao()
    print("4. RelatÃ³rio de Estoque")
    linha_separacao()
    print("5. Sair")
    linha_separacao()
    choice = int(input("choice uma opÃ§Ã£o: "))
    
    if choice == 1:
        adicionar_produto()
    elif choice == 2:
        atualizar_estoque()
    elif choice == 3:
        vender_produto()
    elif choice == 4:
        estoque_relatorio()
    elif choice == 5:
        print("Saindo do sistema.")
        break
    else:
        print("OpÃ§Ã£o invÃ¡lida. choice uma opÃ§Ã£o vÃ¡lida.")

#Ex 52 -

def contar_palavras(lista):
    frequencias = {}
    for palavra in lista:
        if palavra in frequencias:
            frequencias[palavra] += 1
        else:
            frequencias[palavra] = 1
    return frequencias

#Ex 53 -

def unir_dicionarios(d1, d2):
    novo_dicionario = d1.copy()
    novo_dicionario.update(d2)
    return novo_dicionario


#Ex 54 -

def listar_chaves(dicionario):
    chaves = []
    for chave, valor in dicionario.items():
        chaves.append(chave)
        if isinstance(valor, dict):
            chaves.extend(listar_chaves(valor))
    return chaves

#Ex 55 -

pessoas = {
    'Ana': 30,
    'João': 25,
    'Maria': 40,
    'Pedro': 22
}

pessoas_ordenadas = dict(sorted(pessoas.items(), key=lambda item: item[1]))

#Ex 56

import statistics

def analisar_numeros(lista):
    resultado = {
        'soma': sum(lista),
        'media': statistics.mean(lista),
        'desvio_padrao': statistics.stdev(lista)
    }
    return resultado

#Ex 57 -

def contar_palavras_variaveis(*args):
    frequencias = {}
    for palavra in args:
        frequencias[palavra] += 1
    else:
        frequencias[palavra] = 1
    return frequencias


#Ex 58 -

def criar_funcao_potencia(n):
    def funcao_potencia(x):
        return(2 * x) ** n
    return funcao_potencia()

"""
