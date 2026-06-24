memoria_principal = [format(i, '05b') for i in range(32)]
memoria_cache = [None for _ in range(4)]

opcao = input("[B] Buscar  [P] Parar  Selecione: ").upper()
while opcao != "P":
    if opcao == "B":
        busca = input("Digite o endereço (TTLLC): ")

        if len(busca) != 5:
            print("Endereço inválido. Use 5 bits no formato TTLLC, sem espaços.")
        
        else: 
            tag = busca[0:2]
            linha = int(busca[2:4], 2)
            conteudo = memoria_cache[linha]

            conteudo_linha = []
            for i in memoria_principal:
                if i[0:4] == busca[0:4]:
                    conteudo_linha.append(i)

            if conteudo is not None and conteudo[0:2] == tag: 
                print(f"Hit na linha {format(linha, '02b')}\n")
                memoria_cache[linha] = memoria_principal[int(busca, 2)]
                
        
            else:
                print(f"Miss na linha {format(linha, '02b')}\n")
                memoria_cache[linha] = memoria_principal[int(busca, 2)]
                

            print("Memória cache:")
            for i in range(len(memoria_cache)):
                if memoria_cache[i] is None:
                    print(f"Linha: {format(i, '02b')}  Tag: --  Célula: --")
                else:
                    print(f"Linha: {format(i, '02b')}  Tag: {memoria_cache[i][0:2]}  Célula: {memoria_cache[i][-1]}")
            print(f"\nCélulas da linha {format(linha, '02b')}: {conteudo_linha}")

    else:
        print("Opção inválida. Tente novamente.")

    opcao = input("\n[B] Buscar  [P] Parar  Selecione: ").upper()