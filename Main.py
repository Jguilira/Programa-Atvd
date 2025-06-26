
from Produto import Produto
from Produto_alimenticio import Produto_alimenticio

lista_produtos = []

def menu():
    print('\n--- Menu ---')
    print('1 - Cadastrar produto comum')
    print('2 - Cadastrar produto alimentício')
    print('3 - Listar todos os produtos')
    print('4 - Repor estoque')
    print('5 - Vender produto')
    print('Digite "sair" para encerrar')

while True:
    menu()
    opcao = input('\nInforme a opção desejada: ').lower()

    if opcao == 'sair':
        break

    elif opcao == '1':
        nome = input('Nome do produto: ')
        preco = float(input('Preço do produto:R$'))
        quantidade = int(input('Quantidade: '))
        produto = Produto(nome, preco, quantidade)
        lista_produtos.append(produto)

    elif opcao == '2':
        nome = input('Nome do produto: ')
        preco = float(input('Preço do produto: '))
        quantidade = int(input('Quantidade: '))
        data_validade = input('Data de validade: ')
        produto = Produto_alimenticio(nome, preco, quantidade, data_validade)
        lista_produtos.append(produto)

    elif opcao == '3':
        for produto in lista_produtos:
            produto.exibir_produtos()

    elif opcao == '4':
        nome_prod = input('Nome do produto para repor: ')
        for produto in lista_produtos:
            if produto.nome == nome_prod:
                qtd = int(input('Quantidade para repor: '))
                produto.repor_estoque(qtd)
                break
        else:
            print('Produto não encontrado.')

    elif opcao == '5':
        nome_prod = input('Nome do produto para vender: ')
        for produto in lista_produtos:
            if produto.nome == nome_prod:
                qtd = int(input('Quantidade para vender: '))
                produto.vender(qtd)
                break
        else:
            print('Produto não encontrado.')
