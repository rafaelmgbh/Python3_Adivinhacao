import random

print("**********************************************")
print("  Advinhação do numero")
print("**********************************************")


numero_secreto = random.randrange(1,101)
total_de_tentativas = 3
rodada = 1
total_tentativas = total_de_tentativas

while(total_de_tentativas > 0):
    # Print trabalhando a interpolação de strings
    print("Tentativa {} de {}" .format(rodada,total_tentativas))
    chute_str = input("Digite o seu número entre 1 e 100 : ")
    print("Voce digitou  : ", chute_str)
    chute = int(chute_str)
    if(chute < 1 or chute > 100 ):
        print("Você deve digitar um número entre 1 e 100")
        continue

    # Transformando o chute informado em numero inteiro .

    if(numero_secreto==chute):
        print("Voce acertou")
        break
    else:
        if(chute>numero_secreto):
            print("Voce errou !!! , seu chute foi maior do que o número secreto")
        if(chute<numero_secreto):
            print("Voce errou !!! ,  seu chute foi menor do que o número secreto")
    total_de_tentativas = total_de_tentativas - 1
    rodada = rodada +1
print("Fim de jogo")