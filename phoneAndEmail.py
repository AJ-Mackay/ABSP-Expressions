#! python3

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?    # area code (optional)
(\s|-)                      # first separator
\d\d\d                      # first three digits
-                           # separator
\d\d\d\d                    # last four digits
(((ext(\.)?\s)|x)           # extention word-part (optional)
(\d{2,5}))?                 # extention number-part (optional)
)
''', re.VERBOSE)

# Create a regex for email addresses - only covers the use of .+_
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+             # name part
@                           # @ symbol
[a-zA-Z0-9_.+]+             # domain name part
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedEmail = emailRegex.findall(text)
extractedPhone = phoneRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# TODO: Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
