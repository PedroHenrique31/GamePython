'''         Jogo da forca
    Novo modulo que dá a opção de um outro jogo, ainda não está pronto, mas já temos know how.
    Obs:Para não ser xecutado automaticamente é preciso definir apenas funções no módulo.
'''
def jogar_forca():

    print("***************************************")
    print("***Bem vindo ao jogo da forca**********")
    print("***************************************")

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