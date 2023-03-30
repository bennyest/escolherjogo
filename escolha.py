import forca
import adivinhacao

# "palavras" = words
#"forca" = hangman
#!adivinhacao" = guess


def escolhe_jogo():
    #choose_game
    print("***************************")
    print("**Please choose your game**")
    print("***************************")

    print("(1) Hangman (2) Guess the number")

    jogo = int(input("Which game? "))

    if (jogo == 1):
        print("Starting 'Hangman'")
        forca.jogar()
    elif (jogo == 2):
        print("Starting 'Guess the number'")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()