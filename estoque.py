# Regras
# Somente variáveis comuns
# estruturas condicionais if/else
# funções nativas (print, etc)
# 1 loop

# Produtos (com objetos e arrays é bem melhor)
beer = 0
whisky = 0
vodka = 0

print("\n!!!======================| BAR DO SEU ZÉ |=====================!!!\n")

estoque_incial = input("Bem vindo! Deseja inserir o estoque inicial? [S | N]: ").upper()
if estoque_incial == "S":
    beer = int(input("Estoque de Cerveja: "))
    whisky = int(input("Estoque de Whisky: "))
    vodka = int(input("Estoque de Vodka: "))
    print("\n> Estoque inicial preenchido, prosseguindo...")

init = True
while init:
    print("\n====================== CONTROLE DE ESTOQUE GERAL DE PRODUTOS DO SEU ZÉ ======================\n")

    userChoice = int(input(
        """O que deseja fazer? (Digite o número correspondente)\n 
        [1] Consultar produtos no estoque
        [2] Atualizar estoque
        [3] Retirar um produto
        [4] Sair...\n"""))
    
    if userChoice == 1:
        print("=========== ESTOQUE TOTAL ===========")
        totalProducts = beer + whisky + vodka
        if totalProducts >= 100:
            print("\n> Se liga no estoque do véio, bonado\n")
        elif totalProducts < 100:
            print("\n> O véi ta póbi, faz favor de comprar os produto\n")

        print(f"Cerveja (Glacial): {beer}")
        print(f"Vodka (Natasha): {vodka}")
        print(f"Whisky (Passaporte falsificado): {whisky}")
        print(f"\n========= Estoque Total: {totalProducts} produtos. ==========")
        
        verify = input("\nDeseja continuar ? [S/N]").upper()
        if verify == "S":
            continue
        else:
            print("> Programa encerrado! Seu zé foi beber pinga...")
            init = False

    if userChoice == 2:
        print("\n> Atualize o estoque dos produtos a seguir...\n")

        beer = int(input("Estoque de Cerveja: "))
        whisky = int(input("Estoque de Whisky: "))
        vodka = int(input("Estoque de Vodka: "))

        verify = input("\nDeseja continuar ? [S/N]").upper()
        if verify == "S":
            continue
        else:
            print("\n> Programa encerrado! Seu zé foi beber pinga...")
            init = False

    if userChoice == 3:
        print("========== RETIRADA DE PRODUTOS DO ESTOQUE ===========")

        print("\n> Escolha um produto para retirar do estoque. CUIDADO!!!\n")

        userRemoveOption = int(input(f"""Produtos em estoque (Digite o número correspondente):
        [1] Cerveja [QTD: {beer}]
        [2] Vodka [QTD: {vodka}]
        [3] Whisky [QTD: {whisky}]\n
        ESCOLHA: """))

        userQtd = int(input("Digite a quantidade a ser retirada: "))
        if userQtd <= 0:
            print("> Seu zé fica nervoso e vai jogar truco com tamanha lerdice")
            break
        
        if userRemoveOption == 1:
            beer = beer - userQtd
            print(f"{userQtd} cervejas removidas...")
            print(f"Estoque restante: [{beer}] cervejas")

        if userRemoveOption == 2:
            vodka = vodka - userQtd
            print(f"\n> {userQtd} vodka removidas...")
            print(f"Estoque restante: [{vodka}] vodka")

        if userRemoveOption == 3:
            whisky = whisky - userQtd
            print(f"{userQtd} whisky removidas...")
            print(f"Estoque restante: [{whisky}] whisky")

        if userRemoveOption == 4:
            print("\n> Seu zé te pegou no flagra roubando as bebidas dele...")
            print("> Ele te cacetou na porrada e te jogou na sarjeta, tente outra vez\n")
            init = False
            break
        
        verify = input("\nDeseja continuar ? [S/N]").upper()
        if verify == "S":
            continue
        else:
            print("\n> Programa encerrado! Seu zé foi beber pinga...")
            init = False

    if userChoice == 4:
        print("> Boa ideia! Adeus!!!")
        print("> Seu zé fecha o bar... e vive feliz pra sempre nos alpes suiços")
        init = False 


