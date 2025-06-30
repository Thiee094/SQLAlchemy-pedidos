# Sistema Pizzaria

Projeto simples para gerenciar usuários e pedidos de uma pizzaria usando Python e SQLAlchemy.

## Estrutura do projeto

- `pizzaria.db`: banco de dados SQLite (não comitado).
- `requirements.txt`: dependências do projeto.
- `models/`: contém os modelos do banco de dados.

## Como usar

1. Clone o repositório:
   ```bash
   git clone <https://github.com/Thiee094/sqlalchemy-bdpizzaria.git>
   cd sistema_pizzaria
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Rode o script principal:
   ```bash
   python app.py
   ```

---

# Detalhes

Projeto desenvolvido para praticar SQLAlchemy 2.0, com modelos `User` e `Pedido`, relacionamentos e operações básicas.
