match_found = False

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(char)
        match_found = True
if not match_found:
    print("No match was found")