menu = '''
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

'''

saldo = 0
extrato = '='*10 + 'EXTRATO' + '='*10
limite = 500
LIMITE_SAQUES = 3
saques_realizados = 0

while True:

    opcao = input(menu)
    if opcao == 'd':
        valor = int(input('Digite o quanto quer depositar: '))
        saldo+=valor
        print('Depósito realizado com sucesso!')
        extrato+=f'\nDepósito: R${valor:.2f}'

    elif opcao == 's':
        if saldo>0:
            if saques_realizados<LIMITE_SAQUES:
                valor = int(input('Digite o valor do saque: '))
                if saldo>valor and limite>=valor:
                    saldo-=valor
                    print('Saque realizado com sucesso!')
                    extrato+=f'\nSaque: R${valor:.2f}'
                    saques_realizados+=1
                else:
                    print('Não foi possível continuar. Valor digitado é maior que o saldo/limite.')
            else:
                print('Não foi possível continuar. Limite diário de saques atingido.')
        else:
            print('Não foi possível continuar. Saldo em conta é igual a zero.')

    elif opcao == 'e':
        print(extrato + f'\nSaldo atual: R${saldo:.2f}')
        print('='*27)

    elif opcao == 'q':
        break

    else:
        print('Opção inválida. Tente novamente.')