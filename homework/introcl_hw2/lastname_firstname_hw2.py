###
# Name and EID:

#########
# Problem 1a:
import re
f = open("../introcl_hw1/wells.txt")
file_contents = f.read()
lowercase_wells= file_contents.lower()

def find_one_syllables(text):
  count = 1
  for word in text:
    if re.search("[^aeiou]*[aeiou]+[^aeiou]*", word):
      count +=1
  print(count)

find_one_syllables(lowercase_wells)
#########
# Problem 1b:
# bite

#########
# Problem 2:

#########
# You can do problems 3-5 on paper, if you like.
# But please don't forget to put your name on the paper!

