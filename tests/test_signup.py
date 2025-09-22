# tests/test_signup.py
from pytest_bdd import scenarios

# Import direto e explícito
from steps.signup_steps import *

scenarios('../features/signup.feature')