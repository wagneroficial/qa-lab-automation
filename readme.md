# 🚀 QAP Automation 

Test automation project for the QAP system using **Playwright** + **pytest-bdd**, implementing BDD (Behavior Driven Development) pattern with Page Object Model.

## 📋 Table of Contents

- [Technologies](#-technologies)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Execution](#-execution)
- [BDD Structure](#-bdd-structure)
- [Screenshots](#-screenshots)
- [Reports](#-reports)
- [Contributing](#-contributing)

## 🛠 Technologies

- **[Playwright](https://playwright.dev/)** - Modern and reliable browser automation
- **[pytest-bdd](https://pytest-bdd.readthedocs.io/)** - BDD for Python with Gherkin
- **[pytest](https://pytest.org/)** - Robust testing framework
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** - Environment variables management
- **Python 3.12+** - Base language of the project

## 📁 Project Structure

```
qap-automation/
├── 📂 config/
│   ├── __init__.py
│   └── settings.py          # Centralized settings
├── 📂 features/
│   └── login.feature         # BDD scenarios in Gherkin
├── 📂 pages/
│   ├── __init__.py
│   ├── base_page.py         # Base class for Page Objects
│   └── login_page.py        # Login page Page Object
├── 📂 steps/
│   ├── __init__.py
│   └── login_steps.py       # BDD steps implementation
├── 📂 tests/
│   ├── __init__.py
│   └── test_login.py        # Automated tests
├── 📂 screenshots/          # Visual evidence (gitignored)
├── 📂 reports/              # HTML reports (gitignored)
├── .env                     # Environment variables (gitignored)
├── .gitignore
├── conftest.py              # pytest configurations
├── pytest.ini              # pytest configuration
├── requirements.txt         # Python dependencies
└── README.md
```

## ⚙️ Prerequisites

- **Python 3.12** or higher
- **Git** for version control
- **Operating System:** Linux, macOS or Windows

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://gitlab.konneqt.io/konneqt/qa-team/qap-e2e.git
cd qap-e2e
```

### 2. Create virtual environment
```bash
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers
```bash
playwright install
playwright install-deps  # Linux: system dependencies
```

## 🔧 Configuration

### 1. .env File
Create the `.env` file in the project root:

```bash
# System URLs
BASE_URL=https://your-application.com
DASHBOARD_URL=https://your-application.com/dashboard

# Test credentials - Admin
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=your_admin_password

# Test credentials - User
USER_EMAIL=user@example.com  
USER_PASSWORD=your_user_password

# Browser settings
HEADLESS=false
SLOW_MO=1000
BROWSER_TIMEOUT=10000
```

### 2. Configuration validation
```bash
# Test if configurations are correct
python -c "from config.settings import settings; settings.validate(); print('✅ Valid configuration!')"
```

## 🎮 Execution

### Basic commands
```bash
# Run all tests
pytest

# Run specific tests
pytest tests/test_login.py

# Verbose mode (detailed)
pytest tests/test_login.py -v

# With prints output
pytest tests/test_login.py -v -s

# Run with HTML report
pytest tests/test_login.py --html=reports/report.html

# Run by tags
pytest -m smoke      # Only critical tests
pytest -m positive   # Only positive scenarios

# Run specific scenarios by name (keyword)
pytest -k "login"                    # Scenarios containing "login"
pytest -k "success"                  # Scenarios containing "success"  
pytest -k "Successful login"         # Exact scenario
pytest -k "admin"                    # Admin-related scenarios
pytest -k "credentials"              # Credential scenarios
pytest -k "login and success"        # Scenarios with both words
pytest -k "not failure"              # Scenarios that DON'T contain "failure"
```

## 📸 Screenshots

The framework automatically captures screenshots during execution:

- **📁 Location:** `screenshots/`
- **🔍 Debug:** Screenshots at key flow points
- **💥 Failures:** Automatic screenshot when test fails

## 📊 Reports

### HTML Report
```bash
# Generate report
pytest tests/test_login.py --html=reports/report.html

# Open report
firefox reports/report.html
```

### Report includes:
- ✅ Test status (PASSED/FAILED)
- ⏱️ Execution time
- 📊 General statistics
- 🔗 Links to screenshots
- 📝 Detailed logs

## 🏷️ Available Tags

```bash
@smoke      # Critical/essential tests
@positive   # Success scenarios  
@negative   # Failure scenarios
@regression # Regression tests
@api        # API-related tests
@admin      # Admin functionalities
@user       # User functionalities
```

## 🔒 Security

- **Credentials:** Never commit `.env` (it's in `.gitignore`)
- **Screenshots:** May contain sensitive data (also ignored)  
- **Reports:** Check if they don't expose confidential information

## 🐛 Troubleshooting

### Issue: "Step definition not found"
**Solution:** Check if the text in `.feature` exactly matches the `@given/@when/@then`

### Issue: Browser doesn't open
**Solution:** 
```bash
playwright install chromium
# Linux
sudo playwright install-deps
```

### Issue: Test timeouts
**Solution:** Increase timeout in `.env`
```bash
BROWSER_TIMEOUT=15000
```

### Issue: Screenshots don't appear
**Solution:** Check folder permissions
```bash
mkdir screenshots
chmod 755 screenshots
```

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Merge Request



**Developed by:** QA Team - Konneqt  
**Repository:** https://gitlab.konneqt.io/konneqt/qa-team/qap-e2e