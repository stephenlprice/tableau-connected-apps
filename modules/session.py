from utils import log
from libs import rest, connected_apps

class Session:
  """
  """

  def __init__(self, env_dict):
    self.env_dict = env_dict
    self.jwt
    self.key
    self.session

  def __str__(self):
    return f"" 

  # encode a JWT token for connected apps authentication: https://help.tableau.com/current/online/en-us/connected_apps.htm#step-4-embedding-next-steps
  def get_JWT(self, silent):
    self.jwt = connected_apps.encode(self.env_dict)

    if silent:
      return self.jwt
    else:
      print('SUCCESS --> JWT encoded:', self.jwt)
      log.logger.info('SUCCESS --> JWT encoded:', self.jwt)


  # authenticate to Tableau's REST API to obtain an API key
  def get_key(self, silent):
    self.jwt = self.get_JWT(True)
    self.key = rest.auth(self.env_dict, self.jwt)

    if silent:
      return self.key
    else:
      print('SUCCESS --> REST API key:', self.key)
      log.logger.info('SUCCESS --> REST API key:', self.key)

  # creates a full session, can output JWT and API Key
  def get_session(self, silent):
    self.key = self.get_key(True)

    if silent:
      return {"jwt": self.jwt, "key": self.key}
    else: 
      print(f"""
      ***** SESSION *****
      JWT: {self.jwt}
      API Key: {self.key}
      """)
