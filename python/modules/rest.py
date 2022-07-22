import requests
from utils import exceptions, log

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