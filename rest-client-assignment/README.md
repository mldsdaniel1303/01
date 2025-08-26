# REST API + Console Client (Python)

Projeto simples para a atividade: implementar uma API REST que retorne dados fictícios e um cliente console que consuma os endpoints.

## Estrutura
- `app.py` - API em Flask com endpoints: /health, /users, /users/<id>, /products, /orders (POST, GET)
- `client.py` - Cliente console que consome a API usando `requests`
- `requirements.txt` - Dependências

## Como executar

1. Crie um virtualenv (recomendado) e ative:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows (PowerShell)
   ```

2. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Inicie a API:
   ```bash
   python app.py
   ```
   A aplicação ficará escutando em `http://127.0.0.1:5000`.

4. Em outro terminal, execute o cliente:
   ```bash
   python client.py
   ```

## Observações
- A API usa armazenamento em memória (listas). Reiniciar o servidor limpa os pedidos.
- Para documentação manual, você pode usar o Postman / Insomnia / Rest Client no VS Code apontando para os endpoints acima.
