# Estruturas de Controle

## Contexto: Jogo de Adivinhação

Este exemplo implementa um jogo simples onde o jogador deve adivinhar um número entre 1 e 10. O código demonstra o uso de:

### Estruturas de Controle Utilizadas
- **Seleção (if/elif/else)**: para verificar se o palpite está certo, menor ou maior que o número secreto.
- **Repetição (while)**: permite que o jogador continue tentando até acertar ou atingir o número máximo de tentativas.
- **Controle de fluxo (break, continue, try/except)**: usado para interromper o loop ou lidar com erros de entrada.

## Código

```python
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
```
