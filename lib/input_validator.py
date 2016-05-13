import abc
from lib.validator import Validator

class InputValidator(Validator):

  def is_valid(self, user_input):
    return not self.__is_blank(user_input)

  def __is_blank(self, user_input):
    empty_string = ''
    return user_input.isspace() or user_input == empty_string