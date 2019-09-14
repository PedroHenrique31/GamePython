'''
                Projeto de jogo de advinhação
    Como parte do curso de pyhton da alura cursos online tenho feito esse jogo de advinhação
é um conceito simples mas bastante escalável.
    O conceito de pontos será feito de forma invertida, o jogador começa com mil pontos que vão sendo subtraídos
conforme o tamanho do erro do jogador.
'''
#TODO:A senha e o número para invocar o cheet estão iguais, melhor corrigir isso, para nao soprar direto.
import random

print("####################################################################")
print("################### Jogo de advinhação #############################")
print("####################################################################")

'''     Predefinições do jogo
    Definições importantes de ambiente, antes do jogo se iniciar,
    Variáveis e funções para tratar excessões
'''
#numero_secreto=round(random.random()*100)
numero_secreto=random.randrange(1,101)#agora gera numeros aleatorios entre 0 e 100
total_tentativas=2
rodada=1
cheet=4096
pontos=1000
#cheetou=(chute==cheet)


#Agora uma pequena função de cheet para testar o jogo
def resp(codigo):
    senha=4096
    if(codigo==senha):
        print("Numero_secreto= ", numero_secreto)
    else:
        print("Numero_secreto= Achou que ia ter respota né... raaa\n")
#TODO:Criar uma função para selecionar esses níveis dinamicamente, assim o usuário pode por qualquer número e ele será ajustável
print("Selecione nível de dificuldade\n(1)Fácil (2)Médio (3)Difícil\n")
nivel=int(input("Digite o nível:"))
if(nivel==1):
    total_tentativas=9
elif(nivel==2):
    total_tentativas=5
else:
    total_tentativas=3


'''     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Engine do jogo em si
'''
for rodada in range(1,total_tentativas+1):
    rodada_str=str(rodada)
    total_tentativas_str=str(total_tentativas)
    #não entendi porque tem que ser .format() mas só funcionou assim
    print("===> Tentativa {} de {}".format(rodada,total_tentativas))
    chute_str=input("Dá seu chute ae entre 1 e 100\n")
    #print("Você está certo de que é ",chute_str,"?\n")
    chute=int(chute_str)
    cheetou = (chute == cheet)
    if (cheetou):  # invocação do cheet
        resp(chute)
    elif((chute<1) or (chute>100)):
        print("ENTRE 1 E 100 CEEEEEM!!\n")
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
        if (cheetou):  # invocação do cheet
            resp(chute)
        elif(maior):
            print("Você errou! foi muito longe\n")
        elif(menor):
            print("Você errou! muito baixo\n")
        pontos_perdidos=abs(numero_secreto-chute)
        pontos=pontos-pontos_perdidos

    rodada=rodada+1
print("Fim de Jogo!!!\nVocê fez:{}\nO número era {}".format(pontos,numero_secreto))
