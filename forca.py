'''         Jogo da forca
    Novo modulo que dá a opção de um outro jogo, ainda não está pronto, mas já temos know how.
    Obs:Para não ser xecutado automaticamente é preciso definir apenas funções no módulo.
'''
import random
def jogar_forca():

    print("***************************************")
    print("***Bem vindo ao jogo da forca**********")
    print("***************************************")

    #Lê de um arquivo as palavras para o jogo
    with open("palavras.txt","r") as arquivo
    palavras=[]

    for linha in arquivo:
        linha=linha.strip()
        palavras.append(linha)
    print(palavras)

    palavra_sorteada=random.randrange(0,len(palavras))
    #variáveis de jogo
    palavra_secreta=palavras[palavra_sorteada].upper()
    tamanho_chances=6
    letra_certa=["_" for letras in palavra_secreta]

    enforcou=False
    acertou=False
    erros=0

    print(letra_certa)  # Imprime a forca pra dar uma previa
    #Game loop
    while(not enforcou and not acertou):

        chute=input("Dá um chute ae: ")
        chute=chute.strip().upper()#tira os espacos e converte tudo pra maiusculo

        posicao=0
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(chute==letra):#letra.upper, tranforma udo em caps lock
                    letra_certa[posicao]=letra
                posicao = posicao+1
        else:
            erros+=1

        acertou=("_" not in letra_certa)
        enforcou=(erros==tamanho_chances)
        print(letra_certa)
    print("Jogando...")
    if(acertou):
        print("Parabéns!!! Você venceu!! ;)\n")
    else:
        print("Você perdeu!!")
    print("Fim de Jogo!!!\n")
'''
        IMPORTANTE
    Chamada recursiva do módulo, esse if é o que permite a execução do modulo individualmente pelo interpretador
python, uma vez que você chama um modulo ele é guardado na variável __name__, sem essa diretiva o modulo main que será
executado somente se GameSelector, com essa chamada do modulo para sua propria função podemos portanto executá-lo
separadamente da função GameSelector.
'''
def carrega_palavras():
    # Lê de um arquivo as palavras para o jogo
    with open("palavras.txt", "r") as arquivo
if(__name__=="__main__"):
    jogar_forca()