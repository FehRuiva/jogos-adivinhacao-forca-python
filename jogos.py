
import forca
import adivinhacao5

def escolhe_jogo():
    print("**********************************")
    print("********ESCOLHA SEU JOGO!*********")
    print("**********************************")


    print("(1) Forca (2) Advinhação")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao5.jogar()
if(__name__ == "__main__"):
    escolhe_jogo()
