'''
                Projeto de jogo de advinhação
    Como parte do curso de pyhton da alura cursos online tenho feito esse jogo de advinhação
é um conceito simples mas bastante escalável.
'''
print("####################################################################")
print("################### Jogo de advinhação #############################")
print("####################################################################")

# Variaveis de jogo
numero_secreto=42
total_tentativas=5
rodada=1

while(rodada<=total_tentativas):
    print("Tentativa {} de {}",rodada,total_tentativas)
    chute_str=input("Dá seu chute ae\n")
    print("Você está certo de que é ",chute_str,"?\n")
    chute=int(chute_str)

    acertou=(chute==numero_secreto)
    maior=(chute>numero_secreto)
    menor=(chute<numero_secreto)

    if(acertou):
        print("Ae mizeravi\n")
    else:
        if(maior):
            print("Você errou! foi muito longe\n")
        elif(menor):
            print("Você errou! muito baixo\n")

    rodada=rodada+1

