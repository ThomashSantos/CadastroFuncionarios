# Sistema de Cadastro de Funcionários - OrangeHRM

Sistema automatizado para cadastro de candidatos no portal OrangeHRM utilizando dados de um arquivo CSV.

## Descrição

Este projeto automatiza o processo de cadastro de candidatos no sistema OrangeHRM, lendo informações de um arquivo CSV e preenchendo automaticamente os formulários web através de automação com Playwright.

## Estrutura do Projeto

```
CadastroFuncionarios/
├── main.py                              # Arquivo principal de execução
├── requirements.txt                     # Dependências do projeto
├── README.md                           # Documentação do projeto
└── fonte/
    ├── __init__.py                     # Configuração de logging e pastas
    ├── dados/
    │   ├── entrada/
    │   │   └── banco.sql.csv          # Arquivo com dados dos candidatos
    │   ├── saida/                     # Arquivos temporários de currículos
    │   └── logs/                      # Logs diários do sistema
    └── modulos/
        ├── candidatos/
        │   └── capturada_dados.py     # Classe para manipulação dos dados
        └── orange_hrm/
            └── portal_orange.py       # Classe para automação do OrangeHRM
```

## Formato dos Dados

O arquivo CSV deve conter as seguintes colunas:

| Campo | Descrição | Exemplo |
|-------|-----------|---------|
| `full_name` | Nome completo do candidato | Ana Beatriz Souza |
| `vacancy` | Vaga pretendida | Senior QA Lead |
| `email` | E-mail do candidato | ana.beatriz.souza@email.com |
| `contact_number` | Número de contato | (11) 98765-4321 |
| `keywords` | Palavras-chave separadas por `;` | Empatia; Liderança; Comunicação |

## 🛠️ Instalação

### Pré-requisitos

- Python 3.8 ou superior
- Google Chrome instalado

### Passos de instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/SEU_USUARIO/CadastroFuncionarios.git
   cd CadastroFuncionarios
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Instale os navegadores do Playwright**:
   ```bash
   playwright install
   ```

4. **Configure as variáveis de ambiente**:
   ```bash
   # Copie o arquivo de exemplo
   cp .env.example .env
   
   # Edite o arquivo .env com suas credenciais
   nano .env
   ```

## 🚀 Uso

1. **Prepare os dados**:
   - Coloque o arquivo CSV com os dados dos candidatos em: `fonte/dados/entrada/banco.sql.csv`

2. **Execute o sistema**:
   ```bash
   python main.py
   ```

3. **Acompanhe o progresso**:
   - Os logs são salvos automaticamente em: `fonte/dados/logs/YYYYMMDD.log`
   - O sistema exibirá o progresso no terminal
