total_potencia = 0
tensao_rede = int(input("Digite a tensão da rede(127 ou 220):"))
while True:

    if tensao_rede != 127 and tensao_rede != 220:
        print("TENSÃO DE REDE INVALIDA.")
        tensao_rede = int(input("Digite a tensão da rede(127 ou 220):"))

    elif tensao_rede == 127 or tensao_rede == 220:

        aparelho = input('Digite o nome do equipamento: (DIGITE "X" PARA SAIR)')
        if aparelho.lower() == 'x':
            break
        potencia = int(input(f"Digite a potencia do(a) {aparelho}: "))
        total_potencia += potencia

corrente = total_potencia / tensao_rede

match corrente:
    case 0.5: var = total_potencia / tensao_rede

"""if 0 < corrente <= 9:
    print(" CABO A SER UTILIZADO: 0.5 mm²")

elif 9.1 < corrente <= 11:
    print(" CABO A SER UTILIZADO: 0.75 mm²")

elif 11 < corrente <= 14:
    print(" CABO A SER UTILIZADO: 1.00 mm²")

elif 14 < corrente <= 17.5:
    print(" CABO A SER UTILIZADO: 1.50 mm²")

elif 17.5 < corrente <= 24:
    print(" CABO A SER UTILIZADO: 2.50 mm²")

elif 24 < corrente <= 32:
    print(" CABO A SER UTILIZADO: 4.00 mm²")

elif 32 < corrente <= 41:
    print(" CABO A SER UTILIZADO: 6.00 mm²")

elif 41 < corrente <= 57:
    print("CABO A SER UTILIZADO: 10.00 mm²")"""

print(f"POTÊNCIA TOTAL DOS EQUIPAMENTOS: {total_potencia}")
print(f"CORRENTE: {corrente:.2f}")
