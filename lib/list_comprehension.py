#!/usr/bin/env python3

def return_evens(num_list):
    # even_elements = [(n % 2 == 0) for n in num_list]
    even_elements = [n for n in num_list if (n % 2 == 0)]
    return even_elements

print(return_evens([0, 1, 3, 5, 7, 8, 9]))
print(return_evens([9,5,6,8,0,2,5,4,6,1,1,2,0,9]))

def make_exclamation(sentence_list):
    words = [word + "!" for word in sentence_list]
    return words

print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))