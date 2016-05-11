class SelectionValidator(object):

  def is_valid(self, user_input, options):
    empty_string = ''
    return user_input.isdigit() and user_input != empty_string and self.__is_within_range_of_options(user_input, options)

  def __is_within_range_of_options(self, user_input, options):
    return int(user_input) <= len(options) and int(user_input) > 0