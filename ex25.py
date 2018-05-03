# ex25.py
# even more practice

def break_words(stuff):
    """this function will break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sorts the words."""
    return sorted(words)

def print_first_word(words):
    """prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


#import ex25
#sentence = "all good things come to those who wait."
#words = ex25.break_words(sentence)
#words
#sorted_words = ex25.sort_words(words)
#sorted_words
#ex25.print_first_word(words)
#ex25.print_last_word(words)
#words
#ex25.print_first_word(sorted_words)
#ex25.print_last_word(sorted_words)
#sorted_words
#sorted_words = ex25.sort_sentence(sentence)
#sorted_words
#ex25.print_first_and_last(sentence)
#ex25.print_first_and_last_sorted(sentence)
