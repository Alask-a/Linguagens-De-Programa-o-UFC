import threading
import time

def contar(nome, tempo):
    for i in range(1, 6):
        print(f"{nome} contando: {i}")
        time.sleep(tempo)
    print(f"{nome} terminou!")

thread1 = threading.Thread(target=contar, args=("Thread A", 1))
thread2 = threading.Thread(target=contar, args=("Thread B", 0.5))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Contagem concorrente finalizada.")
