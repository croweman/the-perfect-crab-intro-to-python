from lib.helpers import check_that_these_are_equal

# Challenge 5
#
# You need to create a function called 'get_third_lowest_and_highest_numbers' which will accept an array/list of numbers as a parameter (argument) e.g. numbers
# You need to find the third lowest and second highest numbers and return them as an array/list which will only contain 2 numbers
# The array/list will not be in order so you will need to ensure it is
# You will always be given at least 2 numbers
# By default if nothing is returned a function will return 'None'

# Add your function definition here:



# Tests around your function are below:

check_that_these_are_equal(
  get_third_lowest_and_highest_numbers([3, 5, 7, 4, 2, 1, 8, 9, 6]),
  [3, 7]
)

check_that_these_are_equal(
  get_third_lowest_and_highest_numbers([88, 4]),
  [4, 88]
)

