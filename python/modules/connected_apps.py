import datetime, uuid
import jwt
import requests
from utils import exceptions, log, environment

env_var = environment.env_dict

class connected_apps:
  def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
    self.salary = salary
    self.message = message
    super().__init__(self.message)

  def __str__(self):
    return f'{self.salary} -> {self.message}'

# tableau connected app variables (JWT) see: https://help.tableau.com/current/online/en-us/connected_apps.htm#step-3-configure-the-jwt
header_data = {
  "iss": env_var["TABLEAU_CA_CLIENT"],
  "kid": env_var["TABLEAU_CA_SECRET_ID"],
  "alg": "HS256",
}

payload_data = {
  "iss": env_var["TABLEAU_CA_CLIENT"],
  "sub": env_var["TABLEAU_USERNAME"],
  "aud": "tableau",
  "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
  "jti": str(uuid.uuid4()),
  "scp": ["tableau:content:read", "tableau:workbooks:create"]
}

connected_app_secret = env_var["TABLEAU_CA_SECRET_VALUE"]

# encode the JWT with declared payload, secret and headers
token = jwt.encode(
  payload = payload_data,
  key = connected_app_secret,
  headers = header_data
)
print(f'encoded token: {token}')

# decode the JWT for testing purposes
decodedToken = jwt.decode(
  jwt = token, 
  key = connected_app_secret,
  audience = payload_data["aud"], 
  algorithms = header_data["alg"]
)
print(f'decoded token: {decodedToken}')


# authentication into tableau's REST API
base_path = f'{env_var["TABLEAU_SERVER"]}/api'

auth_url = f'{base_path}/3.16/auth/signin'

auth_payload = """
<tsRequest>
  <credentials jwt="{0}">
    <site contentUrl="{1}"/>
  </credentials>
</tsRequest>
"""

auth_headers = {
  'Content-Type': 'application/xml',
  'Accept': 'application/json'
}

response = requests.request("POST", auth_url, headers=auth_headers, data=auth_payload.format(token, env_var["TABLEAU_SITENAME"]))

response_body = response.json()
print(response_body)

# obtain dict values from response
site_id = response_body["credentials"]["site"]["id"]
api_key = response_body["credentials"]["token"]
print(site_id)

# get a list of views for a site
views_url = f'{base_path}/exp/sites/{site_id}/views'

payload={}
headers = {
  'Accept': 'application/json',
  'X-Tableau-Auth': api_key
}

response = requests.request("GET", views_url, headers=headers, data=payload)

print(response.text)

