import os, inspect
from dotenv import load_dotenv
from modules import interface
from utils import log, environment


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

  cli = interface.CLI()

