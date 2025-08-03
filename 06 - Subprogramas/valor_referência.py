def por_valor(x):
    x += 10
    print("Dentro da função (x):", x)

def por_referencia(lista):
    lista.append(99)
    print("Dentro da função (lista):", lista)

a = 5
print("Antes da função (a):", a)
por_valor(a)
print("Depois da função (a):", a)

b = [1, 2, 3]
print("Antes da função (b):", b)
por_referencia(b)
print("Depois da função (b):", b)
