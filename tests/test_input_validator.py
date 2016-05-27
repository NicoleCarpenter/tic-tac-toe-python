import unittest
from lib.input_validator import InputValidator

class TestInputValidator(unittest.TestCase):

  def setUp(self):
    self.validator = InputValidator()

  def test_is_valid_return_string(self):
    self.assertEquals(self.__is_valid_return('John Smith'), True)
    self.assertEquals(self.__is_valid_return('John!'), True)
    self.assertEquals(self.__is_valid_return(' John'), True)

  def test_is_valid_return_special_chars_valid(self):
    self.assertEquals(self.__is_valid_return('\tJohn'), True)
    self.assertEquals(self.__is_valid_return('\rJohn'), True)
    self.assertEquals(self.__is_valid_return('\nJohn'), True)

  def test_is_valid_return_special_chars_invalid(self):
    self.assertEquals(self.__is_valid_return('\t'), False)
    self.assertEquals(self.__is_valid_return('\r'), False)
    self.assertEquals(self.__is_valid_return('\n'), False)
    self.assertEquals(self.__is_valid_return(''), False)
    self.assertEquals(self.__is_valid_return(' '), False)

  def __is_valid_return(self, name):
    return self.validator.is_valid(name)