# 14 – Tendências em Linguagens de Programação

Este diretório apresenta pesquisas e documentações sobre **linguagens emergentes**, com foco em **Rust** e **Go (Golang)**.  
O objetivo é entender o contexto dessas linguagens, suas características principais e exemplos práticos.

---

## Rust

### Introdução
Rust é uma linguagem de programação moderna, criada pela Mozilla Research em 2010, cujo foco principal é **desempenho, segurança e concorrência**.  
Ela foi projetada para evitar erros comuns como *segfaults* e problemas de concorrência, oferecendo ao mesmo tempo velocidade próxima à de C e C++.

### Características Principais
- **Segurança de Memória**: sistema de ownership e borrowing que evita ponteiros nulos e data races em tempo de compilação.
- **Concorrência Segura**: abstrações para concorrência, garantindo ausência de race conditions.
- **Desempenho**: performance próxima a C/C++ e compilação para binários otimizados.
- **Ferramentas Modernas**: Cargo (gerenciador de pacotes), Rustup (gerenciador de versões) e o ecossistema de crates.

### Onde é Usada
- Sistemas operacionais (partes do Linux)
- WebAssembly
- Navegadores (motor Servo)
- Blockchain e criptografia
- Aplicações de alto desempenho

### Comparação com Outras Linguagens

| Linguagem  | Pontos Fortes                           | Limitações                       |
|------------|-----------------------------------------|----------------------------------|
| Rust       | Segurança de memória sem GC, performance | Curva de aprendizado alta        |
| Go         | Simplicidade, concorrência com goroutines | Coleta de lixo pode impactar performance |
| Kotlin     | Produtividade, multiplataforma (JVM)     | Depende da JVM ou compilador nativo |
| TypeScript | Tipagem estática no JavaScript          | Performance limitada pelo JS     |

### Tendências e Comunidade
- Rust está entre as linguagens mais amadas do Stack Overflow desde 2016.
- Empresas como Amazon, Microsoft, Discord, Dropbox e Cloudflare utilizam Rust em produção.

### Exemplo de Código

```rust
fn main() {
    let nome = "Mundo";
    println!("Olá, {}!", nome);
}
