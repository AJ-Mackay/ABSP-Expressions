# Module 10 - Regular Expressions: Regex Dot-Star and the Caret/Dollar Characters

# ^ (Caret) = The string must begin with.
# $ (Dollar) = The string must end with.
# . (Dot/Period) = Any character except newline.
# .* (Dot Star) = Any pattern at all. (.*) is greedy. (.*?) is non-greedy.

import re

beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello there!'))
print(beginsWithHelloRegex.search('He said "Hello!"')) # returns 'None' as 'Hello' is not at the start of the string.

endsWithWorldRegex = re.compile(r'world!$')
print(endsWithWorldRegex.search('Hello world!'))
print(endsWithWorldRegex.search('Hello world!srghiurehgiureu')) # returns 'None'.

allDigitsRegex = re.compile(r'^\d+$') # Must contain the WHOLE string, in this case the string must start with(^), end with($), and contain more than(+) one digit.
print(allDigitsRegex.search('2587432859734587'))
print(allDigitsRegex.search('25874328x59734587')) # returns 'None' as "x" is not a digit.

atRegex = re.compile(r'.at') # Anything followed by "at".
print(atRegex.findall('The cat in the hat sat on the flat mat.')) # returns ['cat', 'hat', 'sat', 'lat', 'mat'] - notice 'lat' from "flat".

atRegex = re.compile(r'.{1,2}at') # One or two characters followed by "at".
print(atRegex.findall('The cat in the hat sat on the flat mat.')) # returns [' cat', ' hat', ' sat', 'flat', ' mat'] - included the space in front of words.

# Example: Index Math
# 'First Name: Al Last Name: Sweigart'.find(':') - returns '10' as the colon appears at index 10.
# 'First Name: Al Last Name: Sweigart'.find(':') + 2 - returns index '12'.
# 'First Name: Al Last Name: Sweigart'[12:] - returns 'Al Last Name: Sweigart'.

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Al Last Name: Sweigart')) # retusn [('Al', 'Sweigart')]

serve = '<To serve humans> for dinner.>'

nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve)) # returns ['To serve humans']

greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve)) # returns ['To serve humans> for dinner.']

prime = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
print(prime)

dotStar = re.compile(r'.*')
print(dotStar.search(prime)) # returns 'Serve the public trust.' - "." does not include newlines ("\n").

dotStar = re.compile(r'.*', re.DOTALL) # Adding the second argument makes the dot mean EVERYTHING including newlines.
print(dotStar.search(prime)) # returns 'Serve the public trust.\nProtect the innocent.\nU' as it matches the entire string.
# Note: Is there a possible character limit of the .Match() function as "phold the law." was not returned?

# Example: Ignore case
# vowelRegex = re.compile(r'[aeiou]') - will only return lowercase vowels in this example - ['o', 'e', 'o', 'u', 'o', 'a', 'i', 'o', 'o', 'a', 'a', 'o', 'u', 'o', 'o', 'o', 'o', 'u'].
vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE) # will ignore the case of the vowels in this example. "re.I" (shorthand version) also works.
print(vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?')) # includes the capital A from "Al" - ['A', 'o', 'e', 'o', 'u', 'o', 'a', 'i', 'o', 'o', 'a', 'a', 'o', 'u', 'o', 'o', 'o', 'o', 'u'].
