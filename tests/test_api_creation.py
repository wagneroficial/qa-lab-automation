from pytest_bdd import scenarios

# Import explícito dos steps (como faz no test_login.py)
from steps.login_steps import *
from steps.api_creation_steps import *

scenarios('../features/api_creation.feature')

