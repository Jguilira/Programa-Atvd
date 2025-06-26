print("Atvd vini for")

'''num = int(input("Digite um número:"))
soma = 0
for i in range(1, num+1):
    if i % 2 == 0:
        soma = soma + i

print("A soma dos números pares de 1 a 6:", soma)

numero = int(input("Insira um número inteiro:"))
for i in range(1, 11):
    multi = numero * i
    
    print(f"{numero} x {i} =", multi)

qtd_notas = int(input("Quantas notas:"))
notas = []
for i in range(0, qtd_notas):
    numero = int(input("Insira um numero positivo:"))
    notas.append (numero)

soma = 0
for i in range(0 , qtd_notas):
    soma += notas[i]

    media = soma / qtd_notas
print("A média dos números é:", media)

qtd_numeros = int(input("Quantas notas:"))
numeros = []
for i in range(0, qtd_numeros):
    numero = int(input("Insira um numero positivo:"))
    numeros.append (numero)

soma = 0
for i in range(0 , qtd_numeros):
    soma += numeros[i]

    media = soma / qtd_numeros
print("A média dos números é:", media)

qtd_palavras = int(input("Quantas palavras:"))
lista = []
for i in range(0, qtd_palavras):

    palavras = str(input("Insira a palavra:"))
    lista.append (palavras)

lista.reverse
print("As palavras são:", lista)
print("A média dos números é:", media)

lista = ["Casa", "Moto", "Carro"]
print(lista)
lista.append("Fogão")#Coloca no final da lista.
print(lista)
lista.sort()#Organiza em ordem crescente.
print(lista)
lista.insert(2,"Avião")#Coloca na posição que eu quiser, dois parametros
print(lista)
lista.pop(1)#remove o ultimo.
print(lista)
lista.remove("Fogão")#Remove o item da lista
print(lista)
nome = input("Informe seu nome que deseja procurar:")
quantidade = lista.count(nome)#Retorne um numero inteiro indicando a quatidade de vezes
print("A quantidade  de vezes que josé parece na lista:", quantidade)
lista.reverse()# Organiza a lista em ordem Inversa.
print(lista)
lista2 = lista.copy()
lista.clear()#Esvaziar a lista, remove todos os elementos da lista.
print(lista)
print(lista2)

lista1 = ["Vini", "Bete", "Carlos", "Luana"]
print(lista1)
lista2 = lista1.copy()
print(lista1 + lista2)

lista_usu = int(input("Informe quantos números você quer na lista: "))
lista = []
for i in range(0, lista_usu):
    lista.append(int(input("Informe um número:")))
lista.sort()


print("O maior é:", lista[lista_usu-1])
print("O menor é:",lista[0])

n = int(input("Insira o número pra fatorar:"))
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i 
print(fatorial)

numero = int(input("Informe um número para a sequencia de fibonacci:"))
one, two = 0, 1

for i in range(numero):
    print(one)
    one , two = two, one + two'''

'''n = int(input("Digite um numero:"))
soma_dos_divisores = 0

for i in range(1, n):

    if n % i == 0:
        soma_dos_divisores = soma_dos_divisores + i
if soma_dos_divisores == n:
    print(f"Número perfeito: {n} ")
else:
     print(f"Não é número perfeito: {n}")'''

'''lista = []

for i in range(100):
    lista_num = int(input("Insira um número: "))
    lista.append(lista_num)
    print(lista)
    if lista == sorted(lista):
        print("SIM")
    else:
        print("NÃO")'''

'''dia = int(input("Insira um número de 1 até 7: "))

match dia:
    case 1:
        print("Segunda-feira")
    case 2:
        print("Terça-feira")
    case 3:
        print("Quarta-feira")
    case 4:
        print("Quinta-feira")
    case 5:
        print("Sexta-feira")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")'''



'''aluno = {
    "id": 1,
    "Nome": "João gui",
    "Idade": 17,
    "notas": []
}

for chaves, valor in aluno.items():
   print(chaves, valor)'''

'''aluno = {
    "id": 1,
    "Nome": "João gui",
    "Idade": 17,
    "notas": []
}

for i in range(3):
    aluno["notas"].append(float(input("Insira sua nota: ")))

print(aluno["notas"])'''
'''
alunos = {
    "aluno1": {
    "id": 1,
    "Nome": "João gui",
    "Idade": 17,
    "notas": []
    },
    "aluno2": {
    "id": 2,
    "Nome": "Gustavo",
    "Idade": 18,
    "notas": []
    }
}

for nota in range(2):
    nota1 = (float(input("Insira uma nota: ")))
    alunos["aluno1"]["notas"].append(nota1)

    nota2 = (float(input("Insira uma nota: ")))
    alunos["aluno2"]["notas"].append(nota2)

media = (nota1[alunos] + nota2) / 2

print("notas dos alunos: ", media)
for aluno, dados in alunos.items():
    print(f"{dados['Nome']} Notas: {dados['notas']}"'''


