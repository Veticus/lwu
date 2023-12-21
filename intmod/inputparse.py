import re

input = ["lolcake", "4", "l3", "e7"]

# Wordlength:
#   Identify if exists
#   Maximum one
#   Either one or two digits
#   If not exists:
#       Show matches for all lengths
#   If exists:
#       Show matches for only this length

# Spotletters:
#   Identify if exist
#   If exist:
#       For each:
#           Split into letter and number
#           Look for match with letter at number position


spotletters = [s for s in input if re.compile(r'[a-zA-Z]\d{1,2}').search(s)]
letters = [s for s in input if re.compile(r'^[a-z]{2,40}$').search(s)]
wordlength = [s for s in input if re.compile(r'^\d{1,2}$').search(s)]

# Print the matches
print(spotletters)
print(letters)
print(wordlength)
