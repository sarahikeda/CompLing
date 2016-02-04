def which_larger(word1,word2):
    if word1 < word2:
        print(word1 + " wins!")
        return True
    else:
        print("word 2 is the winner!")
        return False

which_larger("watermelon", "zebra")

def filter_function_one_word(word):
    stop_words = ["the", "a", "in", "and"]
    if word in stop_words:
        return None
    else:
        return word
print ("Filtering out function words for one word:")
print(filter_function_one_word("the"))
print(filter_function_one_word("apple"))

print("Filtering out function words for one sentence:")
print(filter_function_words("went to the store"))

def noun_detective(sentence):
    if sentence[0] == sentence[0].capitalize():
        return True
    elif sentence.endswith("ism") or sentence.endswith("ion"):
        return True
    else:
        return False
print("Noun detective: ")
print(noun_detective("So much"))
print(noun_detective("so altruism"))
print(noun_detective("tree"))