'''qtd = int(input("Insira a quantidade de funcionários: "))
funcionario = {}
for i in range(0, qtd):
    nome = str(input("Insira o nome do funcionário: "))
    salario = float(input("Insira o salario do funcionário: "))
    funcionario[nome] = salario
print(funcionario.items())


nome_funcionario = str(input("Insira o nome do funcionario que você deseja: "))

if nome_funcionario in funcionario:
    print((f'O funcionario é {nome} e o salário é {salario}'))
else:
    print('Esse funcionário nao existe!')

media = sum(funcionario.values()) / len(funcionario)
print(f'A média de sálario da sua empresa é {media}')'''

'''pessoas = {'nome': 'Guilherme', 'idade': 22, 'sexo': 'Masculino'}
print(f'O sexo é:{pessoas["sexo"]}')'''

'''texto = 'abracadabra'
contagem = {}

for letra in texto:
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1

print(contagem)'''

'''aparelhos = {'iphone 11': 2500, 'ipad': 10000, 'airpods': 400 }

aparelhos['macbook'] = 22000'''
'''loja = {}
qtd_produto_cad = int(input('Insira quantos produtos serão cadastrados: '))
for i in range(qtd_produto_cad):
    nome_produto = str(input('Insira o nome do produto: '))
    qtd_produto =  int(input('Insira quantidade do produto: '))
    loja[nome_produto] = qtd_produto

for chave, valor in loja.items():
    print(f'Produto: {chave} | Quantidade: {valor}')
print('--'*45)
print('Busca pelo produto\n')
produto = input('Informe o nome do produto: ')

if produto in loja:
    print(f'A quantidade do item {produto} é: {loja[produto]}')
else:
    print('Produto não está no estoque!')

print('Adicionar ou remover produtos')
att_produto = input('Informe o nome do produto: ')

if att_produto in loja:
    print('1 - Para adicionar')
    print('2 - Para remover')
    opcao = int(input('Informe o número desejado: '))

    if opcao == 1:
        qtd_adc = int(input('Informe a quantidade que deseja adicionar: '))
        loja[att_produto] += qtd_adc
        print(f'Quantidade após adicionar {loja[att_produto]}')
    elif opcao == 2:
        qtd_rm = int(input('Informe a quantidade que deseja remover: '))
        if qtd_rm > loja[att_produto]:
            print(f'Você só pode remover até {loja[att_produto]} unidades desse item')
        else:
            loja[att_produto] -= qtd_rm
            print(loja[att_produto])'''






'''projetos = []
qtd_projetos = int(input('Insira a quantidade de projetos: '))
for i in range(qtd_projetos):
    nome_projeto = str(input('Insira o nome do projeto: '))
    nome_responsavel = str(input('Insira o nome do responsável pelo projeto: '))
    qtd_horas = int(input('Insira a quantidade de horas estimadas: '))
    status_projeto = str(input('Insira "ativo" ou "finalizado": '))
    projeto = {
        "Nome": nome_projeto,
        "Responsável": nome_responsavel,
        "Horas": qtd_horas,
        "Status": status_projeto
    }
    projetos.append(projeto)
    print('Dados cadastrados.')

print(projetos)

print("---"*30)
print('MENU')
print('1 - Listar todos os projetos')
print('2 - Buscar projetos por responsável')
print('3 - Exibir somente projetos ativos')
print('4 - Calcular total de horas estimadas')
print('5 - Alterar status de um projeto')
print('6 - Sair')

condicao = int(input('Insira o número desejado: '))

while condicao != 6:
    if condicao == 1:
        print(projetos)
    elif condicao == 2:
        responsavel = str(input('Insira o nome do responsável pelos projetos que você deseja: '))
        for proj in projetos:
            if proj['Responsável'].lower() == responsavel.lower():
                print(proj)
    elif condicao == 3:
        for proj in projetos:
            if proj['Status'].lower() == 'ativo':
                print(proj)
    elif condicao == 4:
        total_horas = 0
        for proj in projetos:
            total_horas += proj['Horas']
        print(f'O total de horas é: {total_horas}')
    elif condicao == 5:
        nome_projeto_alterar = str(input('Insira o nome do projeto que deseja alterar o status: '))
        novo_status = str(input('Insira o novo status ("ativo" ou "finalizado"): '))
        projetos_alterados = 0
        for proj in projetos:
            if proj['Nome'].lower() == nome_projeto_alterar.lower():
                proj['Status'] = novo_status.lower()
                print(f'O status do projeto "{nome_projeto_alterar}" foi alterado para "{novo_status}".')
                projetos_alterados += 1
    elif condicao == 6:
        print('Saindo do programa.')
    condicao = int(input('Insira o número desejado: '))'''

