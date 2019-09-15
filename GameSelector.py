'''         Game Selector
    Novo módulo para selecionar qual jogo o usuário optou por jogar, este modlo sincorniza entre as classes.

'''
import forca
import Joguinho


print("*************************************")
print("******** OLÁÁÁ!! Temos vários Jogos!\n")
print("******* Escolha seu jogooo************")

print("(1)Forca (2)Advinhação")
jogo=int(input("Qual a sua escolha? "))

if(jogo==1):
    print("Então é forca!")
    forca.jogar_forca()
elif (jogo==2):
    print("Então vai ser advinhação!!")
    Joguinho.jogar_advinhacao()
print("Obrigado e até logo!! ;-)\n")