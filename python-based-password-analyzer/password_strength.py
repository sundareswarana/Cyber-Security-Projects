import re
print("Password Strength Checker")
pwd = input("Enter Password: ")
s= 0
if len(pwd) >= 8:
    s+= 1
if re.search("[A-Z]", pwd):
    s+= 1
if re.search("[a-z]", pwd):
    s+= 1
if re.search("[0-9]", pwd):
    s+= 1
if re.search("[@#$%^&*!]", pwd):
    s+= 1
print("\nPassword Analysis Result:")
if s <= 2:
    print("Password Strength: WEAK")
elif s<= 4:
    print("Password Strength: MEDIUM")
else:
    print("Password Strength: STRONG")
if s < 5:
    print("Suggestions to improve password:")
    if len(pwd) < 8:
        print("- Use at least 8 characters")
    if not re.search("[A-Z]", pwd):
        print("- Add uppercase letters")
    if not re.search("[a-z]", pwd):
        print("- Add lowercase letters")
    if not re.search("[0-9]", pwd):
        print("- Include numbers")
    if not re.search("[@#$%^&*!]", pwd):
        print("- Add special characters")