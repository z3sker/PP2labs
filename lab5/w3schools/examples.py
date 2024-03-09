# Python RegEx

import re

# Search the string to see if it starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

# Function	Description
    # findall	Returns a list containing all matches
    # search	Returns a Match object if there is a match anywhere in the string
    # split	Returns a list where the string has been split at each match
    # sub	Replaces one or many matches with a string

# Metacharacters
    # Character	Description
    # []	A set of characters
    # \	Signals a special sequence (can also be used to escape special characters)
    # .	Any character (except newline character)
    # ^	Starts with
    # $	Ends with
    # *	Zero or more occurrences
    # +	One or more occurrences
    # ?	Zero or one occurrences
    # {}	Exactly the specified number of occurrences
    # |	Either or
    # ()	Capture and group

# Special Sequences
    # \A	Returns a match if the specified characters are at the beginning of the string
    # \b	Returns a match where the specified characters are at the beginning or at the end of a word
    # \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
    # \d	Returns a match where the string contains digits (numbers from 0-9)
    # \D	Returns a match where the string DOES NOT contain digits
    # \s	Returns a match where the string contains a white space character
    # \S	Returns a match where the string DOES NOT contain a white space character
    # \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
    # \W	Returns a match where the string DOES NOT contain any word characters
    # \Z	Returns a match if the specified characters are at the end of the string


# The findall() Function
txt = "The rain in Spain"
x = re.findall("ai", txt)

# The search() Function
txt = "The rain in Spain"
x = re.search("\s", txt)

# The split() Function
txt = "The rain in Spain"
x = re.split("\s", txt)

# The sub() Function
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)

# Match Object
txt = "The rain in Spain"
x = re.search("ai", txt)