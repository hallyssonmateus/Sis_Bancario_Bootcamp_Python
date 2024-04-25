menu = f"""

[1] Depositar
[2] Sacar
[3] Extrato
[Q] Sair

"""

saldo = 0
saque = 0
limite = 500
extrato = 0
numero_saques = 0
LIMITE_SAQUES = 3
tot_saques = 0

while True:
    opcao = input(menu)

    if opcao == "1":
        
        print("Deposito")
        val_saldo = float(input("Digite o valor do deposito: "))
        if val_saldo > 0:
            saldo += val_saldo
            deposito += val_saldo
        
        else: 
            print("Valor de saldo invalido!")

    elif opcao == "2":
        print("Saque")
        saque = float(input("Qual valor do saque: "))
        if saldo > 0:            
            if numero_saques <=3:
                extrato += saque
                numero_saques+=1
                saldo -= saque
                if saque <= limite:                
                    tot_saques += saque
                    if tot_saques <= limite*3:
                        print("Voce ultrapasou o limite total diario de R$ 1500,00!")
                else:
                    print("O limite diario de saque é R$500,00")        
            else:
                print("Voce ultrapassou o limite diario de 3 tentativas!")   
        else:
            print("Não é possivel realizar saque por falta de saldo!")

    elif opcao == "3":
        print("Extrato")
        if extrato == "" or extrato == 0:
            print("Não foram realizadas movimentações!")
        else:    
            print(f"Deposito - R$ {deposito}")
            print(f"Extrato - R$ {extrato}")
            print(f"Extrato - R$ {saldo}")

    elif opcao == "Q":
        break

    else:
        print("Operação invalida, por favor, selecione novamente a operação desejada.")