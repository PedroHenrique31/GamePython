'''         Jogo da forca
    Novo modulo que dá a opção de um outro jogo, ainda não está pronto, mas já temos know how.
    Obs:Para não ser xecutado automaticamente é preciso definir apenas funções no módulo.
'''
def jogar_forca():

    print("***************************************")
    print("***Bem vindo ao jogo da forca**********")
    print("***************************************")
    #variáveis de jogo
    palavra_secreta="banana"
    enforcou=False
    acertou=False


    #Game loop
    while(not enforcou and not acertou):
        chute=input("Dá um chute ae: ")

        index=0
        for letra in palavra_secreta:
            if(chute==letra):
                print("Encontrei a letra {} na posição {}".format(chute,index))
            #print("index= ",index)
            index = index+1
        print("Jogando...")
    print("Fim de Jogo!!!\n")
'''
        IMPORTANTE
    Chamada recursiva do módulo, esse if é o que permite a execução do modulo individualmente pelo interpretador
python, uma vez que você chama um modulo ele é guardado na variável __name__, sem essa diretiva o modulo main que será
executado seria somente GameSelector, com essa chamada do modulo para sua propria função podemos portanto executá-lo
separadamente da função GameSelector.
'''
if(__name__=="__main__"):
    jogar_forca()