# Password checker exercise for RegEx practice
import re

padding = "                "
print(f"\n\n{padding}===Password Checker===")
print("Passwords must be at least 8 characters and end in a number.")
print("Passwords can contain these characters: a-Z, 0-9, $%#@!")

while True:
    password = input("\nPlease input a password: ")
    pattern = re.compile(r"(^[a-zA-z0-9$%#@!]{7,}\d)$")

    if bool(re.search(pattern, password)):
        print("Password accepted!")
        break
    else:
        print("Password does not meet the requirements...\n")
        continue