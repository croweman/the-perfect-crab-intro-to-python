from lib.helpers import check_that_these_are_equal

# Challenge 6
#
# You need to create a function called 'get_number_of_twos' which will accept astring as a parameter (argument) e.g. message
# You need to get the count of all 2 characters in the string and return the count
# By default if nothing is returned a function will return 'None'

# Add your function definition here:



# Tests around your function are below:

check_that_these_are_equal(
  get_number_of_twos("1297624590adsflkj254902fgmn64pAre2"),
  5
)

check_that_these_are_equal(
  get_number_of_twos("lkjasdf098562asdf2lkjsdfglkjsdfgoiuertlkdfgoiudfglkr2lkjdfgoiud"),
  3
)
