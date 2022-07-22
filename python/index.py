import os
from dotenv import load_dotenv
from utils import exceptions, log, environment
from modules import connected_apps

# load environment files from .env
load_dotenv("../.env")
# calling environ is expensive, this saves environment variables to a dictionary
env_dict = dict(os.environ)

# validate environment variables
environment.validate(env_dict)

# encode a JWT token for connected apps authentication: https://help.tableau.com/current/online/en-us/connected_apps.htm#step-4-embedding-next-steps
connected_apps.encode(env_dict)
