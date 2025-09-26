# 🤖 QA Lab Automation

Automação de testes para o sistema **qa-lab-inventory** usando **Playwright** + **pytest-bdd** com padrão BDD (Behavior Driven Development).

## 🛠 Tecnologias

- **[Playwright](https://playwright.dev/)** - Automação de navegadores moderna
- **[pytest-bdd](https://pytest-bdd.readthedocs.io/)** - BDD para Python com Gherkin
- **[pytest](https://pytest.org/)** - Framework de testes
- **Python 3.12+**

## 📁 Estrutura do Projeto

```
qa-lab-automation/
├── 📂 config/
│   ├── __init__.py
│   └── settings.py          # Configurações centralizadas
├── 📂 features/
│   ├── login.feature        # Cenários de login
│   └── registration.feature # Cenários de registro
├── 📂 pages/
│   ├── __init__.py
│   ├── base_page.py         # Classe base para Page Objects
│   ├── login_page.py        # Page Object da tela de login
│   └── registration_page.py # Page Object da tela de registro
├── 📂 steps/
│   ├── __init__.py
│   ├── login_steps.py       # Steps do login
│   └── registration_steps.py # Steps do registro
├── 📂 tests/
│   ├── __init__.py
│   ├── test_login.py        # Testes de login
│   └── test_registration.py # Testes de registro
├── 📂 screenshots/          # Evidências visuais
├── 📂 reports/              # Relatórios HTML
├── .env                     # Variáveis de ambiente
├── conftest.py              # Configurações do pytest
├── requirements.txt         # Dependências Python
└── README.md
```

## 🚀 Instalação

### 1. Clonar o repositório
```bash
git clone https://github.com/wagneroficial/qa-lab-automation.git
cd qa-lab-automation
```

### 2. Criar ambiente virtual
```bash
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
playwright install
```

## 🔧 Configuração

### Arquivo .env
```bash
# URL do sistema
BASE_URL=http://localhost:3000

# Credenciais de teste
TEST_EMAIL=teste@exemplo.com
TEST_PASSWORD=123456

# Configurações do navegador
HEADLESS=false
SLOW_MO=1000
```

## 🎮 Execução

```bash
# Executar todos os testes
pytest

# Executar testes específicos
pytest tests/test_login.py
pytest tests/test_registration.py

# Com relatório HTML
pytest --html=reports/report.html

# Modo verbose
pytest -v

# Por tags
pytest -m smoke       # Testes críticos
pytest -m login       # Testes de login
pytest -m registration # Testes de registro
```
