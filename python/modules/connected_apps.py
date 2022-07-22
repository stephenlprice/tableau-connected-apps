import datetime, uuid
import jwt


def encode(env_vars):
  # tableau connected app variables (JWT) see: https://help.tableau.com/current/online/en-us/connected_apps.htm#step-3-configure-the-jwt
  header_data = {
    "iss": env_vars["TABLEAU_CA_CLIENT"],
    "kid": env_vars["TABLEAU_CA_SECRET_ID"],
    "alg": "HS256",
  }

  payload_data = {
    "iss": env_vars["TABLEAU_CA_CLIENT"],
    "sub": env_vars["TABLEAU_USERNAME"],
    "aud": "tableau",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
    "jti": str(uuid.uuid4()),
    "scp": ["tableau:content:read", "tableau:workbooks:create"]
  }

  connected_app_secret = env_vars["TABLEAU_CA_SECRET_VALUE"]

  # encode the JWT with declared payload, secret and headers
  token = jwt.encode(
    payload = payload_data,
    key = connected_app_secret,
    headers = header_data
  )
  print(f'encoded token: {token}')

  decode(token, connected_app_secret, payload_data["aud"], header_data["alg"])


# decode the JWT for testing purposes
def decode(token, connected_app_secret, audience, algorithms):
  decodedToken = jwt.decode(
    jwt = token, 
    key = connected_app_secret,
    audience = audience, 
    algorithms = algorithms
  )
  print(f'decoded token: {decodedToken}')



