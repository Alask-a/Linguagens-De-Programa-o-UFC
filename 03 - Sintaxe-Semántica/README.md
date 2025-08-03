# ExprLang — Gramática e Análise Léxica

Este documento descreve uma linguagem fictícia chamada **ExprLang**, projetada para manipulação de expressões matemáticas simples com variáveis, números e operadores aritméticos.

---

## Gramática Sintática

A seguir está a gramática sintática em BNF simplificada:

```
<programa>       ::= <linha> | <linha> <programa>

<linha>          ::= <definicao> | <avaliacao>

<definicao>      ::= "def" <identificador> "=" <expressao> ";"

<avaliacao>      ::= "calc" <expressao> ";"

<expressao>      ::= <termo> | <expressao> "+" <termo> | <expressao> "-" <termo>

<termo>          ::= <fator> | <termo> "*" <fator> | <termo> "/" <fator>

<fator>          ::= <numero> | <identificador> | "(" <expressao> ")"

<identificador>  ::= letra (letra | dígito)*

<numero>         ::= dígito+
```

---

## Análise Léxica

A análise léxica converte o código fonte em uma lista de **tokens**. Os principais tokens de **ExprLang** incluem:

| Token             | Exemplo         | Descrição                         |
|------------------|-----------------|-----------------------------------|
| `def`            | `def`           | Palavra reservada para definição |
| `calc`           | `calc`          | Palavra reservada para avaliação |
| `identificador`  | `resultado`, `a1`| Nomes de variáveis                |
| `número`         | `42`, `7`       | Valores numéricos inteiros       |
| `+`, `-`, `*`, `/`| `+`, `-`, `*`, `/`| Operadores aritméticos        |
| `=`              | `=`             | Atribuição                        |
| `;`              | `;`             | Final de instrução               |
| `(`, `)`         | `(`, `)`        | Agrupamento de expressões        |

---

## Exemplo de Código ExprLang

```exprlang
def a = 10;
def b = 5;
calc a * (b + 2);
```

### Tokens gerados

| Token            | Valor     |
|------------------|-----------|
| `def`            | "def"     |
| `identificador`  | "a"       |
| `=`              | "="       |
| `número`         | "10"      |
| `;`              | ";"       |
| `def`            | "def"     |
| `identificador`  | "b"       |
| `=`              | "="       |
| `número`         | "5"       |
| `;`              | ";"       |
| `calc`           | "calc"    |
| `identificador`  | "a"       |
| `*`              | "*"       |
| `(`              | "("       |
| `identificador`  | "b"       |
| `+`              | "+"       |
| `número`         | "2"       |
| `)`              | ")"       |
| `;`              | ";"       |

---

## Considerações

- **ExprLang** é orientada à avaliação de expressões matemáticas com sintaxe enxuta.
- Pode ser usada para simular interpretadores simples ou treinar analisadores léxicos/sintáticos.
