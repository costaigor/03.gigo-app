print("=== BEM-VINDO AO GIGO-APP (Módulo de Saúde) ===")

# BLOCO 1: Coleta de dados
name = input("Digite seu nome: ")
telefone = int(input("Digite seu numero com DDD: "))
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso em kg (ex: 80.5): "))
altura_cm = int(input("Digite sua altura em cm (ex: 175): "))
sexo = input("Digite M/F: ")

print("\n NÍVEL DE ATIVIDADE FÍSICA ---")
print("1 - Sedentário (Pouco ou nenhum exercício)")
print("2 - Levemente Ativo (Exercício leve 1-3 dias/semana)")
print("3 - Moderadamente Ativo (Exercício moderado 3-5 dias/semana)")
print("4 - Altamente Ativo (Exercício pesado 6-7 dias/semana)")
atividade_opcao = input("Escolha o número da sua opção (1 a 4): ")

print("\n-------------------------------------------")
print(f"Processando dados de {name}...")
print("-------------------------------------------\n")

# BLOCO 2: IMC

altura_m = altura_cm / 100
imc = peso / (altura_m ** 2)

if imc < 18.5:
    classificacao_imc = "Abaixo do peso"
elif imc <= 24.9:
    classificacao_imc = "Peso normal"
elif imc <= 29.9:
    classificacao_imc = "Sobrepeso"
else:
    classificacao_imc = "Obesidade"


# BLOCO 3: Cálculo da Taxa Metabólica Basal (TMB)

basal_m = 88.369 + (13.397 * peso) + (4.799 * altura_cm) - (5.677 * idade)

basal_f = 447.593 + (9.247 * peso) + (3.098 * altura_cm) - (4.330 * idade)

if sexo == "M" or sexo == "m":
    tmb = basal_m 
    print(f"Seu gasto calório basal é: {basal_m:.2f} kcal")
elif sexo == "F" or sexo == "f": 
    print(f"Seu gasto calório basal é: {basal_f:.2f} kcal")
    tmb = basal_f
else: 
    print("Sexo inválido! Digite M ou F. ")
    tmb = 0

# BLOCO 4: Cálculo do Gasto Energético Total (GET)

if atividade_opcao == "1":
    fator = 1.2
elif atividade_opcao == "2":
    fator = 1.375
elif atividade_opcao == "3":
    fator = 1.55
elif atividade_opcao == "4":
    fator = 1.725
else:
    fator = 1.0
    print("Opção de atividade inválida! Usando fator padrão (1.0).")

get = tmb * fator

# ==========================================
# 5. Saída de Dados (O Relatório Atualizado)
# ==========================================
print(f"=== RELATÓRIO DE SAÚDE: {name.upper()} ===")
print(f"➔ IMC: {imc:.2f} ({classificacao_imc})")
print(f"➔ Taxa Metabólica Basal (TMB): {tmb:.2f} kcal")
print(f"➔ Gasto Energético Total Diário (GET): {get:.2f} kcal")
print("=======================================")