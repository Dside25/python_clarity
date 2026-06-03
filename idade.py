executar = True
while executar :
    anoNasc = int(input("Em que ano você nasceu? \nR:"))
    anoAtual = int(input ("Em que ano estamos? \nR:"))
    idade = anoAtual - anoNasc
    print('Você tem: ' + str(idade) + ' anos')
    input('\n Desejar testar novamente? \n[1]Sim \n[2] Não\nR:')
    if opcao == "2" or opcao == "Não" :
        executar = False