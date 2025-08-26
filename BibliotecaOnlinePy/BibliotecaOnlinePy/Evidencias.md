# Evidências – Biblioteca Online (API em Python + FastAPI)

**Tema**: Biblioteca Online – gerenciamento de publicações (Livros, Revistas, Jornais).  
**Tecnologia**: FastAPI (Python) com routes, services e models.

## Conceitos de POO aplicados
- **Abstração**: `Publicacao` é uma **classe abstrata** que define membros comuns (id, titulo, autor, ano) e obriga as subclasses a implementarem `calcular_taxa_emprestimo()`.
- **Herança**: `Livro`, `Revista` e `Jornal` **herdam** de `Publicacao`.
- **Polimorfismo**: cada tipo implementa `calcular_taxa_emprestimo()` de forma diferente; o serviço/rotas usa o tipo base `Publicacao` e o **método correto é resolvido em tempo de execução**.
- **Interface/ABC**: `IEmprestavel` (via `ABC`) define o contrato `calcular_taxa_emprestimo()` e é implementada por `Publicacao`.

## Camadas
- **models.py**: classes de domínio (`Publicacao`, `Livro`, `Revista`, `Jornal`).
- **services/publicacao_service.py**: lógica de negócio (CRUD em memória com dados de seed).
- **routes/publicacoes.py**: endpoints REST (GET, POST, PUT, DELETE).
- **requests.http**: arquivo para uso com REST Client (VS Code) com exemplos de consumo.

## Como executar
1. Instale Python 3.10+.
2. Crie um ambiente virtual (recomendado):
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux / macOS
   .venv\Scriptsctivate      # Windows (cmd)
   ```
3. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute a API com uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
5. A API estará disponível em `http://localhost:8000` e a documentação automática em `http://localhost:8000/docs`.

## Observações
- A implementação usa **tipos dataclass** e `ABC` para demonstrar abstração e polimorfismo.
- O serviço mantém os dados em memória (adequado para demonstração e avaliação).

Gerado em 2025-08-26 18:37:23.
