# This program calculates BMR using the most accurate formula and the metric system

# Get the user's weight in kilograms
weight_kg = float(input("Enter your weight in kilograms: "))

# Get the user's height in centimeters
height_cm = float(input("Enter your height in centimeters: "))

# Get the user's age in years
age_years = float(input("Enter your age in years: "))

# Calculate the user's BMR using the most accurate formula and the metric system
bmr = 66 + (13.7 * weight_kg) + (5 * height_cm) - (6.8 * age_years)

# Print the user's BMR
print("Your BMR is", bmr)
