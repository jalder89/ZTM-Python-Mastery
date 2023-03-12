is_magician = True
is_expert = True

# Check if magician and expert: "You are a master magician"
if is_magician and is_expert:
    print("You are a master magician!")

# Check if magician and not expert: "at least you're getting there"
if is_magician and not is_expert:
    print("...at least you're getting there!")

# If you're not a magician: "You need magic powers"
if not is_magician:
    print("You need magic powers...")

# Ternary Operator
print("You are a master magician!") if is_magician and is_expert else print("...at least you're getting there!") if is_magician and not is_expert else print("You need magic powers...")