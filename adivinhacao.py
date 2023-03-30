import random


def jogar():
    print("******************************")
    print("Welcome to Guess the number!")
    print("******************************")

    numero_secreto = round(random.random() * 100)
    total_de_tentativas = 0
    pontos = 1000

    print("LEVELS")
    print("(1) Easy - 20 attempts \
          (2) Normal - 10 attempts \
          (3) Difficult - 5 attempts \
          (4) Impossible - 1 attempt")

    nivel = int(input("Choose a level: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    elif (nivel == 3):
        total_de_tentativas = 5
    else:
        total_de_tentativas = 1

    print(numero_secreto)

    for rodada in range(1, total_de_tentativas + 1):
        print("Attempt {} of {}".format(rodada, total_de_tentativas))
        chute_str = input("Choose a number between 1 and 100: ")
        print("You typed ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("You must type a number between 1 and 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Congrats! You got it and scored {} points!".format(pontos))
            break
        else:
            if (maior):
                print("Oh no! Your guess was too high.")
            elif (menor):
                print("Oh no! Your guess was too low.")
            pontos_perdidos = numero_secreto - chute
            pontos = pontos - pontos_perdidos

    # print("You attemps are over! Start again!")
    # print("The number was {}".format(numero_secreto))
    print("Gameover")


if (__name__ == "__main__"):
    jogar()
