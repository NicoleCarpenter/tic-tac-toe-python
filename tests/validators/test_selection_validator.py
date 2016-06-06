import unittest
from lib.validators.selection_validator import SelectionValidator

class TestSelectionValidator(unittest.TestCase):

  def setUp(self):
    self.validator = SelectionValidator()

  def is_valid_return(self, selection):
    options = ['1 - First', '2 - Second', '3 - Third']
    return self.validator.is_valid(selection, options)

  def test_is_valid(self):
    self.assertEquals(self.is_valid_return('1'), True)
    self.assertEquals(self.is_valid_return('3'), True)

  def test_is_valid_fail_number(self):
    self.assertEquals(self.is_valid_return('0'), False)
    self.assertEquals(self.is_valid_return('-1'), False)
    self.assertEquals(self.is_valid_return('1.5'), False)
    self.assertEquals(self.is_valid_return('4'), False)

  def test_is_valid_fail_char(self):
    self.assertEquals(self.is_valid_return('a'), False)
    self.assertEquals(self.is_valid_return('!'), False)
    self.assertEquals(self.is_valid_return(''), False)
    self.assertEquals(self.is_valid_return(' '), False)