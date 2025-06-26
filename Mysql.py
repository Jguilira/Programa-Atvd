import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "teste"
)

cursor = conexao.cursor()
"""cursor.execute('''create table usuarios(
                id int primary key auto_increment,
                nome varchar(75) not null,
                senha varbinary(100) not null
               );''')
for i in cursor:
    print(i)"""

'''nome = input('Informe seu nome: ')
senha = int(input('Informe a senha: '))
banco = ('insert into usuarios (nome, senha) values (%s, %s)')
valores = (nome,senha)
cursor.execute(banco,valores)
conexao.commit()
print(f'Bem vindo {nome}')'''

'''nome = input('Informe seu nome: ')
senha = int(input('Informe a senha: '))
banco = ('update usuarios set senha = %s where nome = %s')
valores = (senha,nome)
cursor.execute(banco,valores)
conexao.commit()
print(f'Senha alterada com sucesso!')'''

nome = input('Qual você quer apagar?: ')
sql = 'DELETE from usuarios where nome = %s'
valores = (nome, )
cursor.execute(sql, valores)
conexao.commit()
print('Dados apagados!')


cursor.execute('select * from usuarios')
resultado = cursor.fetchall()

for linha in resultado:
    print(linha)

