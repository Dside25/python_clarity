executar = True
while = executar
    escolhas = '''
        sinal = [    
        {[1] ou [+] para Somar},
        {[2] ou [-] para Subtrair}
        {[3] ou [/] para Dividir},
        {[4] ou [*] para Multiplicar},
        {[5] para Sair},
        {(ou digite sua opção: Somar / Subtrair / Multiplicar / Dividir / Sair)} 
    '''
    print(escolhas)
    operador = input("Qual sua opção?: \nR:")
    valor01 = int(input('Escolha seu primeiro numero: \nR:'))
    valor02  = int(input('Escolha seu primeiro numero: \nR:'))
    
textinho02 = '''
    [1] Não, desejo sair!
    [2] Sim, desejo realizar outro calculo
'''
# -------------- Soma -----------------#
if operador == "1" or operador == "+" or operador == "somar" :
    resultado = valor01 + valor02
    print(f'Resultado é: {resultado} \n')
    print(textinho02)
    operador = input('Deseja realizar outra conta?\nR:')
    if operador == "1" :
        executar = False
        
# -------------- Subtrair -----------------#
if operador == "2" or operador == "-" or operador == "subtrair" :
    resultado = valor01 - valor02
    print(f'Resultado é: {resultado} \n')
    print(textinho02)
    operador = input('Deseja realizar outra conta?\nR:')
    if operador == "1" :
        executar = False

# -------------- Divisão -----------------#
if operador == "3" or operador == "/" or operador == "Dividir" :
    resultado = valor01 / valor02
    print(f'Resultado é: {resultado} \n')
    print(textinho02)
    operador = input('Deseja realizar outra conta?\nR:')
    if operador == "1" :
        executar = False
        
# -------------- Multiplicacao -----------------#
if operador == "34" or operador == "*" or operador == "Multiplicar" :
    resultado = valor01 * valor02
    print(f'Resultado é: {resultado} \n')
    print(textinho02)
    operador = input('Deseja realizar outra conta?\nR:')
    if operador == "1" :
        executar = False