import requests
from utils import exceptions, log


credentials = {
  "server": "",
  "api_version": "",
  "site_id": "",
  "api_key": ""
}

paths = {
  "classic": f'{credentials["server"]}/api/{credentials["api_version"]}/',
  "new": f'{credentials["server"]}/api/*/',
  "site": f'sites/{credentials["site_id"]}/',
}

# authentication into tableau's REST API with a valid JWT
def auth(env_vars, jwt):

  credentials['server'] = env_vars['TABLEAU_SERVER']
  credentials['api_version'] = env_vars['TABLEAU_RESTAPI_VERSION']

  auth_url = f'{paths["classic"]}/auth/signin'

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

  response = requests.request("POST", auth_url, headers=auth_headers, data=auth_payload.format(jwt, env_vars["TABLEAU_SITENAME"]))

  response_body = response.json()
  print(response_body)

  # obtain dict values from response
  credentials["site_id"] = response_body["credentials"]["site"]["id"]
  credentials["api_key"] = response_body["credentials"]["token"]

  print(credentials)



def get_workbooks_site(api_key):
  # get a list of views for a site
  query_parameters = f'pageSize=5-size&fields=_all_'

  views_url = f'{paths["classic"]}{paths["site"]}workbooks?{query_parameters}'

  payload={}
  headers = {
    'Accept': 'application/json',
    'X-Tableau-Auth': api_key
  }

  response = requests.request("GET", views_url, headers=headers, data=payload)

  response_body = response.json()
  print(response_body)
