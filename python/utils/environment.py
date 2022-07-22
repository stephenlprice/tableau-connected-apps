from utils import exceptions, log

def validate(environment, env_vars):
  # check that each environment variable has been declared and assigned
  for vars in env_vars:
    try:
      # check the local dictionary pulled from os.environ
      environment[vars]

      # check that key value length is non-zero
      if len(environment[vars]) == 0:
        log.logger.critical(f"Environment variable value for key {vars} was not assigned.")
        raise exceptions.EnvironmentError(vars)

    except KeyError:
      # raises error if an environment variable has not been declared
      log.logger.critical(f"Environment variable {vars} was not declared.")
      raise RuntimeError(f"Environment variable {vars} was not declared.")
