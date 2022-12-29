import argparse, uuid
import session

class CLI:
  """
  """

  def __init__(self, env_dict):
    self.env = env_dict
    self.id = uuid.uuid4()
    self.session
    self.sessions = {}
    self.parser = argparse.ArgumentParser()
    self.__init_parser()
    self.args = self.parser.parse_args()
    self.__parse()

  def __str__(self):
    return f""

  # adds positional and optional arguments to the parser
  def __init_parser(self):
    self.parser.add_argument("new")
    self.parser.add_argument("-t", "--jwt", action="store_true")
    self.parser.add_argument("-k", "--key", action="store_true")
    self.parser.add_argument("-l", "--list")

  # defines responses to CLI arguments
  def __parse(self):
    while self.args.new:
      # creates a new session object
      self.session = session.Session(self.env)
      self.__handle_session()
      self.__add_session()

  def __handle_session(self):
    if self.args.t:
      # only outputs JWT
      return self.session.get_JWT()
    if self.args.k:
      # only outputs API KEY
      return self.session.get_key()
    # outputs the full session
    return self.session.get_session()

  def __add_session(self):
    self.sessions.update({
      self.id: self.session
    })
