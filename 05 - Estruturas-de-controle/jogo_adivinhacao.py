import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativas = 0

    print("=== Jogo de Adivinhação ===")
    print("Tente adivinhar o número de 1 a 10.")

    while True:
        try:
            chute = int(input("Digite seu palpite: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        tentativas += 1

        if chute == numero_secreto:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativa(s).")
            break
        elif chute < numero_secreto:
            print("O número é maior. Tente novamente.")
        else:
            print("O número é menor. Tente novamente.")

        if tentativas >= 5:
            print(f"Fim de jogo! O número secreto era {numero_secreto}.")
            break

jogo_adivinhacao()
