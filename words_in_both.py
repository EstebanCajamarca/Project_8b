# Author: Esteban Cajamarca
# GitHub username: EstebanCajamarca
# Date: 2/19/2022

# Write a function named words_in_both that takes two strings as parameters and returns a set of only those words
# that appear in both strings. You can assume all characters are letters or spaces.
def words_in_both(sentence_1, sentence_2):
    """ Takes two strings as input, split them to further print all repeated words."""
    words_sentence_1 = set(sentence_1.lower().split(" "))  # changing to lower case/splitting sentence
    words_sentence_2 = set(sentence_2.lower().split(" "))
    return words_sentence_1.intersection(words_sentence_2)  # returning only repeated values


"""Testing
common_words = words_in_both("She is a jack of all trades", 'Jack was tallest of all')
print(common_words)
"""
