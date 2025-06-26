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


'''class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} - {self.autor}"


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
    print("Entrada inválida. Por favor, digite um número.")'''

'''class Fruta:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


frutas = [
    Fruta("Maçã"),
    Fruta("Banana"),
    Fruta("Laranja"),
    Fruta("Uva")
]


print("Lista de Frutas Disponíveis na Feira:\n")
for i, fruta in enumerate(frutas, 1):
    print(f"{i}. {fruta}")

nome = input("\nDigite seu nome: ")

escolha = input("Escolha o número da fruta que deseja (1-4): ")


opcoes_validas = [str(i) for i in range(1, len(frutas)+1)]

if escolha in opcoes_validas:
    fruta_escolhida = frutas[int(escolha) - 1]
    print("\n Compra realizada com sucesso!")
    print(f"Cliente: {nome}")
    print(f"Fruta escolhida: {fruta_escolhida}")
else:
    print("\nOpção inválida. Por favor, selecione um número entre 1 e", len(frutas))

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone, email):
        contato = {
            "nome": nome,
            "telefone": telefone,
            "email": email
        }
        self.contatos.append(contato)
        print(f"Contato '{nome}' adicionado com sucesso!")

    def listar_contatos(self):
        if not self.contatos:
            print("Agenda vazia.")
        else:
            print("Lista de contatos:")
            for c in self.contatos:
                print(f"Nome: {c['nome']}, Telefone: {c['telefone']}, Email: {c['email']}")

    def buscar_contato(self, nome):
        encontrados = [c for c in self.contatos if nome.lower() in c['nome'].lower()]
        if encontrados:
            print(f"Contatos encontrados para '{nome}':")
            for c in encontrados:
                print(f"Nome: {c['nome']}, Telefone: {c['telefone']}, Email: {c['email']}")
        else:
            print(f"Nenhum contato encontrado com o nome '{nome}'.")


agenda = Agenda()

agenda.adicionar_contato("Ana Silva", "1111-2222", "ana@email.com")
agenda.adicionar_contato("João Pedro", "3333-4444", "joao@email.com")

agenda.listar_contatos()

agenda.buscar_contato("ana")'''


class Pessoa:
    def __init__(self, nome, id_pessoa):
        self.nome = nome
        self.id_pessoa = id_pessoa
    def __str__(self):
        return f"{self.nome} (ID: {self.id_pessoa})"

class Aluno(Pessoa):
    pass

class Professor(Pessoa):
    pass

class Curso:
    def __init__(self, nome_curso, codigo):
        self.nome_curso = nome_curso
        self.codigo = codigo
    
    def __str__(self):
        return f"{self.nome_curso} (Código: {self.codigo})"
    
class SistemaCadastro:
    def __init__(self):
        self.alunos = set()
        self.professores = set()
        self.cursos = set()

    def cadastrar_aluno(self, aluno):
        if aluno in self.alunos:
            print(f"Aluno {aluno} já cadastrado.")
        else:
            self.alunos.add(aluno)
            print(f"Aluno {aluno} cadastrado com sucesso!")

    def cadastrar_professor(self, professor):
        if professor in self.professores:
            print(f"Professor {professor} já cadastrado.")
        else:
            self.professores.add(professor)
            print(f"Professor {professor} cadastrado com sucesso!")

    def cadastrar_curso(self, curso):
        if curso in self.cursos:
            print(f"Curso {curso} já cadastrado.")
        else:
            self.cursos.add(curso)
            print(f"Curso {curso} cadastrado com sucesso!")

    def listar_alunos(self):
        print("\n--- Lista de Alunos ---")
        for aluno in self.alunos:
            print(aluno)

    def listar_professores(self):
        print("\n--- Lista de Professores ---")
        for prof in self.professores:
            print(prof)

    def listar_cursos(self):
        print("\n--- Lista de Cursos ---")
        for curso in self.cursos:
            print(curso)


sistema = SistemaCadastro()


aluno1 = Aluno("Carlos Silva", "2023001")
aluno2 = Aluno("Maria Oliveira", "2023002")

prof1 = Professor("Ana Souza", "1001")
prof2 = Professor("Bruno Lima", "1002")

curso1 = Curso("Matemática", "MATH101")
curso2 = Curso("História", "HIST202")

sistema.cadastrar_aluno(aluno1)
sistema.cadastrar_aluno(aluno2)
sistema.cadastrar_professor(prof1)
sistema.cadastrar_professor(prof2)
sistema.cadastrar_curso(curso1)
sistema.cadastrar_curso(curso2)
