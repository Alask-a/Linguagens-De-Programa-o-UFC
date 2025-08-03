# Subprogramas: Passagem de Parâmetros por Valor e por Referência

Este projeto demonstra como diferentes linguagens lidam com passagem de parâmetros **por valor** e **por referência**.

## Exemplos Utilizados

### Python (Semântica de objetos)
- Tudo é passado por referência ao objeto, mas tipos imutáveis como inteiros se comportam como valor.
- Listas e dicionários podem ser modificados diretamente.

### C (por valor e simulação de referência com ponteiros)
- A linguagem C passa argumentos **por valor**.
- A referência é simulada usando **ponteiros**.

---

## Python: valor vs referência

```python
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
```

---

## C: valor e referência

```c
#include <stdio.h>

void por_valor(int x) {
    x += 10;
    printf("Dentro da função (x): %d\n", x);
}

void por_referencia(int *x) {
    *x += 10;
    printf("Dentro da função (*x): %d\n", *x);
}

int main() {
    int a = 5;
    printf("Antes da função (a): %d\n", a);
    por_valor(a);
    printf("Depois da função (a): %d\n", a);

    por_referencia(&a);
    printf("Depois da função com ponteiro (a): %d\n", a);

    return 0;
}
```

---

## Conclusão

- Em Python, objetos mutáveis (como listas) podem ser alterados diretamente nas funções.
- Em C, a passagem por referência precisa ser feita explicitamente com ponteiros.

---

## JavaScript: valor e referência

```javascript
function porValor(x) {
    x += 10;
    console.log("Dentro da função (x):", x);
}

function porReferencia(arr) {
    arr.push(99);
    console.log("Dentro da função (arr):", arr);
}

let a = 5;
console.log("Antes da função (a):", a);
porValor(a);
console.log("Depois da função (a):", a);

let b = [1, 2, 3];
console.log("Antes da função (b):", b);
porReferencia(b);
console.log("Depois da função (b):", b);
```

## Conclusão (atualizada)

- **Python**: listas e dicionários são mutáveis, inteiros se comportam como valor.
- **C**: usa ponteiros para simular referência.
- **JavaScript**: primitivos são por valor, objetos são por referência.
