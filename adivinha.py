from random import randint

print("#####    Iniciando o Jogo!   #####")


random = randint(0, 100)
chute = 01
chances = 10

# < MENOR
# > MAIOR
# == IGUAL
# != DIFERENTE
# >= MAIOR OU IGUAL
# <= MENOR OU IGUAL

while chute != random  :
    chute = input("Chute um numero entre 0 e 100\nR:")
    if chute.isnumeric() :
        chute  = int(chute) 
        chances = chances - 1
        if chute == random :
            print("")
            print("PARABENS VOCE GANHOU! O NUMERO ERA {} E VOCE AINDA TINHA {} CHANCES.".format(random, chances))
            print("")
            break
        else : 
            print()
            if chute > random :
                print("VOCÊ ERROU! Dica: É um numero menor")
            else :
                print("VOCÊ ERROU! Dica: É um numero maior")
            print("Você possui ainda {} chances".format(chances))
            print("")
        if chances == 0 :
            print()
            print("Suas chances acabaram, você perdeu! ONumero era: {}".format(random))
            print("")
            break
    
    
    int("#####    FIM DE JOGO!     #####")

