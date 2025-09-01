# tests/test_login.py
from pytest_bdd import scenarios

# Import direto e explícito
from steps.login_steps import *

scenarios('../features/login.feature')