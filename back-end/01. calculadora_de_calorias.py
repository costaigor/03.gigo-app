# 1. Coleta de dados
name = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso em kg (ex: 80.5): "))
altura_cm = int(input("Digite sua altura em cm (ex: 175): "))
sexo = input("Digite M/F: ")

#Sistema de IMC

altura_m = altura_cm / 100
imc = peso / (altura_m ** 2)

print(f"\n{name}, o seu IMC é: {imc:.2f}")

#Calculadora_BASAL_Harris-Benedict

basal_m = 88.369 + (13.397 * peso) + (4.799 * altura_cm) - (5.677 * idade)

basal_f = 447.593 + (9.247 * peso) + (3.098 * altura_cm) - (4.330 * idade)

if sexo == "M" or sexo == "m": 
    print(f"Seu gasto calório basal é: {basal_m:.2f} kcal")
elif sexo == "F" or sexo == "f": 
    print(f"Seu gasto calório basal é: {basal_f:.2f} kcal")
else: 
    print("Sexo inválido! Digite M ou F. ")