# Function to calculate the calories burned during jumping rope
def calculate_calories_burned(weight, age, time):
    MET = 10.0  # Metabolic equivalent of task for jumping rope
    calories_burned = ((MET * weight * 3.5) / 200) * time
    return calories_burned

# Function to calculate the time required to burn the intended calories


def calculate_time_to_burn_calories(weight, age, intended_calories):
    # Initial time estimate of 30 minutes
    time = 30
    # Calculate calories burned for 30 minutes
    calories_burned = calculate_calories_burned(weight, age, time)
    # Loop until calories burned is greater than or equal to intended calories
    while calories_burned < intended_calories:
        # Increase time by 5 minutes for each iteration
        time += 5
        calories_burned = calculate_calories_burned(weight, age, time)
    return time


# Get input from user and handle errors
try:
    weight = float(input("Enter your weight in kg: "))
    age = int(input("Enter your age: "))
    intended_calories = float(
        input("Enter the number of calories you intend to burn: "))
    # Calculate time required to burn intended calories
    time_required = calculate_time_to_burn_calories(
        weight, age, intended_calories)
    print("To burn", intended_calories,
          "calories by jumping rope, you need to workout for", time_required, "minutes.")
except ValueError:
    print("Invalid input. Please enter valid values for weight, age, and intended calories as numbers.")
