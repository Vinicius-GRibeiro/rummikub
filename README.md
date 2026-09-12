# 🎲 Rummikub in Python

Uma implementação completa do clássico jogo de tabuleiro **Rummikub** em Python, desenvolvida com foco em **Clean Architecture**, **Programação Orientada a Objetos (POO)** e **Testes Automatizados**.

O projeto foi concebido para ser desacoplado da interface: a lógica de regras e domínio é 100% independente, permitindo rodar primeiro em modo de linha de comando (CLI interativa) e, posteriormente, acoplar uma interface gráfica (GUI).

---

## 🚀 Destaques de Arquitetura

- **Domínio Isolado (`core`):** As entidades de jogo (`Tile`, `TileBag`, `Meld`, `Board`, `Player`) não possuem dependências de terminal ou bibliotecas gráficas (sem `print()` ou `input()` no domínio).
- **Testes Automatizados:** Suíte de testes com `pytest` cobrindo cenários felizes, edge cases e tratamento de exceções.

---

## 📁 Estrutura do Projeto

```text
Rummikub/
├── src/
│   └── rummikub/
│       ├── core/       # Regras puras e entidades (Tile, Bag, Meld, Board, Player)
│       └── ui/
│           ├── cli/    # Interface de Terminal (Renderização ANSI e controles)
│           └── gui/    # Futura Interface Gráfica (Pygame / Arcade)
├── tests/              # Testes unitários com pytest
├── pytest.ini          # Configuração da suíte de testes
└── requirements.txt    # Dependências do projeto
```

---

## 🗺️ Roadmap de Desenvolvimento

- [x] **Peça (`Tile`):** Cores com `Enum`, Coringa, validação de limites (1 a 13) e imutabilidade.
- [x] **Monte de Peças (`TileBag`):** 106 peças oficiais, compra individual, compra em lote e embaralhamento.
- [x] **Suíte de Testes Inicial:** 18 testes automatizados cobrindo peças e monte de compra.
- [x] **Jogador & Suporte (`Player` / `Rack`):** Gerenciamento da mão, contagem de pontos e ordenação por cor e número.
- [x] **Validação de Combinações (`Meld`):** Regras de Grupos (*Sets*), Sequências (*Runs*) e Coringas.
- [ ] **Mesa & Transações (`Board`):** Manipulação de peças com suporte a *snapshot* e *rollback*.
- [ ] **Mecânica de Jogo (`Game`):** Regra dos 30 pontos na saída inicial e ciclo de turnos.
- [ ] **Interface CLI:** Renderização no terminal com cores ANSI e navegação interativa.
- [ ] **Interface Gráfica (GUI):** Implementação visual interativa.

---

## 🛠️ Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/Vinicius-GRibeiro/rummikub.git
cd Rummikub
```

### 2. Criar e ativar o ambiente virtual
```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# Linux / MacOS
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Executar os testes automatizados
```bash
pytest
```

---
