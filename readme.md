# 🚀 QAP Automation Framework

Projeto de automação de testes para o sistema QAP usando **Playwright** + **pytest-bdd**, implementando padrão BDD (Behavior Driven Development) com Page Object Model.

## 📋 Índice

- [Tecnologias](#-tecnologias)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Configuração](#-configuração)
- [Execução](#-execução)
- [Estrutura BDD](#-estrutura-bdd)
- [Screenshots](#-screenshots)
- [Relatórios](#-relatórios)
- [Contribuição](#-contribuição)

## 🛠 Tecnologias

- **[Playwright](https://playwright.dev/)** - Automação de navegadores moderna e confiável
- **[pytest-bdd](https://pytest-bdd.readthedocs.io/)** - BDD para Python com Gherkin
- **[pytest](https://pytest.org/)** - Framework de testes robusto
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** - Gerenciamento de variáveis de ambiente
- **Python 3.12+** - Linguagem base do projeto

## 📁 Estrutura do Projeto

```
qap-automation/
├── 📂 config/
│   ├── __init__.py
│   └── settings.py          # Configurações centralizadas
├── 📂 features/
│   └── login.feature         # Cenários BDD em Gherkin
├── 📂 pages/
│   ├── __init__.py
│   ├── base_page.py         # Classe base para Page Objects
│   └── login_page.py        # Page Object da tela de login
├── 📂 steps/
│   ├── __init__.py
│   └── login_steps.py       # Implementação dos steps BDD
├── 📂 tests/
│   ├── __init__.py
│   └── test_login.py        # Testes automatizados
├── 📂 screenshots/          # Evidências visuais (gitignored)
├── 📂 reports/              # Relatórios HTML (gitignored)
├── .env                     # Variáveis de ambiente (gitignored)
├── .gitignore
├── conftest.py              # Configurações do pytest
├── pytest.ini              # Configuração do pytest
├── requirements.txt         # Dependências Python
└── README.md
```

## ⚙️ Pré-requisitos

- **Python 3.12** ou superior
- **Git** para controle de versão
- **Sistema operacional:** Linux, macOS ou Windows

## 🚀 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/qap-automation.git
cd qap-automation
```

### 2. Crie o ambiente virtual
```bash
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Instale os navegadores do Playwright
```bash
playwright install
playwright install-deps  # Linux: dependências do sistema
```

## 🔧 Configuração

### 1. Arquivo .env
Crie o arquivo `.env` na raiz do projeto:

```bash
# URLs do sistema
BASE_URL=https://qap-dev.konneqt.cloud
DASHBOARD_URL=https://qap-dev.konneqt.cloud/admin/dashboard

# Credenciais de teste - Admin
ADMIN_EMAIL=seu_admin@example.com
ADMIN_PASSWORD=sua_senha_admin

# Credenciais de teste - Usuário
USER_EMAIL=seu_user@example.com  
USER_PASSWORD=sua_senha_user

# Configurações do browser
HEADLESS=false
SLOW_MO=1000
BROWSER_TIMEOUT=10000
```

### 2. Validação da configuração
```bash
# Testar se as configurações estão corretas
python -c "from config.settings import settings; settings.validate(); print('✅ Configuração válida!')"
```

## 🎮 Execução

### Comandos básicos
```bash
# Executar todos os testes
pytest

# Executar testes específicos
pytest tests/test_login.py

# Modo verboso (detalhado)
pytest tests/test_login.py -v

# Com output dos prints
pytest tests/test_login.py -v -s

# Executar com relatório HTML
pytest tests/test_login.py --html=reports/report.html

# Executar por tags
pytest -m smoke      # Apenas testes críticos
pytest -m positive   # Apenas cenários positivos

# Executar cenários específicos por nome (keyword)
pytest -k "login"                    # Cenários que contenham "login"
pytest -k "sucesso"                  # Cenários que contenham "sucesso"  
pytest -k "Login com sucesso"        # Cenário exato
pytest -k "admin"                    # Cenários relacionados a admin
pytest -k "credenciais"              # Cenários sobre credenciais
pytest -k "login and sucesso"        # Cenários com ambas palavras
pytest -k "not falha"                # Cenários que NÃO contenham "falha"
```

### Configurações úteis
```bash
# Executar em modo headless (sem interface gráfica)
HEADLESS=true pytest tests/test_login.py

# Executar mais rápido (sem slow motion)
SLOW_MO=0 pytest tests/test_login.py

# Parar no primeiro erro
pytest tests/test_login.py -x

# Executar múltiplos filtros
pytest tests/test_login.py -k "login and admin" -v

# Combinando filtros por keyword e tag
pytest -m smoke -k "sucesso" -v
```

## 🎭 Estrutura BDD

### Feature Example (Gherkin)
```gherkin
Feature: Login Básico
    Scenario: Login com sucesso
        Given I go to the login page
        When I login with valid credentials  
        Then I should be logged in successfully
```

### Steps Implementation
```python
@given("I go to the login page")
def go_to_login_page(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()

@when("I login with valid credentials")
def login_with_valid_credentials(page):
    login_page = LoginPage(page)
    login_page.login_as_admin()

@then("I should be logged in successfully")
def verify_login_success(page):
    login_page = LoginPage(page)
    login_page.wait_for_dashboard()
```

### Page Object Pattern
```python
class LoginPage(BasePage):
    def navigate_to_login(self):
        self.page.goto(settings.BASE_URL)
        self.page.get_by_role("button", name="Sign in").click()
        
    def login_as_admin(self):
        self.login(settings.ADMIN_EMAIL, settings.ADMIN_PASSWORD)
```

## 📸 Screenshots

O framework captura screenshots automaticamente durante a execução:

- **📁 Local:** `screenshots/`
- **🕐 Timestamp:** Cada screenshot tem data/hora única
- **🔍 Debug:** Screenshots em pontos-chave do fluxo
- **💥 Falhas:** Screenshot automático quando teste falha

### Estrutura dos Screenshots
```
screenshots/
├── 01_home_page_20241224_143022.png
├── 02_login_form_20241224_143025.png  
├── 06_dashboard_loaded_20241224_143035.png
└── FAILED_test_login_20241224_143040.png
```

## 📊 Relatórios

### Relatório HTML
```bash
# Gerar relatório
pytest tests/test_login.py --html=reports/report.html

# Abrir relatório
firefox reports/report.html
```

### Relatório inclui:
- ✅ Status dos testes (PASSED/FAILED)
- ⏱️ Tempo de execução
- 📊 Estatísticas gerais
- 🔗 Links para screenshots
- 📝 Logs detalhados

## 🏷️ Tags Disponíveis

```bash
@smoke      # Testes críticos/essenciais
@positive   # Cenários de sucesso  
@negative   # Cenários de falha
@regression # Testes de regressão
@api        # Testes relacionados à API
@admin      # Funcionalidades de admin
@user       # Funcionalidades de usuário
```

## 🔒 Segurança

- **Credenciais:** Nunca commitar `.env` (está no `.gitignore`)
- **Screenshots:** Podem conter dados sensíveis (também ignorados)  
- **Relatórios:** Verificar se não expõem informações confidenciais

## 🐛 Troubleshooting

### Problema: "Step definition not found"
**Solução:** Verificar se o texto no `.feature` bate exatamente com o `@given/@when/@then`

### Problema: Browser não abre
**Solução:** 
```bash
playwright install chromium
# Linux
sudo playwright install-deps
```

### Problema: Timeout nos testes
**Solução:** Aumentar timeout no `.env`
```bash
BROWSER_TIMEOUT=15000
```

### Problema: Screenshots não aparecem
**Solução:** Verificar permissões da pasta
```bash
mkdir screenshots
chmod 755 screenshots
```

## 🤝 Contribuição

### Fluxo de desenvolvimento
1. **Fork** o repositório
2. **Crie** uma branch: `git checkout -b feature/nova-funcionalidade`
3. **Implemente** os testes seguindo o padrão BDD
4. **Execute** os testes: `pytest tests/ -v`
5. **Commit**: `git commit -m "feat: adiciona testes de API import"`
6. **Push**: `git push origin feature/nova-funcionalidade`
7. **Pull Request** com descrição detalhada

### Padrões do projeto
- **BDD:** Cenários em português claro
- **Page Objects:** Um arquivo por página/módulo
- **Steps:** Organizados por funcionalidade
- **Commits:** Padrão conventional commits
- **Screenshots:** Evidências visuais obrigatórias

## 📝 Changelog

### v1.0.0 - 2024-12-24
- ✨ Implementação inicial do framework
- ✅ Testes de login com Keycloak
- 📸 Sistema de screenshots automático
- 🔧 Configuração com variáveis de ambiente
- 📊 Relatórios HTML
- 📖 Documentação completa

## 📞 Suporte

Para dúvidas ou problemas:

1. **Issues:** Abra uma issue no GitHub
2. **Wiki:** Consulte a documentação detalhada
3. **Logs:** Execute com `-v -s` para debug

---

## 🎯 Roadmap

### Próximas funcionalidades:
- [ ] Testes de API import (URL + arquivo)
- [ ] Testes de dashboard navigation  
- [ ] Integração com CI/CD (GitHub Actions)
- [ ] Testes de diferentes usuários/permissões
- [ ] Parallel execution
- [ ] Allure reports
- [ ] Docker support

---

**Desenvolvido com ❤️ usando Playwright + pytest-bdd**

*Framework de automação profissional para testes end-to-end do sistema QAP*