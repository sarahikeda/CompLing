# # translate sentence from German to English
# mydict = {"befreit":"liberated", "baeche":"brooks", "eise":"ice", "sind":"are", "strom":"river", "und":"and", "vom":"from"}

# def tokenize(sentence):
#   return sentence.split(" ")

# #1st way
# def translate(sentence):
#   words = tokenize(sentence)
#   for word in words:
#     if word in mydict:print(mydict[word], end=" ")

# translate("vom eise befreit sind strom und baeche")

# #2nd way
# def whole_sentence_translation(sentence):
#   words = tokenize(sentence)
#   translation = []
#   for word in words:
#     if word in mydict:
#       translation.append(mydict[word])
#   return " ".join(translation)
# print(whole_sentence_translation("vom eise befreit sind strom und baeche"))


# count occurrences of all words
paragraph = "While dieters are accustomed to exercise of will, a new English translation of Germany's most popular diet book takes the concept to a new philosophical level. Thie nietzschean diet, which commands it adherents to eat superhuman amounts of whatever they most fear is developing a strong following in America."

def count_words(paragraph):
  count = {}
  for word in paragraph.split():
    if word not in count:
      count[word] = 1
    else:
      count[word] +=1
  return count
print(count_words(paragraph))

# to sort values instead of keys
# def second_of_tuple(t):
#   return t[1]

# sorted(counts.items(), key = second_of_tuple)

# # alternatively
# sorted(counts.items(), key = lambda t:t1[])
# # lambda is the placeholder for the method

# sorted(counts.keys(), key = lambda word:counts[word], reverse = True)

# # lambda = nameless function
# # in lieu of docs
# help(sorted)
# help(print)

# # shorthand for loop with list comprehension
# [w.lower() for w in words]
