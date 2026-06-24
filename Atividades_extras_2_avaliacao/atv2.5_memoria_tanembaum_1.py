def conversao_binario_decimal(binario):
    decimal = 0
    for i in range(len(binario)):
        decimal += int(binario[i]) * (2 ** (len(binario) - 1 - i))
    return decimal

memoria = [[0]*11 for _ in range(11)]
operacao = input("Selecione: [W] Escrever  [R] Ler  [L] Listar memória [P] Parar ").upper()

while operacao != "P":

    # Operação de escrita
    if operacao == "W":

        endereco = list(map(str, input("Digite o endereço (linha,coluna): ").split(",")))
        dado = int(input("Digite o dado (1 bit): "))
        if len(endereco) == 2 and conversao_binario_decimal(endereco[0]) < 11 and conversao_binario_decimal(endereco[1]) < 11 and len(str(dado)) == 1:
            ras = conversao_binario_decimal(endereco[0])
            cas = conversao_binario_decimal(endereco[1])
            memoria[ras][cas] = dado
        else:
            print("Endereço ou dado inválido. Tente novamente")

    # Operação de leitura
    elif operacao == "R":
        endereco = list(map(str, input("Digite o endereço (linha,coluna): ").split(",")))
        if len(endereco) == 2 and conversao_binario_decimal(endereco[0]) < 11 and conversao_binario_decimal(endereco[1]) < 11:
            ras = conversao_binario_decimal(endereco[0])
            cas = conversao_binario_decimal(endereco[1])
            print(f"Conteúdo: {memoria[ras][cas]}")
        else:
            print("Endereço inválido. Tente novamente.")

    # Operação de listar da memória
    elif operacao == "L":
        print("Memória:")
        for i in range(len(memoria)):
            print(f"{format(i, '04b')} - {memoria[i]}")

    else:
        print("Operação inválida. Selecione uma das operações do menu.")
    
    operacao = input("\nSelecione: [W] Escrever  [R] Ler  [L] Listar memória [P] Parar ").upper()

print("Fim do programa.")