from utils import exceptions, log

# dictionary with required environment variables
env_vars = [
  "TABLEAU_SERVER",
  "TABLEAU_SITENAME",
  "TABLEAU_USERNAME",
  "TABLEAU_CA_CLIENT",
  "TABLEAU_CA_SECRET_ID",
  "TABLEAU_CA_SECRET_VALUE"
]

def validate(env_dict):
  # check that each environment variable has been declared and assigned
  for vars in env_vars:
    try:
      # check the local dictionary pulled from os.environ
      env_dict[vars]

      # check that key value length is non-zero
      if len(env_dict[vars]) == 0:
        log.logger.critical(f"Environment variable value for key {vars} was not assigned.")
        raise exceptions.EnvironmentError(vars)

    except KeyError:
      # raises error if an environment variable has not been declared
      log.logger.critical(f"Environment variable {vars} was not declared.")
      raise RuntimeError(f"Environment variable {vars} was not declared.")
