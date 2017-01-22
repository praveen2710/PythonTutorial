###Regex

##Uses of regex

#String validation: eg:validate email address

#String substituions: replace string in text editor

import re

pattern = r"eggs"

##match function checks only start of string here
if(re.match(pattern,"beggsandbreadeggs")):
    print("match found")
else:
    print("No match found")

#search function checks for pattern in complete string
if(re.search(pattern,"beggesandbreadegg")):
    print("search match found")
else:
    print("No search match found")

#finall function checks for pattern in complete string and returns a list
#of all matched strings
print(re.findall(pattern,"beggsandbreadeggs"))


string = "My name is John, Hi I'm John"

pattern2 = r"John"

#sub will replace all John with Jane
newString = re.sub(pattern2,"Jane",string)
print (newString)

##More on pattern string
# . meta character signifies one wild card character
pattern3 = r"gr.y"
print(re.findall(pattern3, "idsgraygreygrrygreagreeyas"))

# ^ string should start with following character
pattern4 = r"^g"

if re.search(pattern4,"gaaassraascfgvhbgy"):
    print ("found pattern4 in search")
else:
    print ("Not found")

# $ string should end with preceding character
pattern5 = r"y$"

if re.search(pattern5,"gaaassraascfgvhbgy"):
    print ("found pattern5 in search")
else:
    print ("Not found")

# []  character set
pattern6 = r"[A-Z][A-Z][0-9]"

#its matching AA9
if re.search(pattern6,"AA5jkm9BN2"):
    print ("found pattern6 in search")
    print(re.findall(pattern6, "AA5jkm9BN2"))
else:
    print ("Not found")

# * meta character
pattern6 = r"g.*y"

print(re.findall(pattern6, "idsgraygreygrrygreagreeyasrthbn"))

