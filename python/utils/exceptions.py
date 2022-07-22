from utils import log

class Error(Exception):
  """base class for errors"""

class EnvironmentError(Error):
  """
  Exception raised when environment variables are empty or not strings

  Attributes:
    key_attribute -- environment variable
  """

  def __init__(self, environment_variable):
    self.environment_variable = environment_variable
    self.message = f"Environment variable value for key {environment_variable} was not assigned."
    super().__init__(self.message)
    
class JWTEncodingError(Error):
  """
  Exception raised when encoding fails

  Attributes:
    key_attribute -- environment variable
    key_attribute -- environment variable
  """

  def __init__(self, error):
    self.message = f"Cannot encode JWT: {error}"
    self.log = log.logger.error(f"cannot encode JWT, {error}")
    super().__init__(self.message)
    