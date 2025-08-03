# Linguagens para Scripts e Web — Organização Automática de Arquivos

## Visão Geral

Este projeto demonstra o uso prático de uma linguagem de script — Python — para automação simples de tarefas cotidianas no computador. O script fornecido organiza os arquivos dentro de uma pasta, classificando-os automaticamente em subpastas conforme suas extensões (tipos de arquivo).

Esse tipo de automação pode ajudar a manter o ambiente de trabalho, downloads ou qualquer diretório de arquivos mais limpo e organizado, facilitando a localização e gestão dos dados.

---

## Objetivo do Script

O script `organizador.py` visa:

- Automatizar a organização de arquivos em uma pasta local.
- Criar subpastas automaticamente para cada tipo de arquivo encontrado (baseado na extensão).
- Mover os arquivos para as respectivas pastas, evitando bagunça e duplicação manual.
- Ser simples, direto e reutilizável para diversas situações.

---

## Funcionamento

Quando executado, o script:

1. Solicita ao usuário o caminho absoluto ou relativo da pasta que deseja organizar.
2. Verifica se a pasta existe e tem permissão de acesso.
3. Percorre todos os arquivos na pasta especificada (não faz varredura em subpastas).
4. Para cada arquivo, identifica sua extensão (por exemplo: `jpg`, `pdf`, `txt`).
5. Cria uma subpasta com o nome da extensão, se ela ainda não existir.
6. Move o arquivo para a subpasta correspondente.
7. Ao final, exibe mensagem informando que a organização foi concluída.

---
