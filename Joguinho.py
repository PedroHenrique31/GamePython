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
total_tentativas=2
rodada=1

for rodada in range(1,total_tentativas+1):
    rodada_str=str(rodada)
    total_tentativas_str=str(total_tentativas)
    #não entendi porque tem que ser .format() mas só funcionou assim
    print("===> Tentativa {} de {}".format(rodada,total_tentativas))
    chute_str=input("Dá seu chute ae entre 1 e 10 milhões\n")
    #print("Você está certo de que é ",chute_str,"?\n")
    chute=int(chute_str)
    if((chute<1) or (chute>10000000)):
        print("ENTRE 1 E 10 MILHÕÕÕES!!\n")
        continue#esse comando diferentemente do break não sai do laço, ele apenas pula essa iteração


    ''' Valores booleanos criados diretamente fora, para facilitar a leitura, nunca pensei em fazer
        isso em outra linguagem
    '''
    acertou=(chute==numero_secreto)
    maior=(chute>numero_secreto)
    menor=(chute<numero_secreto)

    if(acertou):
        print("Ae mizeravi\n")
        break
    else:
        if(maior):
            print("Você errou! foi muito longe\n")
        elif(menor):
            print("Você errou! muito baixo\n")

    rodada=rodada+1
print("Fim de Jogo")
