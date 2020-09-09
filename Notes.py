# Module 10 - Regular Expressions: Regex Character Classes and the findall() method.

# .findall() - returns a list of ALL suitable phone numbers, not just the first as .search() does.

# Example 1:
# phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# phoneRegex.search(document) - will return: '508-555-5555'.
# phoneRegex.findall(document) - will return strings: ['508-555-5555', '508-555-1234']

# Example 2:
# phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# phoneRegex.findall(document) - will return tuples: [('508','555-5555'), ('508','555-1234')]

# Example 3: will return a list of groups as there are now three groups, combining the above results (full number and the tuples).
# phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
# phoneRegex.findall(document) - returns: [('508-555-5555', '508', '555-5555'), ('508-555-1234', '508', '555-1234')]

# "|" means "or".
# "\d" (digit) is the same as "0|1|2|3|4|5|6|7|8|9".

# \d = Numeric digits from 0 to 9.
# \D = Any character that is NOT a numeric digit.
# \w = Letters, Digits or Underscore.
# \W = Any character that is not a letter, digit or underscore.
# \s = Space, tab or newline characters.
# \S = Any character that is not a space, tab or newline character.

# Example 4:

import re

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics)) # returns ['12 drummers', '11 pipers', ... '1 partridge'].

vowelRegex = re.compile(r'[aeiouAEIOU]') # same as r'(a|e|i|o|u|A|E|I|O|U)' - lowercase and caps. For all letters including caps: r'(a-zA-Z)'
print(vowelRegex.findall('Robocop eats baby food.')) # returns ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o'].

doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(doubleVowelRegex.findall('Robocop eats baby food.')) # returns ['ea', 'oo'] - two vowels in a row ('ea'ts f'oo'd).

# Example 5: Negative character classes.

consonantsRegex = re.compile(r'[^aeiouAEIOU]') # returns EVERYTHING that is not a vowel (caps, lowercase, spaces, punctuation).
print(consonantsRegex.findall('Robocop eats baby food.')) # returns ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.']
