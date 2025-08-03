# Tipos de Dados nas Linguagens de Programação

Este exemplo compara a tipagem em três linguagens populares: **Python**, **JavaScript** e **C**.

## Critérios de Comparação

| Linguagem   | Tipagem         | Verificação     | Observações                            |
|-------------|------------------|------------------|----------------------------------------|
| Python      | Dinâmica + Forte | Em tempo de execução | Não permite operações inválidas entre tipos incompatíveis |
| JavaScript  | Dinâmica + Fraca | Em tempo de execução | Permite coerção automática de tipos    |
| C           | Estática + Forte | Em tempo de compilação | Requer declaração explícita de tipos   |

---

## Exemplos

### Python

```python
x = 5           
x = "texto"     
def soma(a, b):
    return a + b

print(soma(10, 5))     
print(soma("a", "b"))  
```

### JavaScript

```javascript
let x = 5;
x = "texto";

function soma(a, b) {
    return a + b;
}

console.log(soma(10, 5));     
console.log(soma("a", "b"));  
console.log(soma(10, "5"));   
```

### C

```c
#include <stdio.h>

int soma(int a, int b) {
    return a + b;
}

int main() {
    int x = 5;
    printf("%d\n", soma(10, 5)); 
    return 0;
}
```

---

## Conclusão

- Python e JavaScript permitem redefinir tipos de variáveis, enquanto C exige consistência.
- Em JavaScript, a coerção implícita pode levar a resultados inesperados.
- Em C, erros de tipo são evitados já na compilação.
