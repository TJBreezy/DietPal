# This program calculates the total calories burned based on the exercises and number of repetitions

# Dictionary containing the calories burned per repetition for each exercise
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

    # Get the number of repetitions for the exercise
    repetitions = int(
        input("Enter the number of repetitions for exercise #" + str(i + 1) + ": "))

    # Calculate the calories burned for the exercise
    calories = exercise_calories[exercise] * repetitions

    # Add the calories burned for the exercise to the total calories burned
    total_calories += calories

# Print the total calories burned
print("You burned a total of", total_calories, "calories.")
