import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # brackets to break up the number into area code and phone number.
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo.group()) # print full number
print(mo.group(1)) # print just area code
print(mo.group(2)) # rest of the number

phoneNumRegex2 = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo2 = phoneNumRegex2.search('My number is (415) 555-4242')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo3 = batRegex.search('Batmobile lost a wheel')
print(mo3.group())
print(mo3.group(1))

#mo4 = batRegex.search('Batmotorcycle lost a wheel')
#mo4 == None
#print(mo4.group())
