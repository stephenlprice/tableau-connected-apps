from utils import exceptions


def validate(env_dict):
  # dictionary with required environment variables
  env_vars = [
    "TABLEAU_SERVER",
    "TABLEAU_SITENAME",
    "TABLEAU_RESTAPI_VERSION",
    "TABLEAU_USERNAME",
    "TABLEAU_CA_CLIENT",
    "TABLEAU_CA_SECRET_ID",
    "TABLEAU_CA_SECRET_VALUE"
  ]
  # check that each environment variable has been declared and assigned
  for vars in env_vars:
    try:
      # check the local dictionary pulled from os.environ
      env_dict[vars]

      # check that key value length is non-zero
      if len(env_dict[vars]) == 0:
        raise exceptions.EnvironmentAttributeError(vars)

    except KeyError as error:
      # raises error if an environment variable has not been declared
      raise exceptions.EnvironmentKeyError(vars, error)
