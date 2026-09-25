# co2-calculator

# Calculadora de Emissão de CO₂ 🚗🌳

Calcula a emissão de CO₂ gerada pelo deslocamento diário de uma pessoa e converte o total anual em número equivalente de árvores necessárias para compensar essa emissão.

## ODS relacionada

**ODS 13 — Ação Contra a Mudança Global do Clima**, meta 13.3 (educação e conscientização sobre mudança do clima). A aplicação não reduz emissões por si só, mas torna visível o impacto de escolhas de transporte do dia a dia, incentivando a troca por meios mais sustentáveis.

## Funcionalidades

- Cálculo de emissão diária e anual de CO₂, a partir da distância percorrida, do meio de transporte e da frequência semanal.
- Conversão do CO₂ anual em número de árvores equivalentes necessárias para absorver aquele gás.
- Tratamento de erros para entradas inválidas (distância zero/negativa, transporte inexistente, dias fora do intervalo de 1 a 7).

Fatores de emissão e fontes detalhadas em [`docs/fatores-emissao.md`](docs/fatores-emissao.md).

## Tecnologias

- Python 3.11+
- pytest (testes unitários)
- black (formatação de código)
- GitHub Actions (integração contínua)

## Como instalar e rodar

```bash
git clone https://github.com/dmannadias-gif/co2-calculator.git
cd co2-calculator
python -m venv venv
venv\Scripts\activate          # Windows
pip install -e .
pip install pytest black
python main.py
```

## Como rodar os testes

```bash
pytest -v
```

## Estrutura do projeto

src/co2calc/
├── core.py # regras de cálculo (testado por TDD)
├── models.py # estruturas de dados
├── errors.py # exceções customizadas
└── cli.py # interface de linha de comando
tests/ # testes unitários (pytest)
docs/ # fontes dos fatores de 


## Fluxo de branches

Este repositório segue o padrão Git Flow: `main` (estável), `develop` (integração) e branches `feature/<nome>` por funcionalidade/pessoa.

## Integrante

- Anna Vitória Rocha Dias - RA: 325118421
- Karolyne Silva - RA: 32517941
- Maycon De Oliveira Gomes Batista - RA: 325125878


## Trabalho acadêmico

Projeto desenvolvido para a disciplina de Gestão e Qualidade de Software (GQS), UNA, sob orientação do professor Daniel Henrique Matos de Paiva.
