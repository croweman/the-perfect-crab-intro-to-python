from lib.helpers import check_that_these_are_equal

# Challenge 3
#
# You need to create a function called 'get_number_of_differences_of_two' which will accept a string as a parameter (argument) e.g. message
# You need to return the number of characters where the next character (integer) is exactly 2 less than the previous character (integer)
# By default if nothing is returned a function will return 'None'

# Add your function definition here:



# Tests around your function are below:

check_that_these_are_equal(
  get_number_of_differences_of_two("975310"),
  4
)

check_that_these_are_equal(
  get_number_of_differences_of_two("967868357"),
  2
)









