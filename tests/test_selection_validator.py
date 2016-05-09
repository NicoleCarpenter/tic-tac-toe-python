import unittest
from lib.selection_validator import SelectionValidator

class TestSelectionValidator(unittest.TestCase):

  def setUp(self):
    self.validator = SelectionValidator()

  def test_is_valid(self):
    options = ['1 - First', '2 - Second', '3 - Third']
    
    selection = '1'
    is_valid = self.validator.is_valid(selection, options)
    self.assertEquals(is_valid, True)

    selection = '3'
    is_valid = self.validator.is_valid(selection, options)
    self.assertEquals(is_valid, True)

    selection = '0'
    is_valid = self.validator.is_valid(selection, options)
    self.assertEquals(is_valid, False)

    selection = '-1'
    is_valid = self.validator.is_valid(selection, options)
    self.assertEquals(is_valid, False)

    selection = '1.5'
    is_valid = self.validator.is_valid(selection, options)
    self.assertEquals(is_valid, False)

    selection = '4'
    is_valid = self.validator.is_valid(selection, options)
    self.assertEquals(is_valid, False)

    selection = ''
    is_valid = self.validator.is_valid(selection, options)
    self.assertEquals(is_valid, False)

    selection = ' '
    is_valid = self.validator.is_valid(selection, options)
    self.assertEquals(is_valid, False)

    selection = 'a'
    is_valid = self.validator.is_valid(selection, options)
    self.assertEquals(is_valid, False)

    selection = '!'
    is_valid = self.validator.is_valid(selection, options)
    self.assertEquals(is_valid, False)