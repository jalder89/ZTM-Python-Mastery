username = input("What is your username? ")
password = input("What is your password? ")

password_length = len(password)
hidden_password = "*" * len(password)

print(f"Your username is {username} and your password {hidden_password} is {password_length} letters long.")