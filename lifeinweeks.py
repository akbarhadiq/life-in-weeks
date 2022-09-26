print("Your remaining live in weeks, if you live to 90 years.")

# on the assumption that you live to 90 years, here's how much time u got
years = 90
weeks = 90*52
days = 365*90
age = int(input("What is your current age?: \n"))
#

years_left = years - age
weeks_left = weeks - (age*52)
days_left = days - (age*365)

print(f"You have {years_left} years, {weeks_left} weeks, and {days_left} days left to live")
