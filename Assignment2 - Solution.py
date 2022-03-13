# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def reverse(sentence, reverse_word):
    if sentence.isalpha() ==False or reverse_word.isalpha() ==False:
        return(print("invalid input"))
    elif reverse_word not in sentence:
        return(print("The word was not found")) 
    new_word= reverse_word[len(reverse_word)::-1]
    sentence=sentence.replace(reverse_word,new_word)
    return(print(sentence))


#print(reverse("abcdefg", "ab"))

sentence=input("Enter a sentence: ")
reverse_word=input("Enter a word to reverse: ")
reverse(sentence, reverse_word)
