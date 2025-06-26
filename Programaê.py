'''class Viagem:

    def __init__(self, nome, destino):
        self.nome = nome
        self.destino = destino
nome_viajante = input('Insira o nome do viajante: ')

destino = ['Rio de janeiro', 'São paulo', 'Petrolina', 'Aracaju']

print('Destinos disponiveis: ')
for i in range(len(destino)):
    print(f'{destino[i]}')

opção = int(input('Informe um número:'))

viagem = Viagem(nome_viajante, destino)

print(f'\n Viajante: {viagem.nome}')
print(f'Destino escolhido: {viagem.destino[opção - 1]}')'''

# Classe Livro
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

# Lista com 10 livros (instâncias da classe Livro)
livros = [
    Livro("Dom Casmurro", "Machado de Assis"),
    Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry"),
    Livro("1984", "George Orwell"),
    Livro("O Hobbit", "J.R.R. Tolkien"),
    Livro("Capitães da Areia", "Jorge Amado"),
    Livro("A Revolução dos Bichos", "George Orwell"),
    Livro("Memórias Póstumas de Brás Cubas", "Machado de Assis"),
    Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling"),
    Livro("Orgulho e Preconceito", "Jane Austen"),
    Livro("O Código Da Vinci", "Dan Brown")
]


print("Lista de Livros Disponíveis:\n")
for i, livro in enumerate(livros, 1):
    print(f"{i}. {livro}")

nome = input("\nDigite seu nome para realizar o empréstimo: ")


escolha = input("Escolha o número do livro que deseja emprestar (1-10): ")

if escolha:
    escolha = int(escolha)
    if 1 <= escolha <= 10:
        livro_escolhido = livros[escolha - 1]
        print(f"\nEmpréstimo realizado com sucesso!")
        print(f"Solicitante: {nome}")
        print(f"Livro emprestado: {livro_escolhido}")
    else:
        print("Número inválido. Escolha entre 1 e 10.")
else:
    print("Entrada inválida. Por favor, digite um número.")

