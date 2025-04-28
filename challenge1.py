from lib.helpers import check_that_these_are_equal

# Challenge 1
#
# You need to create a function called 'summary' which will accept an array/list as a parameter (argument) e.g. words
# You need to build a string and return it from your function. By default if nothing is returned a function will return 'None'
# You need to iterate through each word in the array to build your string but there are these conditions:
# - If the string length is less than 20 you should add the word to the string with a trailing comma and space ', '
# - If the string length is greater than or equal to 20 you should add 15 the first 15 to the string with trailing dots '...'

# Add your function definition here:



# Tests around your function are below:

check_that_these_are_equal(
  summary(["I am the first string", "I am the second string", "I am the very very long third string"]),
  "I am the first string, I am the second string, I am the very very l..."
)






