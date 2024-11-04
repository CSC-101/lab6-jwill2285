import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp

# Part 1
def selection_sort_books(books : list[data.Book])->list[data.Book] or None:
    #checks if list is empty
    if books == []:
        return None
    else:
        #runs through the whole list of books
        for i in range(len(books)):
            idx = i
            #checks each book to see if it is in the correct spot, if so keeps it, if not...
            #changes it
            for j in range(i+1,len(books)):
                if books[j].title < books[idx].title:
                    idx = j
            books[i], books[idx] = books[idx], books[i]
        return books
# Part 2
def swap_case(word : str)->str:
    new_str = ""
    for i in word:
        #checks if letter is lowercase, if so uppers it
        if i.islower():
            new_str += i.upper()
        #checks if letter is uppercase, if so lowers it
        elif i.isupper():
            new_str += i.lower()
        #any other non letter thing is returned as is
        else:
            new_str += i
    return new_str
# Part 3
def str_translate(word : str, old : str, new: str)->str:
    #defines new string for changed words
    changed_word = ""
    for i in word:
        #checks if the letter is either lowercase or uppercase of the old letter
        #if it is, returns the same capitalization
        if i == old.lower():
            changed_word += new.lower()
        elif i == old.upper():
            changed_word += new.upper()
        #if not letter just adds to string
        else:
            changed_word += i
    return changed_word
# Part 4
def histogram(many_words : str)->dict:
    #creates a dictionary
    word_dict = {}
    #splits the string into list of all words in it
    words = many_words.split()
    for i in words:
        #checks if word is already in dictionary, if so adds one to counter
        if i in word_dict:
            word_dict[i] +=1
        #if word not already in dictionary, adds it to dictionary
        else:
            word_dict[i] = 1
    return word_dict
