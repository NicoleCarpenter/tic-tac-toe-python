import unittest
from lib.input_validator import InputValidator

class TestInputValidator(unittest.TestCase):

  def setUp(self):
    self.validator = InputValidator()

  def is_valid_return(self, name):
    return self.validator.is_valid(name)

  def test_is_valid_return(self):
    self.assertEquals(self.is_valid_return('John Smith'), True)
    self.assertEquals(self.is_valid_return('John!'), True)
    self.assertEquals(self.is_valid_return(' John'), True)
    self.assertEquals(self.is_valid_return('\tJohn'), True)
    self.assertEquals(self.is_valid_return('\rJohn'), True)
    self.assertEquals(self.is_valid_return('\nJohn'), True)
    self.assertEquals(self.is_valid_return('\t'), False)
    self.assertEquals(self.is_valid_return('\r'), False)
    self.assertEquals(self.is_valid_return('\n'), False)
    self.assertEquals(self.is_valid_return(''), False)
    self.assertEquals(self.is_valid_return(' '), False)