# 1. Coleta de dados
name = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso em kg (ex: 80.5): "))
altura_cm = int(input("Digite sua altura em cm (ex: 175): "))

#Sistema de IMC

altura_m = altura_cm / 100
imc = peso / (altura_m ** 2)

print(f"\n{name}, o seu IMC é: {imc:.2f}")