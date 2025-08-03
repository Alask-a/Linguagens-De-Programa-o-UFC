# Programação Funcional em Python – Soma dos Quadrados dos Números Pares

## Visão Geral

Este projeto demonstra uma solução funcional para um problema clássico usando **Python**. O objetivo é calcular a **soma dos quadrados dos números pares** em uma lista de inteiros, utilizando:

- Recursão para implementar funções.
- Funções de alta ordem (funções que recebem outras funções como parâmetro).
- Abordagem funcional, evitando estruturas imperativas e laços explícitos.

---

## Descrição do Problema

Dada uma lista de números inteiros, queremos:

1. Filtrar apenas os números pares.
2. Elevar ao quadrado cada número par filtrado.
3. Somar todos os quadrados resultantes.

---

## Abordagem Funcional

Foram implementadas três funções recursivas de alta ordem:

- `filter_func(lst, predicate)` — filtra elementos que satisfazem a condição do predicado.
- `map_func(lst, func)` — aplica uma função a cada elemento da lista.
- `reduce_func(lst, func, initial)` — reduz a lista a um único valor, acumulando com uma função binária.

Funções auxiliares definidas:

- `is_even(n)` — retorna `True` se `n` for par.
- `square(n)` — retorna o quadrado de `n`.
- `sum_func(a, b)` — retorna a soma de `a` e `b`.

---

## Como executar

1. Salve o arquivo com o código em Python (exemplo: `programacao_funcional.py`).
2. Execute no terminal/cmd:

```bash
python programacao_funcional.py
