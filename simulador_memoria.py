def conversao_binario_decimal(binario):
    decimal = int(binario[0])*8 + int(binario[1])*4 + int(binario[2])*2 + int(binario[3])
    return decimal

memoria = ["0"*8 for _ in range(16)]

operacao = input('''Operações: [W] Escrever  [R] Ler  [L] Listar memória [P] Parar 
Selecionar: ''').upper()

while operacao != "P":

    # Operação de escrita
    if operacao == "W":
        endereco =input("Digite o endereço (4 bits): ")
        dado = input("Digite o dado (8 bits): ")
        if len(endereco) == 4 and len(dado) == 8:
            memoria[conversao_binario_decimal(endereco)] = dado
        else:
            print("Endereço ou dado inválido. Tente novamente")

    # Operação de leitura
    elif operacao == "R":
        endereco =input("Digite o endereço (4 bits): ")
        if len(endereco) == 4:
            print(f"Conteúdo: {memoria[conversao_binario_decimal(endereco)]}")
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