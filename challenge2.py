from lib.helpers import check_that_these_are_equal

# Challenge 2
#
# You need to create a function called 'character_difference' which will accept a string as a parameter (argument) e.g. message
# You need to return either True or False from your function. By default if nothing is returned a function will return 'None'
# You will need to look for characters 'a' and 'b' and get the position difference in the string.
# !!!! There may be multiple 'a' characters in the message so you will need to find all positions of 'a' (a loop to check differences) !!!
# There are these conditions:
# - If the number of characters between these two characters is 5 return True
# (it doesn't matter if there are multiple 'a' characters, as soon as the condition is met you can return True)
# - Otherwise return False

# Add your function definition here:



# Tests around your function are below:

check_that_these_are_equal(
  character_difference("lorem ipsum ande bananas"),
  True
)

check_that_these_are_equal(
  character_difference("a loram ipsum ande bananas"),
  True
)

check_that_these_are_equal(
  Summary("He is dumb"),
  False
)







