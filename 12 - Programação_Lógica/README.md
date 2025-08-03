# Programação Lógica – Modelo de Genealogia em Prolog

## Visão Geral

Este projeto apresenta uma pequena modelagem de um problema clássico de **programação lógica** usando sintaxe inspirada em Prolog.

O foco é construir uma **árvore genealógica simples** que permite consultar relações familiares como pai, mãe, avô, avó e irmãos.

---

## Objetivo

- Demonstrar a representação de fatos e regras em programação lógica.
- Facilitar o entendimento de como expressar relações familiares de forma declarativa.
- Expor consultas típicas feitas em Prolog para explorar a base de conhecimento.

---

## Descrição do Problema

A genealogia modela as relações familiares entre indivíduos, identificando quem é pai, mãe, avô, avó e irmão de quem, utilizando:

- Fatos (exemplo: `filho(joao, carlos)` indica que João é filho de Carlos).
- Regras para definir conceitos derivados (exemplo: `pai(X,Y)` é quem é homem e tem um filho).

---

## Estrutura do Código

### Fatos básicos

- `filho(Filho, PaiOuMae)`: Indica o filho e seu pai ou mãe.
- `homem(Nome)`: Define o gênero masculino.
- `mulher(Nome)`: Define o gênero feminino.

### Regras definidas

- `pai(Pai, Filho)`: Pai é um homem que tem um filho.
- `mae(Mae, Filho)`: Mãe é uma mulher que tem um filho.
- `avo(AvôOuAvó, Neto)`: Avô ou avó, derivado do pai ou mãe dos pais.
- `irmao(X, Y)`: Dois indivíduos que compartilham os mesmos pais e são diferentes.

---