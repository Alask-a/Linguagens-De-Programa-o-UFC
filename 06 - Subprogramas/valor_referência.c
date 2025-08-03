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
