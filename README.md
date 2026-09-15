# 🎲 Rummikub in Python

Uma implementação completa e moderna do clássico jogo de tabuleiro **Rummikub** em Python, desenvolvida com foco em **Clean Architecture**, **Programação Orientada a Objetos (POO)**, **Testes Automatizados (TDD)** e **Interface Gráfica Interativa com Pygame**.

O projeto foi concebido com estrita separação de camadas: as regras de negócio e a máquina de estados do jogo (`core`) são 100% desacopladas de qualquer interface gráfica ou de terminal, permitindo manutenibilidade, testabilidade total e evolução contínua.

---

## 🚀 Destaques de Engenharia e Arquitetura

- **Domínio Isolado (`core`):** As entidades de jogo (`Tile`, `TileBag`, `Meld`, `Board`, `Player`, `Game`) operam de forma pura, sem qualquer dependência de bibliotecas gráficas ou de console.
- **Suíte de Testes Abrangente (61 testes com `pytest`):** Cobertura completa de casos de sucesso, edge cases.
---

## 📁 Estrutura do Projeto

```text
Rummikub/
├── src/
│   └── rummikub/
│       ├── core/               # REGRAS PURAS E ENTIDADES (Sem prints, sem GUI)
│       │   ├── tile.py         # Peça (Tile), Cores (Color Enum), Coringas
│       │   ├── bag.py          # Monte com 106 peças e compras seguras
│       │   ├── meld.py         # Validação de Grupos (Sets) e Sequências (Runs)
│       │   ├── board.py        # Tabuleiro compartilhado com Snapshot e Rollback
│       │   ├── player.py       # Jogador, suporte (Rack) e ordenações duplas
│       │   └── game.py         # Orquestrador de turnos, saída de 30 pts e vitória
│       │
│       └── ui/
│           └── gui/            # CAMADA DE APRESENTAÇÃO GRÁFICA (Pygame)
│               ├── app.py      # Loop principal da aplicação gráfica e HUD
│               ├── tile_view.py# Renderizador procedural das pedrinhas e temas
│               ├── board_view.py# Layout da mesa com quebra automática de melds
│               ├── rack_view.py# Suporte interativo com seleção e hover
│               └── widgets.py  # Botões interativos com estados visuais
│
├── tests/                      # 61 TESTES AUTOMATIZADOS (pytest)
│   ├── test_tile.py            # Testes de imutabilidade, valores e coringas
│   ├── test_bag.py             # Testes de composição, compras e esgotamento
│   ├── test_player.py          # Testes de rack, pontos e ordenações
│   ├── test_meld_group.py      # Testes de grupos com e sem coringas
│   ├── test_meld_run.py        # Testes de sequências e posições de coringas
│   ├── test_board.py           # Testes de integridade de mesa e rollback
│   └── test_game.py            # Testes do loop de partida e regra dos 30 pts
│
├── ARCHITECTURE.md             # Detalhamento arquitetural completo
├── pytest.ini                  # Configuração de caminhos da suíte de testes
└── requirements.txt            # Dependências do projeto (pytest, colorama, pygame-ce)
```

---

## 🗺️ Roadmap do Projeto

- [x] **Peça (`Tile`):** Imutabilidade com `@dataclass(frozen=True)`, Cores com `Enum`, Coringa e validação de limites (1 a 13).
- [x] **Monte de Peças (`TileBag`):** 106 peças oficiais, compra individual, compra em lote e controle de monte vazio.
- [x] **Jogador & Suporte (`Player`):** Gerenciamento da mão, contagem de penalidade e ordenação por cor e por número.
- [x] **Validação de Combinações (`Meld`):** Regras de Grupos (*Sets*), Sequências (*Runs*) e Coringas em qualquer posição.
- [x] **Mesa Transacional (`Board`):** Manipulação de jogos com suporte a *snapshot* e *rollback*.
- [x] **Motor da Partida (`Game`):** Distribuição inicial de 14 peças, alternância circular de turnos, regra dos 30 pontos na saída inicial e detecção de vencedor.
- [x] **Suíte de Testes Automatizados:** 61 testes cobrindo 100% dos módulos do domínio.
- [x] **Interface Gráfica Completa (Pygame):** HUD com placar, botões de ação, mesa em fluxo, seleção e animação tátil de peças.

---

## 🛠️ Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/Vinicius-GRibeiro/rummikub.git
cd rummikub
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

### 5. Executar o Jogo Gráfico
```bash
python src/rummikub/ui/gui/app.py
```

> **Atalhos no Jogo:**
> - `Clique do Mouse`: Seleciona/deseleciona peças do seu suporte.
> - `Tecla T`: Alterna entre os temas visuais *Obsidian Noir* e *Marfim Nobre*.

---
