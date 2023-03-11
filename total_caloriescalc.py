# This program calculates BMR and the total calories burned based on the exercises, number of repetitions, and weight used in kilograms
# Get the user's weight in kilograms
weight_kg = float(input("Enter your weight in kilograms: "))

# Get the user's height in centimeters
height_cm = float(input("Enter your height in centimeters: "))

# Get the user's age in years
age_years = float(input("Enter your age in years: "))

# Calculate the user's BMR using the most accurate formula and the metric system
bmr = 66 + (13.7 * weight_kg) + (5 * height_cm) - (6.8 * age_years)

# Dictionary containing the calories burned per minute for each exercise
exercise_calories = {
    "Squats": 0.085,
    "Bench press": 0.055,
    "Bent-over rows": 0.085,
    "Military press": 0.055,
    "Bicep curls": 0.025,
    "Push-ups": 0.025,
    "Lunges": 0.085,
    "Plank": 0.025,
    "Burpees": 0.2,
    "Deadlifts": 0.135,
    "Pull-ups": 0.05,
    "Tricep extensions": 0.025,
    "Crunches": 0.015,
    "Jumping jacks": 0.12
}

# Initialize total calories burned to 0
total_calories = 0

# Get the number of exercises the user did
num_exercises = int(input("Enter the number of exercises you did: "))

# Loop over the number of exercises
for i in range(num_exercises):
    # Get the name of the exercise
    exercise = input("Enter the name of exercise #" + str(i + 1) + ": ")

    if exercise == "Plank":
        # Get the time spent doing the plank exercise in minutes
        time = float(
            input("Enter the time spent doing the plank exercise in minutes: "))

        # Calculate the calories burned for the exercise
        calories = exercise_calories[exercise] * time
    else:
        # Get the number of repetitions for the exercise
        repetitions = int(
            input("Enter the number of repetitions for exercise #" + str(i + 1) + ": "))

        # Get the weight used for the exercise in kilograms
        weight_kg = float(
            input("Enter the weight used for exercise #" + str(i + 1) + " in kilograms: "))

        # Calculate the calories burned for the exercise
        calories = exercise_calories[exercise] * repetitions * weight_kg

    # Add the calories burned for the exercise to the total calories burned
    total_calories += calories

# Print the user's BMR and the total calories burned
print("Your BMR is", bmr)
print("You burned a total of", total_calories, "calories.")
print("The total calories expended per day are", bmr+total_calories, "calories")
