import re

# ? = match one or zero times.
# If a "?" is part of the text string use escape characters "\?"
# batRegex = re.compile(r'Batman|Batwoman) - same as below.
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())

mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # requires area code.
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
print(mo.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
print(mo.group())

# * = match zero or more times.
# If a "*" is part of the text string use escape characters "\*"
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowowowowowoman')
print(mo.group())

# + = match one or more.
# If a "+" is part of the text string use escape characters "\+"
batRegex = re.compile(r'Bat(wo)+man')
# mo = batRegex.search('The Adventures of Batman') - WILL BREAK
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowowowowowoman')
print(mo.group())


regex = re.compile(r'\+\*\?')
mo = regex.search('I learned about +*? regex syntax')
print(mo.group())

regex = re.compile(r'(\+\*\?)+')
mo = regex.search('I learned about +*?+*?+*?+*?+*? regex syntax')
print(mo.group())

# haRegex = re.compile(r'HaHaHa') - same as below.
haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())

# Looking for three phone numbers in a row, area code and commas are optional.
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
print(phoneRegex.findall('My numbers are 415-555-1234,555-4242,212-555-0000'))
# TODO - Find out why this ^^^ is not working properly.

# {x,y} (at least x, at most y)
haRegex = re.compile(r'(Ha){3,5}') # {,5} = Same as 0:5. {3,} = must have at least 3.
mo = haRegex.search('He said "HaHaHaHa"')
print(mo.group())

# Greedy vs. Nongreedy matching
digitRegex = re.compile(r'(\d){3,5}') # "Greedy match" - returns '12345'
mo = digitRegex.search('1234567890')
print(mo.group())

digitRegex = re.compile(r'(\d){3,5}?') # "Nongreedy match" - returns '123'
mo = digitRegex.search('1234567890')
print(mo.group())
