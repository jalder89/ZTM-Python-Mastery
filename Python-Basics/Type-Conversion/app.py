import datetime

# Get current year from today's date
today = datetime.date.today()
current_year = int(today.strftime("%Y"))

# Get the users birth year
birth_year = input("What year were you born? ")

# Calculate the user's age
age = current_year - int(birth_year)

# Print the birthyear and age
print(f"You were born in {birth_year}")
print(f"Your age is {age}")