########
# Your name and EID:
# Sarah Ing
# #########
# # Problem 1:
# c) my-string - hyphen is an illegal character
# d) 123list - needs to start with a letter
# e) def - one of the defined Python keywords
# f) my string - there is a space
#
# extra credit: VAR - used to distinguish constants
#########
# Problem 2:
f = open("wells.txt")
file_contents = f.read()
print(file_contents.count("of"))

#########
# Problem 3:
import string
tokenized_file = file_contents.split()
no_punc = []
for word in tokenized_file:
    no_punc.append(word.rstrip(string.punctuation))
print(no_punc)
#########
# Problem 4:
count = 0
for word in no_punc:
    if word.endswith("ing"):
        count +=1
print(count)
#########
# Problem 5:
stemmed_words = []
for word in no_punc:
    if word.endswith("ing"):
        word = word.replace("ing", '')
    elif word.endswith("s"):
        word = word.replace("s", '')
    elif word.endswith("ed"):
        word = word.replace("ed", '')
    stemmed_words.append(word)
print(stemmed_words)
#########
# Problem 6:
file = open('pg768.txt')
bronte_string = file.read()
f.close()
def find_index(sentence1, sentence2):
    start_length = len(sentence1)
    start_index = bronte_string.index(sentence1)
    start = start_index + start_length
    end = bronte_string.index(sentence2)
    return (bronte_string[start:end])
print(find_index("***START OF THE PROJECT GUTENBERG EBOOK WUTHERING HEIGHTS***", "***END OF THE PROJECT GUTENBERG EBOOK WUTHERING HEIGHTS***"))
