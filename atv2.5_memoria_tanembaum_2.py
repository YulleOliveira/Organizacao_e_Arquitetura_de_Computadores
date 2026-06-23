def conversao_binario_decimal(binario):
    decimal = 0
    for i in range(len(binario)):
        decimal += int(binario[i]) * (2 ** (len(binario) - 1 - i))
    return decimal

def selecionar_banco(endereco):
    if endereco[0] == '0':
        return 0
    elif endereco[0] == '1':
        return 1
    else:
        return None

banco0, banco1 = [["0"*4]*13 for i in range(13)], [["0"*4]*13 for i in range(13)]
memoria = [banco0, banco1]
operacao = input("Selecione: [W] Escrever  [R] Ler  [L] Listar memória  [P] Parar ").upper()

while operacao != "P":

    # Operação de escrita
    if operacao == "W":

        endereco = input("Digite o endereço (BLLLLCCCC): ")
        dado = input("Digite o dado (4 bits): ")
        banco_selecionado = selecionar_banco(endereco)
        if banco_selecionado is not None:
            ras = conversao_binario_decimal(endereco[1:5])
            cas = conversao_binario_decimal(endereco[5:9])
            memoria[banco_selecionado][ras][cas] = dado
        else:
            print("Endereço inválido. Tente novamente")

    # Operação de leitura
    elif operacao == "R":
        endereco = input("Digite o endereço (BLLLLCCCC): ")
        banco_selecionado = selecionar_banco(endereco)
        if banco_selecionado is not None:
            ras = conversao_binario_decimal(endereco[1:5])
            cas = conversao_binario_decimal(endereco[5:9])
            print(f"Conteúdo: {memoria[banco_selecionado][ras][cas]}")
        else:
            print("Endereço inválido. Tente novamente.")

    # Operação de listar da memória
    elif operacao == "L":
        opcao = input("Listar: [0] Banco 0  [1] Banco 1  [A] Ambos ").upper()
        if opcao == "0":
            print("Banco 0:")
            for i in range(len(memoria[0])):
                print(f"{format(i, '04b')} - {memoria[0][i]}")

        elif opcao == "1":
            print("Banco 1:")
            for i in range(len(memoria[1])):
                print(f"{format(i, '04b')} - {memoria[1][i]}")

        elif opcao == "A":
            print("Memória:")
            for i in range(len(memoria)):
                print(f"Banco {i}:")
                for j in range(len(memoria[i])):
                    print(f"{format(j, '04b')} - {memoria[i][j]}")
        
        else:
            print("Opção inválida. Tente novamente.")

    else:
        print("Operação inválida. Selecione uma das operações do menu.")
    
    operacao = input("\nSelecione: [W] Escrever  [R] Ler  [L] Listar memória  [P] Parar ").upper()

print("Fim do programa.")