print("**********************************************")
print("  Advinhação do numero")
print("**********************************************")


numero_secreto = 43
total_de_tentativas = 3
rodada = 1
total_tentativas = total_de_tentativas
while(total_de_tentativas > 0):
    # Print trabalhando a interpolação de strings
    print("Tentativa {} de {}" .format(rodada,total_tentativas))
    chute_str = input("Digite o seu numero : ")
    print("Voce digitou  : ", chute_str)
    # Transformando o chute informado em numero inteiro .
    chute = int (chute_str)
    if(numero_secreto==chute):
        print("Voce acertou")
        total_de_tentativas = 0
    else:
        if(chute>numero_secreto):
            print("Voce errou !!! , seu chute foi maior do que o numero secreto")
        if(chute<numero_secreto):
            print("Voce errou !!! ,  seu chute foi menor do que o numero secreto")
    total_de_tentativas = total_de_tentativas - 1
    rodada = rodada +1
print("Fim de jogo")