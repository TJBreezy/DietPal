# Constants for calorie calculation
MET_WALKING = 3.5
MET_JOBBING = 7.0
MET_RUNNING = 10.0
CAL_PER_KG_PER_HOUR = 7.2  # calories burned per kg body weight per hour of activity

# Prompt user for inputs
while True:
    try:
        distance = float(input("Enter the distance traveled in meters: "))
        break
    except ValueError:
        print("Invalid distance. Please enter a number.")

while True:
    try:
        time_minutes = float(input("Enter the total time taken in minutes: "))
        break
    except ValueError:
        print("Invalid time. Please enter a number.")

while True:
    try:
        weight = float(input("Enter your body weight in kg: "))
        break
    except ValueError:
        print("Invalid weight. Please enter a number.")

while True:
    try:
        speed = distance / time_minutes
        break
    except ZeroDivisionError:
        print("Invalid time. Time must be greater than zero.")

age = int(input("Enter your age in years: "))
gender = input("Enter your gender (male/female): ")

# Categorize activity based on speed
if speed < 1.4:
    activity = "Walking"
    MET = MET_WALKING
elif speed < 2.5:
    activity = "Jogging"
    MET = MET_JOBBING
else:
    activity = "Running"
    MET = MET_RUNNING

# Calculate calories burned
if gender.lower() == "male":
    BMR = 88.362 + (13.397 * weight) + (4.799 * time_minutes) - (5.677 * age)
else:
    BMR = 447.593 + (9.247 * weight) + (3.098 * time_minutes) - (4.330 * age)

calories_burned = ((MET * BMR) / (24 * 60)) * weight * (time_minutes / 60)

# Output result
print(
    f"You burned {calories_burned:.2f} calories during {activity} at {speed:.2f} m/min.")