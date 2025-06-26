'''print("Primeira atvd!")

numero = int(input("Digite um numero se ele é impar ou par:"))
if numero % 2 == 0:
    print("Numero par \n")

else:
    print("numero impar.\n")


print("Segunda atvd!")

numero1 = int(input("Digite qualquer número: "))

if numero1 == 0:
    print("Número é zero!")

elif numero1 > 0:
    print("Número positivo!")

else:
    print("Número negativo!")

print("Terceira atvd!")

print("Questão 5:QUAL A CAPITAL DO PERNAMBUCO:")

print("A - SALVADOR")
print("B - TERESINA")
print("C - RECIFE")
print("D - BOLIVIA")

resposta = str(input("Digite sua resposta:"))

if resposta == "C" or "c":
    print("Resposta CORRETA!!")
else:
    print("Reswposta INCORRETA!!")


print("Quarta atvd!")

senha_cadastro = input("Digite sua senha aqui:")

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))

divisão = num1 // num2

senha_cadastro2 = input("Digite sua senha novamente aqui:")

if senha_cadastro == senha_cadastro2:
    print("Senha correta!\n", divisão)

else:
    print("Senha incorreta!\n")
    print("Aplicativo sendo fechado...")

print("Quinta atvd!!")

kg = int(input("Insira quantos quilos voce pescou:"))
multa= (kg-50)*4

if kg <= 50:
    print("vc esta insento")
else:
    print("Voce pagara uma multa de R$", multa)

print("Sexta atvd")

temp = int(input("Insira a temperatura do seu ambiente:"))

if temp >= 30:
    print("Está quente!")

elif temp < 20:
    print("Está frio!")

else:
    print("Está agradavel")

print("Sétima atvd!")

valor = int(input("Insira um número:"))
valor1 = int(input("Insira um número:"))
valor2 = int(input("Insira um número:"))

if valor <= valor1 and valor <= valor2:
    if valor1 <= valor2:
        print("A ordem crecente é:", valor, valor1, valor2)
    else:
        print("A ordem crecente é:", valor, valor2, valor1)

elif valor1 <= valor and valor1 <= valor2:
    if valor <= valor2:
        print("A ordem crecente é:", valor1, valor, valor2)
    else:
        print("A ordem crecente é:", valor1, valor2, valor)

else:
    if valor <= valor1:
        print("A ordem crecente é:", valor2, valor, valor1)
    else:
        print("A ordem crecente é:", valor2, valor1, valor)

print ("Segunda atividade!!!")

idade = int(input("Insira sua idade aqui:"))

if idade >= 18:
    print("Pode dirigir!")

else:
    print("Não pode dirigir.")

print("ATVD APROVADOOO!!")

nota = float(input("Digite sua nota de 0 a 10:"))

if nota >= 7:
    print("APROVADO!!")

elif nota >= 5:
    print("RECUPERAÇÃO!!")

else:
    print("REPROVADO!!")

print("Calculadora atvd!")

Valor_compra = float(input("Digite o valor da sua compra:"))
desconto = Valor_compra - (Valor_compra * 0.10)
if Valor_compra >= 100:
    print("Valor com desconto:", desconto)

else:
    print("Valor do produto.")

print("Triangulo atvd!!")

lado1 = int(input("Digite um lado do triangulo:"))
lado2 = int(input("Digite um lado do triangulo:"))
lado3 = int(input("Digite um lado do triangulo:"))

if lado1 == lado2 == lado3:
    print("TRIANGULO EQUILÁTERO")

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("TRIANGULO ISÓSCELES")

else:
    print("TRIANGULO ESCALENO")

print("Loja de ingressos!")

idade1 = int(input("Digite sua idade aqui:"))
taxa1 = 10
taxa2 = 20
taxa3 = 15

if idade1 <= 12:
    print("PAGAR A TAXA DE R$", taxa1)

elif idade1 > 59:
    print("PAGAR A TAXA DE R$", taxa3)

elif idade1 >= 12:
    print("PAGAR A TAXA DE R$", taxa2)

print("Intervalo")

numero4 = int(input("Digite um número:"))

if numero4 >= 10 and numero4 <= 50:
    print("O número está dentro do intervalo.")

else:
    print("Não está dentro do intervalo.")

print ("IMC")

peso = float(input("Digite seu peso:"))
altura = float(input("Digite seu altura:"))

imc = peso // (altura** 2)

if imc < 18.5:
    print("Abaixo do peso!")

elif imc >= 18.5:
    print("Peso normal!")

elif imc >= 25:
    print("Sobrepeso!")

elif imc >= 30:
    print("Obesidade!")'''

print ("Bissexto")

ano = int(input("Digite um ano:"))

if ano % 4 == 0 or ano % 400 == 0:
    print("ANO BISSEXTO")
else:
    print("ANO NÃO É BISSEXTO")
