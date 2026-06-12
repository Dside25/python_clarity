from random import randint
import time

# ============================
# SISTEMA DE RECORDE
# ============================

recorde = 0

try:
    arquivo = open("recorde.txt", "r")
    recorde = int(arquivo.read())
    arquivo.close()
except:
    recorde = 0

# ============================
# MENU PRINCIPAL
# ============================

while True:

    print("\n" + "=" * 40)
    print("🎯      JOGO DA ADIVINHAÇÃO      🎯")
    print("=" * 40)
    print("1 - Jogar")
    print("2 - Ver Recorde")
    print("3 - Regras")
    print("4 - Sair")

    opcao = input("\nEscolha uma opção: ")

    # ============================
    # JOGAR
    # ============================

    if opcao == "1":

        print("\n===== NOVO JOGO =====")

        nome = input("Digite seu nome: ")

        print("\nEscolha a dificuldade:")
        print("1 - Fácil")
        print("2 - Médio")
        print("3 - Difícil")
        print("4 - Insano")

        dificuldade = input("Opção: ")

        if dificuldade == "1":
            limite = 50
            chances = 10
        elif dificuldade == "2":
            limite = 100
            chances = 8
        elif dificuldade == "3":
            limite = 500
            chances = 6
        elif dificuldade == "4":
            limite = 1000
            chances = 4
        else:
            print("Dificuldade inválida.")
            continue

        numero_secreto = randint(0, limite)

        historico = []

        pontos = 0

        print("\nSorteando número...")
        print(f"Adivinhe um número entre 0 e {limite}")

        inicio = time.time()

        venceu = False

        while chances > 0:

            chute = input("\nSeu chute: ")

            if not chute.isnumeric():
                print("Digite apenas números.")
                continue

            chute = int(chute)

            historico.append(chute)

            chances -= 1

            if chute == numero_secreto:

                venceu = True

                fim = time.time()
                tempo_total = fim - inicio

                pontos = (chances * 100)

                if tempo_total <= 15:
                    pontos += 500
                elif tempo_total <= 30:
                    pontos += 250

                print("\n🏆 PARABÉNS!")
                print("VOCÊ ACERTOU!")

                print(f"\nNúmero sorteado: {numero_secreto}")
                print(f"Tempo: {tempo_total:.2f} segundos")
                print(f"Pontos: {pontos}")

                break

            distancia = abs(chute - numero_secreto)

            print("\n❌ Você errou.")

            if chute > numero_secreto:
                print("Dica: o número é MENOR.")
            else:
                print("Dica: o número é MAIOR.")

            if distancia <= 5:
                print("🔥 MUITO QUENTE!")
            elif distancia <= 15:
                print("🌡️ QUENTE!")
            elif distancia <= 30:
                print("❄️ FRIO!")
            else:
                print("🧊 MUITO FRIO!")

            print(f"Chances restantes: {chances}")

            print("Histórico de chutes:")
            print(historico)

        if not venceu:

            fim = time.time()
            tempo_total = fim - inicio

            print("\n💀 FIM DE JOGO")
            print(f"O número era: {numero_secreto}")
            print(f"Tempo jogado: {tempo_total:.2f} segundos")

        # ============================
        # RELATÓRIO FINAL
        # ============================

        print("\n" + "=" * 40)
        print("📊 RELATÓRIO DA PARTIDA")
        print("=" * 40)

        print(f"Jogador: {nome}")
        print(f"Número sorteado: {numero_secreto}")
        print(f"Chutes realizados: {len(historico)}")
        print(f"Histórico: {historico}")

        if venceu:
            print("Resultado: VITÓRIA")
            print(f"Pontuação: {pontos}")
        else:
            print("Resultado: DERROTA")

        # ============================
        # RECORDES
        # ============================

        if pontos > recorde:

            recorde = pontos

            arquivo = open("recorde.txt", "w")
            arquivo.write(str(recorde))
            arquivo.close()

            print("\n🏅 NOVO RECORDE!")
            print(f"Recorde atual: {recorde} pontos")

    # ============================
    # VER RECORDE
    # ============================

    elif opcao == "2":

        print("\n🏅 RECORDE ATUAL")
        print(f"{recorde} pontos")

    # ============================
    # REGRAS
    # ============================

    elif opcao == "3":

        print("\n===== REGRAS =====")
        print("- Escolha uma dificuldade.")
        print("- Tente descobrir o número secreto.")
        print("- Você recebe dicas de maior ou menor.")
        print("- Existe sistema de QUENTE e FRIO.")
        print("- Quanto mais chances sobrando, mais pontos.")
        print("- Quanto mais rápido você vencer, mais pontos.")
        print("- O melhor resultado fica salvo como recorde.")

    # ============================
    # SAIR
    # ============================

    elif opcao == "4":

        print("\nObrigado por jogar!")
        print("Até a próxima!")
        break

    else:
        print("\nOpção inválida.")
