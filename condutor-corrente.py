tensao_rede = int(input("Digite a tensão da rede(127 ou 220):"))

total_potencia = 0

while True:
    if tensao_rede != 127 and tensao_rede != 220:
        print("TENSÃO DE REDE INVALIDA. DIGITE 127 OU 220. ")
        tensao_rede = int(input("Digite a tensão da rede(127 ou 220):"))

    elif tensao_rede == 127:

        aparelho = input('Digite o nome do equipamento: (DIGITE "X" PARA SAIR)')
        if aparelho == 'X' or aparelho == 'x':
            break
        potencia = int(input(f"Digite a potencia do(a) {aparelho}: "))
        total_potencia += potencia

corrente = total_potencia / 127

if corrente PAREI AQUI

print(total_potencia)
print(corrente)