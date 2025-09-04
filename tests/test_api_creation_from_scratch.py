from pytest_bdd import scenarios

from steps.login_steps import *
from steps.api_creation_from_scratch_steps import *

scenarios('../features/api_creation_from_scratch.feature')

