print("**********************************************")
print("  Advinhação do numero")
print("**********************************************")

numero_secreto = 43

chute_str = input("Digite o seu numero : ")

print("Voce digitou  : ", chute_str)
chute = int (chute_str)
if(numero_secreto==chute):
    print("Voce acertou")
else:
    if(chute>numero_secreto):
        print("Voce errou !!! , seu chute foi maior do que o numero secreto")
    if(chute<numero_secreto):
        print("Voce errou !!! ,  seu chute foi menor do que o numero secreto")

print("Fim de jogo")