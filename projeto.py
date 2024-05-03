menu = f"""

[1] Depositar
[2] Sacar
[3] Extrato
[Q] Sair

"""
deposito = 0
saldo = 0 
saque = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        
        print("Deposito")
        val_saldo = float(input("Digite o valor do deposito: "))
        if val_saldo > 0:
            saldo += val_saldo
            extrato += f"Deposito: R$ {val_saldo: .2f}\n"
        
        else: 
            print("Valor de saldo invalido!")

    elif opcao == "2":
        print("Saque")
        saque = float(input("Qual valor do saque: "))
        if saque > saldo:
            print("Não é possivel realizar saque por falta de saldo!")

        elif saque > limite:
            print("Operação falhou. Limite diario de saque é R$500,00")

        elif numero_saques >= LIMITE_SAQUES:
            print("Voce ultrapassou o limite diario de 3 tentativas!")

        elif saque > 0:
            saldo -= saque
            numero_saques += 1
            extrato += f"Saque: R$ {saque:.2f}\n"
                
        else:
            print("Operação falhou. Valor informado é invalido!")       
             

    elif opcao == "3":
        print("\n========= Extrato ===========")
        if extrato == "" or extrato == 0:
            print("Não foram realizadas movimentações!")
        else:    
            print(deposito)
            print(extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "Q":
        break

    else:
        print("Operação invalida, por favor, selecione novamente a operação desejada.")