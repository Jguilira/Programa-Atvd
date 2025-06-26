print("Orientação objetos\n")


'''n = int(input("Digite um numero:"))
soma_dos_divisores = 0

for i in range(1, n):

    if n % i == 0:
        soma_dos_divisores = soma_dos_divisores + i
if soma_dos_divisores == n:
    print(f"Número perfeito: {n} ")
else:
     print(f"Não é número perfeito: {n}")'''



'''class Dateko:
    def __init__(self, nome, fone, Cadastro_pessoa_fisica):
        self.nome = nome
        self.telefone = fone
        self.cpf = Cadastro_pessoa_fisica

    def infor(self):
        print("Informaçôes do cliente:")
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")

c1 = Dateko("João guilherme", "(87)98888-8888", "111.111.111-00\n")
c2 = Dateko("Luciene Almeida", "(87)98888-8888", "111.111.111-00")

c1.infor()
c2.infor()
c1 = Dateko("João guilherme", "(87)98888-8888", "111.111.111-00\n")
c2 = Dateko("Luciene Almeida", "(87)98888-8888", "111.111.111-00")

print(f"Nome: {c1.nome} Número: {c1.telefone} CPF: {c1.cpf}")
print(f"Nome: {c2.nome} Número: {c2.telefone} CPF: {c2.cpf}")'''

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.estado = False

    def ligar(self):
        self.estado = True
        print(f'O carro {self.modelo} está ligado!')

    def desligar(self):
        self.estado = False
        print(f'O carro {self.modelo} está desligado!')

    def info(self):
        aux = 'Ligado' if self.estado else 'Desligado'
        print("-"*45)
        print('Informações do carro:')
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')
        print(f'Estado: {aux}')
carros = []
res_usu = input(f'MENU - LOCADORA\n1 - Cadastrar novo carro\n2 - Ligar carro\n3 - Desligar carro\n4 - Ver carro disponiveis\n5 - Sair\nEscolha a opção: ')
while res_usu != 5:
    if res_usu == '1':
        marca = input('Insira a marca do carro: ')
        modelo = input('Insira o modelo do carro: ')
        ano = input('Insira o ano do carro: ')
        carro1 = Carro(marca, modelo, ano)
        carros.append(carro1)
        print('Carro adicionado!')
    elif res_usu == '2':
        modelo1 = input('Qual o modelo de carro deseja ligar?: ')
        for i in carros:
            if i.modelo == modelo1:
                i.ligar()
                break
        else:
                print('Esse modelo não foi encontrado!')
    elif res_usu == '3':
        modelo_desligado = input('Qual o modelo do carro deseja desligar?: ')
        for i in carros:
            if i.modelo_desligado == modelo: 
                i.desligar()
            break
        else:
            print('Esse modelo não foi encontrado!')
    elif res_usu == '4':
        print(f'Lista de carros Disponiveis')
        for c in carros:
             c.info()

    res_usu = input(f'MENU - LOCADORA\n1 - Cadastrar novo carro\n2 - Ligar carro\n3 - Desligar carro\n4 - Ver carro disponiveis\n5 - Sair\nEscolha a opção: ')

print('Encerrando o programa!...')








     