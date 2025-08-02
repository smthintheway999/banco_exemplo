menu = """
    [d] Depósito
    [s] Saque
    [e] Extrato
    [q] Sair


"""

saldo = 2000
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3
valor_saque = 0
total = 0

eextrato = saldo - valor_saque


while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")



    elif opcao == "s":
        numero_saques +=1
        valor_saque = float(input("\nDigite o quanto você deseja sacar: R$ "))

        if numero_saques <= 3 and valor_saque < limite:
            print(end='')
            
        elif valor_saque > limite:
            if valor_saque / limite <= 3:
                t = int(valor_saque)
                for i in range(0, limite, t):
                    print(end='')
        print(f"\nSeu saque de R${valor_saque:.2f} foi realizado com sucesso e seu saldo é de R${eextrato:.2f}")

            
        

    elif opcao == "e":
        print(f"\nSeu extrato é R${eextrato:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")



    
