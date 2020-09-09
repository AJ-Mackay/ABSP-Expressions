# Module 10 - Regular Expressions: Regex sub() Method and Verbose Mode.

# .sub('ar1', 'arg2') = Substitution/"Find and Replace" method. 'arg1' - what is to be used. 'ar2' - the string to use it in.
# r = raw string of text.
# ''' or """ (at beginning and end) - Multiple lines of text.

import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')) # returns ['Agent Alice', 'Agent Bob'].
print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.')) # returns 'REDACTED gave the secret documents to REDACTED.'

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')) # returns ['A', 'B'] as "(\w)" is a group.
# "\w*" means with more alphabetical characters following.

print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.')) # returns 'Agent A**** gave the secret documents to Agent B****.'
# "\1" refers to the first group ("(\w)" above).
# "****" are placeholders to disguise how many characters are in the rest of the name by making them all the same length.

# Example: Regular Expressions vs Verbose Expressions
# re.compile(r'\(\d\d\d)(-)?\d\d\d-\d\d\d\d) - '(415) 555-5555' and '415-555-5555' are both accepted, but can be confusing at a later date.
# re.compile(r''' MULTILINE TEXT ''', re.VERBOSE) - Allows you to add whitespace and comments (Ignored by the program) to the regex string passed to re.compile().

re.compile(r'''
(\d\d\d-) |   # area code (without parens, with dash)
(\(\d\d\d) )  # -or- area code with parens and no dash
\d\d\d        # first 3 digits
-             # second dash
\d\d\d\d      # last 4 digits
\sx\d{2,4}    # extension with a space in front (from two to four digits), e.g ' x1234'.''', re.VERBOSE)

### If you want to pass multiple arguments to .compile(), you need to combine them with the bitwise('|' aka 'pipe') operator. ###
### re.compile(r''' Multiline text''', re.DOTALL | re.IGNORECASE | re.VERBOSE) - Remember: "re.IGNORECASE" & "re.I" are interchangeable. ###
### THIS CAN ONLY BE DONE WITH "re.compile()" IN PYTHON. ###
