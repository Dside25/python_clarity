def divisao(a, b):
    try:
        resultado = a / b
        print(f"O resultado da divisão de {a} por {b} é {resultado}")
    except ZeroDivisionError:
        print("Erro: Não é possivel dividir por zero.")
    except TypeError:
        print("Erro: Todos os valores devem ser numeros.")
    except Exception as e:
        print(f"Erro inesperado {e}") 
    else:
        print("Divisão realizado com sucesso!")   
    finally:
        # O Bloco Finally sempre será executado, independente de erro ou sucesso
        print("Processo de divisão concluido.")


#teste 01: Divisão Normal

print("\n--- Teste 01 ---\n")
divisao(10,2)

#teste 02: Divisão por 0

print("\n--- Teste 02 ---\n")
divisao(10,0)

#teste 03: Divisão com tipos invalidos

print("\n--- Teste 03 ---\n")
divisao(10,"dois")

#teste 01: Divisão com erro inesperado

print("\n--- Teste 04 ---\n")
divisao("dez",2)