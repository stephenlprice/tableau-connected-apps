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
    