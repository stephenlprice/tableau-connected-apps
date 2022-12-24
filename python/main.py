import os, inspect, argparse
from dotenv import load_dotenv
from pathlib import Path
from utils import log, environment
from modules import connected_apps, rest

class TabJWT:
  """
  """

  def __init__(self):
    self.jwt,
    self.key

  def __str__(self):
    return f"" 

  # encode a JWT token for connected apps authentication: https://help.tableau.com/current/online/en-us/connected_apps.htm#step-4-embedding-next-steps
  def get_JWT(self, silent):
    self.jwt = connected_apps.encode(env_dict)

    if silent:
      return self.jwt
    else:
      print('SUCCESS --> JWT encoded:', self.jwt)
      log.logger.info('SUCCESS --> JWT encoded:', self.jwt)


  # authenticate to Tableau's REST API to obtain an API key
  def get_key(self, silent):
    self.jwt = self.get_JWT(True)
    self.key = rest.auth(env_dict, self.jwt)

    if silent:
      return self.key
    else:
      print('SUCCESS --> REST API key:', self.key)
      log.logger.info('SUCCESS --> REST API key:', self.key)

  # get a list of workbooks on the site
  def get_workbooks(self):
    self.key = self.get_key(True)

    workbooks = rest.get_workbooks_site(self.key)
    print('SUCCESS --> Workbooks:', workbooks)
    log.logger.info('SUCCESS --> Workbooks:', workbooks)
    return workbooks

# protects the entry point of the script so that this only runs during local development
if __name__ == '__main__':
  # load environment files from .env
  load_dotenv("../.env")
  # calling environ is expensive, this saves environment variables to a dictionary
  env_dict = dict(os.environ)

  # validate environment variables
  environment.validate(env_dict)
  print('SUCCESS: environment validation passed...')
  log.logger.info('SUCCESS: environment validation passed...')

  # used to output file name, line number and caller when debugging
  def getLineInfo():
    print(inspect.stack()[1][1],":",inspect.stack()[1][2],":", inspect.stack()[1][3])
