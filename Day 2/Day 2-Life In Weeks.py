age = input("What is your current age? ")
years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.") # You can write it this way or;





age = input("What is your current age? ")
days = (365 * int(age))
days_1 = (32850 - days)

weeks = (52 * int(age))
weeks_1 = (4680 - weeks)

months = (12 * int(age))
months_1 = (1080 - months)
print(f"you have {days_1} days , {weeks_1} weeks, and {months_1} months left " ) # This way or;



age = input("What is your current age? ")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
message = f"you have {days_1} days , {weeks_1} weeks, and {months_1} months left " # This way
print(message)