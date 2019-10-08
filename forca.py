'''         Jogo da forca
    Novo modulo que dá a opção de um outro jogo, ainda não está pronto, mas já temos know how.
    Obs:Para não ser xecutado automaticamente é preciso definir apenas funções no módulo.
'''
import random





def jogar_forca():

    print("***************************************")
    print("***Bem vindo ao jogo da forca**********")
    print("***************************************")

    palavras=carrega_palavras()

    palavra_sorteada=random.randrange(0,len(palavras))#seleciona uma palavra da lista
    #variáveis de jogo
    palavra_secreta=palavras[palavra_sorteada].upper()
    tamanho_chances=7 #TODO: tentar melhorar isso para algo dinamico
    letra_certa=["_" for letras in palavra_secreta]

    enforcou=False
    acertou=False
    erros=0

    print(letra_certa)  # Imprime a forca pra dar uma previa
    #Game loop
    while(not enforcou and not acertou):
        #Apresenta a lê os chutes
        chute=pede_chute()
        #Avalia se tem essa letra na palavra,senão incrementa erros
        if(chute in palavra_secreta):
            avalia_chute(chute,letra_certa,palavra_secreta)
        else:
            erros+=1
            desenha_forca(erros)
        #define o que é considerado um acerto/erro
        acertou=("_" not in letra_certa)
        enforcou=(erros==tamanho_chances)
        print(letra_certa)
    print("Jogando...")
    #Avalia se já ganhou ou não para parar o jogo
    if(acertou):
        imprime_vencedor()
    else:
        imprime_perdedor(palavra_secreta)
    print("Fim de Jogo!!!\n")
###################################### Funções auxiliares de jogo ######################################################
def pede_chute():
    chute=input("Dá um chute ae: ")
    chute = chute.strip().upper()  # tira os espacos e converte tudo pra maiusculo
    return chute


def imprime_vencedor():
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")


def imprime_perdedor(palavra):
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

def carrega_palavras():
    # Lê de um arquivo as palavras para o jogo
    arquivo=open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    return (palavras)

def avalia_chute(chute,letra_certa,palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if (chute == letra):  # letra.upper, tranforma udo em caps lock
            letra_certa[posicao] = letra
        posicao = posicao + 1
def desenha_forca(erros):
        print("  _______     ")
        print(" |/      |    ")

        if (erros == 1):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if (erros == 2):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if (erros == 3):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if (erros == 4):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if (erros == 5):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if (erros == 6):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if (erros == 7):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

'''
        IMPORTANTE
    Chamada recursiva do módulo, esse if é o que permite a execução do modulo individualmente pelo interpretador
python, uma vez que você chama um modulo ele é guardado na variável __name__, sem essa diretiva o modulo main que será
executado somente se GameSelector, com essa chamada do modulo para sua propria função podemos portanto executá-lo
separadamente da função GameSelector.
'''
if(__name__=="__main__"):
    jogar_forca()