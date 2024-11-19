# Pedidos Back-End API

Este repositório contém a implementação do back-end de um sistema simples de gerenciamento de pedidos e estoque. O projeto utiliza Python e Flask, seguindo uma arquitetura modular com padrões de design como Command e Decorator para melhorar a manutenibilidade e escalabilidade.

---

## Funcionalidades

- **Gerenciamento de Pedidos**:
  - Criar novos pedidos.
  - Recuperar todos os pedidos.
  - Recuperar um pedido pelo número.

- **Gerenciamento de Estoque**:
  - Buscar itens de estoque disponíveis.

- **Design Patterns**:
  - Implementação dos padrões de projeto Command e Decorator.

- **Banco de Dados**:
  - Integração com MongoDB para armazenamento e gerenciamento de pedidos e estoque.

---

## Estrutura do Projeto

```plaintext
.
├── app
│   ├── auth                # Decorador para autenticação
│   │   └── auth_decorator.py
│   ├── commands            # Implementação do padrão Command
│   │   ├── command.py
│   │   ├── invoker.py
│   │   └── order_commands.py
│   ├── config              # Configuração de banco de dados
│   │   ├── db_config.py
│   │   └── order_DAO.py
│   ├── controllers         # Lógica de negócio para pedidos e estoque
│   │   ├── order_controller.py
│   │   └── stock_controller.py
│   ├── models              # Modelos para pedidos e estoque
│   │   ├── order_model.py
│   │   └── stock_model.py
│   ├── routes              # Rotas da API
│   │   ├── order_routes.py
│   │   └── stock_routes.py
│   └── run.py              # Aplicação principal Flask
├── .env.example            # Exemplo de variáveis de ambiente
├── .gitignore              # Arquivo gitignore
├── Dockerfile              # Configuração para Docker
├── README.md               # Documentação
├── requirements.txt        # Dependências do projeto
└── tests                   # (Opcional) Casos de teste
```

---

## Instalação

### Pré-requisitos

- Python 3.10+
- Instância do MongoDB

### Passos

1. Clone o repositório:
   ```bash
   git clone <repository_url>
   cd pedidos-back
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure o arquivo `.env`:
   Copie o arquivo `.env.example` para `.env` e preencha as configurações necessárias.

4. Execute a aplicação:
   ```bash
   python app/run.py
   ```

5. Acesse a API em `http://127.0.0.1:5000`.

---

## Endpoints da API

### Rotas de Pedidos

| Método | Endpoint                       | Descrição                     |
|--------|--------------------------------|--------------------------------|
| GET    | `/api/order`                  | Buscar todos os pedidos       |
| GET    | `/api/order/<order_number>`   | Buscar um pedido específico   |
| POST   | `/api/order`                  | Criar um novo pedido          |

### Rotas de Estoque

| Método | Endpoint     | Descrição                |
|--------|--------------|--------------------------|
| GET    | `/api/stock` | Buscar itens de estoque  |

---

## Padrões de Projeto

### Command Pattern
Utilizado para encapsular a lógica de execução de requisições. Comandos incluem:
- `CreateOrderCommand`
- `GetOrderCommand`
- `GetOrderByNumberCommand`

### Decorator Pattern
O decorador `require_auth` é implementado para autenticação das requisições.

---

## Dependências

- **Frameworks**:
  - Flask
  - Flask-CORS

- **Banco de Dados**:
  - PyMongo

- **Utilitários**:
  - Python Dotenv para variáveis de ambiente.