import requests
import json
from utils import exceptions, log
from modules import connected_apps


credentials = {
  "server": "",
  "api_version": "",
  "site_id": "",
  "api_key": ""
}

paths = {
  "classic": "",
  "new": "",
  "site": "",
}

# authentication into tableau's REST API with a valid JWT
def auth(env_dict, jwt):

  credentials['server'] = env_dict['TABLEAU_SERVER']
  credentials['api_version'] = env_dict['TABLEAU_RESTAPI_VERSION']
  paths['classic'] = f"{credentials['server']}/api/{credentials['api_version']}"
  paths['new'] = f"{credentials['server']}/api/exp"

  print('classic', paths["classic"])
  print('server', credentials["server"])

  auth_url = f'{paths["classic"]}/auth/signin'

  print('auth_url: ', auth_url)

  auth_payload = """
  <tsRequest>
    <credentials jwt="{0}">
      <site contentUrl="{1}"/>
    </credentials>
  </tsRequest>
  """

  """
  <tsRequest>
    <credentials jwt="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImlzcyI6IjZhOGEyZTg0LWNkODktNGJmMi1hMzA0LWIwZmIwNjk1ZjUxYiIsImtpZCI6ImM1ZDI5M2U0LTJhMTMtNDAwMy05MTE3LWZhYjBjMTdmZDhmZSJ9.eyJpc3MiOiI2YThhMmU4NC1jZDg5LTRiZjItYTMwNC1iMGZiMDY5NWY1MWIiLCJzdWIiOiJzLnByaWNlQHNhbGVzZm9yY2UuY29tIiwiYXVkIjoidGFibGVhdSIsImV4cCI6MTY1ODQ3NDExMiwianRpIjoiYTcwOWU3N2YtMWMxYS00OTkxLWIwZTItODgwZmY3ZjAwOGJlIiwic2NwIjpbInRhYmxlYXU6Y29udGVudDpyZWFkIiwidGFibGVhdTp3b3JrYm9va3M6Y3JlYXRlIl19.c654sXbEYRbi0BdRTUDlF70ZhDJalNZs_y0ScMOe1eU">
      <site contentUrl="tc22broadcast"/>
    </credentials>
  </tsRequest>
  """

  auth_headers = {
    'Content-Type': 'application/xml',
    'Accept': 'application/json'
  }
  print(jwt)
  print(auth_payload.format(jwt, env_dict["TABLEAU_SITENAME"]))
  

  response = requests.request("POST", auth_url, headers=auth_headers, data=auth_payload.format(jwt, env_dict["TABLEAU_SITENAME"]))

  response_body = response.json()

  print('/auth response body: ', json.dumps(response_body, indent=4, sort_keys=True))

  # obtain dict values from response
  credentials["site_id"] = response_body["credentials"]["site"]["id"]
  credentials["api_key"] = response_body["credentials"]["token"]
  paths['site'] = f"sites/{credentials['site_id']}/"

  return credentials["api_key"]


def get_workbooks_site(api_key):
  # get a list of views for a site
  query_parameters = f'pageSize=1&fields=_all_'

  workbooks_url = f'{paths["classic"]}/{paths["site"]}workbooks?{query_parameters}'

  print('workbooks_url: ', workbooks_url)

  payload={}
  headers = {
    'Accept': 'application/json',
    'X-Tableau-Auth': api_key
  }

  response = requests.request("GET", workbooks_url, headers=headers, data=payload)

  response_body = response.json()

  print('/workbooks response body: ', json.dumps(response_body, indent=4, sort_keys=True))
