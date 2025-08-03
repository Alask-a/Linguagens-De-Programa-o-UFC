# Concorrência com Threads em Python

Este projeto demonstra um exemplo simples de concorrência usando `threading`.

## Diferença entre Threads e Processos

**Threads:**
- Compartilham o mesmo espaço de memória.
- Mais leves e rápidas.
- Requerem cuidados com sincronização.

**Processos:**
- Isolados e independentes.
- Mais seguros, mas mais pesados.
- Comunicação entre eles é mais complexa.

## Exemplo

Executamos duas threads concorrentes que fazem contagem com pausas diferentes para simular execução simultânea.

## Como executar

```bash
python concorrencia_threads.py
```
