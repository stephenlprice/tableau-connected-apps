import os
from dotenv import load_dotenv
from utils import exceptions, log, environment
from modules import connected_apps

# dictionary with required environment variables
env_vars = [
  "TABLEAU_SERVER",
  "TABLEAU_SITENAME",
  "TABLEAU_USERNAME",
  "TABLEAU_CA_CLIENT",
  "TABLEAU_CA_SECRET_ID",
  "TABLEAU_CA_SECRET_VALUE"
]

# load environment files from .env
load_dotenv("../.env")
# calling environ is expensive, this saves environment variables to a dictionary
env_dict = dict(os.environ)

# validate environment variables
environment.validate(env_dict, env_vars)

# encode a JWT token for connected apps authentication: https://help.tableau.com/current/online/en-us/connected_apps.htm#step-4-embedding-next-steps
token = connected_apps.encode(env_dict)

