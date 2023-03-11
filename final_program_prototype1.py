import random


def calculate_bmi(weight_kg, height):
    bmi = weight_kg / (height ** 2)
    if bmi < 18.5:
        return f'Your BMI is {bmi:.2f}. You are underweight for your height.'
    elif bmi >= 18.5 and bmi < 25:
        return f'Your BMI is {bmi:.2f}. You are at a healthy weight for your height.'
    elif bmi >= 25 and bmi < 30:
        return f'Your BMI is {bmi:.2f}. You are overweight for your height.'
    else:
        return f'Your BMI is {bmi:.2f}. You are obese for your height.'


while True:
    # Get user input
    weight_kg = float(input('Enter your weight in kilograms: '))
    height = float(input('Enter your height in meters: '))

    # Calculate and display the BMI
    bmi = calculate_bmi(weight_kg, height)
    print(bmi)

    # Ask the user if they want to continue
    response = input('Do you want to continue? (y/n) ')
    if response.lower() == 'n':
        print('Thank you for using the BMI calculator!')
        break

    else:

        # This program calculates BMR and the total calories burned based on the exercises, number of repetitions, and weight used in kilograms
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

        # Get the user's body weight in kilograms
        weight_kg = float(input("Enter your body weight in kilograms: "))

        # Get the intensity of the exercise
        intensity = input(
            "Enter the intensity of the exercise (low, moderate, high): ")

        # Convert the intensity to a multiplier
        if intensity == "low":
            intensity_multiplier = 0.
        elif intensity == "moderate":
            intensity_multiplier = 1
        else:
            intensity_multiplier = 1.5

        # Get the number of exercises the user did
        num_exercises = int(input("Enter the number of exercises you did: "))

        # Loop over the number of exercises
        for i in range(num_exercises):
            # Get the name of the exercise
            while True:
                try:
                    exercise = input(
                        "Enter the name of exercise #" + str(i + 1) + ": ")
                    break
                except:
                    print("Error, try again")

            if exercise == "Plank":
                # Get the time spent doing the plank exercise in minutes
                time = float(
                    input("Enter the time spent doing the plank exercise in minutes: "))

                # Calculate the calories burned for the exercise
                calories = (exercise_calories[exercise]
                            * time) * intensity_multiplier
            else:
                # Get the number of repetitions for the exercise
                repetitions = int(
                    input("Enter the number of repetitions for exercise #" + str(i + 1) + ": "))

                # Get the weight used for the exercise in kilograms (optional)
                weight_used_kg = float(input(
                    "Enter the weight used for exercise #" + str(i + 1) + " in kilograms (optional): "))

            # Calculate the calories burned for the exercise
            if weight_used_kg == 0:
                calories = (exercise_calories[exercise]
                            * repetitions) * intensity_multiplier
            else:
                calories = (
                    exercise_calories[exercise] * repetitions * weight_used_kg) * intensity_multiplier

            # Add the calories burned for the exercise to the total calories burned
            total_calories += calories

        # Print the user's BMR and the total calories burned
        print("Your BMR is", bmr)
        print("You burned a total of", total_calories, "calories.")
        print("The total calories expended per day are",
              bmr+total_calories, "calories")

        # Get the total number of calories expended from the user
        calories = bmr+total_calories

        # Prompt the user for whether they want to do a bulk or cut
        while True:
            try:
                goal = input("Do you want to do a bulk or cut? ")
                break
            except:
                print("Error, try again")

        # Modify the total number of calories based on the user's goal
        if goal.lower() == "bulk":
            calories += 250
        elif goal.lower() == "cut":
            calories -= 450

        # Print the total number of calories and the user's goal
        print("The total number of calories you need are:", calories)
        print("Your goal is to:", goal)

        # Prompt the user for the goal number of calories
        goal_calories = calories

        # Initialize the total number of carbs, proteins, and fats to 0
        total_carbs = 0
        total_proteins = 0
        total_fats = 0

        # Initialize a dictionary with the available foods and their corresponding calories per 100g and classification
        foods = {
            "maize flour": (365, "carbs"),
            "spinach": (23, "carbs"),
            "cabbage": (25, "carbs"),
            "vegetable oil": (884, "fats"),
            "chapati": (155, "carbs"),
            "boiled beans": (127, "carbs"),
            "cooked rice": (130, "carbs"),
            "uncooked rice": (365, "carbs"),
            "goat meat": (122, "proteins"),
            "pork": (291, "proteins"),
            "chicken": (165, "proteins"),
            "eggs": (143, "proteins"),
            "mandazi": (198, "carbs"),
            "milk": (42, "proteins"),
            "white bread": (265, "carbs"),
            "wheat porridge": (103, "carbs"),
            "fermented milk": (64, "proteins"),
            "tilapia": (116, "proteins"),
            "fish meat": (191, "proteins"),
            "oranges": (47, "carbs"),
            "apples": (52, "carbs"),
            "milk(3.25 percent fat)": (61, "proteins"),
            "githeri": (230, "carbs"),
            "pawpaw": (43, "carbs"),
            "tomatoes": (18, "carbs"),
            "onions": (40, "carbs"),
            "sugar": (387, "carbs"),
            "fried groundnuts": (567, "fats"),
            "bananas": (89, "carbs"),
            "maziwa lala": (60, "proteins"),
            "kale": (33, "carbs"),
            "fried chicken": (277, "proteins"),
            "nescafe powder": (455.6, "carbs"),
            "onion samosa": (250, "carbs"),
            "chips": (319, "carbs"),
            "pineapple": (50, "carbs"),
            "goat liver": (236, "proteins"),
            "watermelon": (30, "carbs"),
            "passion fruit": (97, "carbs")
        }

        # Set the minimum and maximum values for each macronutrient
        min_protein = 10
        max_protein = 35
        min_carbohydrates = 45
        max_carbohydrates = 65
        min_fats = 20
        max_fats = 35

        # Generate random values for each macronutrient within the specified range
        protein_percentage = random.randint(min_protein, max_protein)
        carbohydrates_percentage = random.randint(
            min_carbohydrates, max_carbohydrates)
        fats_percentage = random.randint(min_fats, max_fats)

        # Calculate the total percentage
        total_percentage = protein_percentage + \
            carbohydrates_percentage + fats_percentage

        # If the total percentage is not 100, adjust the value of each macronutrient to make it equal 100
        if total_percentage != 100:
            diff = 100 - total_percentage
            # Adjust the value of each macronutrient by an equal amount
            protein_percentage += diff / 3
            carbohydrates_percentage += diff / 3
            fats_percentage += diff / 3

        # Check if any of the values are outside of the recommended range and adjust them accordingly
        if protein_percentage < min_protein:
            diff = min_protein - protein_percentage
            protein_percentage += diff
            carbohydrates_percentage -= diff / 2
            fats_percentage -= diff / 2
        elif protein_percentage > max_protein:
            diff = protein_percentage - max_protein
            protein_percentage -= diff
            carbohydrates_percentage += diff / 2
            fats_percentage += diff / 2

        if carbohydrates_percentage < min_carbohydrates:
            diff = min_carbohydrates - carbohydrates_percentage
            carbohydrates_percentage += diff
            protein_percentage -= diff / 2
            fats_percentage -= diff / 2
        elif carbohydrates_percentage > max_carbohydrates:
            diff = carbohydrates_percentage - max_carbohydrates
            carbohydrates_percentage -= diff
            protein_percentage += diff / 2
            fats_percentage += diff / 2

        if fats_percentage < min_fats:
            diff = min_fats - fats_percentage
            fats_percentage += diff
            protein_percentage -= diff / 2
            carbohydrates_percentage -= diff / 2
        elif fats_percentage > max_fats:
            diff = fats_percentage - max_fats
            fats_percentage -= diff
            protein_percentage += diff / 2
            carbohydrates_percentage += diff / 2

        # Print the final percentage values for each macronutrient
        print("Protein % needed:", protein_percentage)
        print("Carbohydrates % needed:", carbohydrates_percentage)
        print("Fats % needed:", fats_percentage)

        # Calculate the number of calories needed for each macronutrient based on the percentage and caloric goal
        protein_calories = goal_calories * protein_percentage / 100
        carbohydrates_calories = goal_calories * carbohydrates_percentage / 100
        fats_calories = goal_calories * fats_percentage / 100

        # Print the number of calories needed for each macronutrient
        print("Protein:", protein_calories, "calories are needed")
        print("Carbohydrates:", carbohydrates_calories, "calories are needed")
        print("Fats:", fats_calories, "calories are needed")

        # Initialize a list to store the names and amounts of the inputted foods
        food_list = []

        # Prompt the user for the number of foods they want to input
        num_foods = input("Enter the number of foods you want to input: ")

        # Convert the input to an integer
        num_foods = int(num_foods)

        # Prompt the user for the name and amount of each food
        for i in range(num_foods):
            while True:
                try:
                    name = input(f"Enter the name of food #{i+1}: ")
                    amount = input(
                        f"Enter the amount of food #{i+1} in grams: ")
                    break
                except:
                    print("Error, try again")

            # Convert the amount to an integer
            amount = int(amount)
            # Get the calories and classification of the food from the dictionary
            calories, classification = foods[name.lower()]

            # Calculate the number of calories from the food
            food_calories = calories * amount / 100

            # Add the food's calories to the total number of carbs, proteins, or fats
            if classification == "carbs":
                total_carbs += food_calories
            elif classification == "proteins":
                total_proteins += food_calories
            elif classification == "fats":
                total_fats += food_calories

            # Add the name and amount of the food to the list
            food_list.append((name, amount))

        # Recommending calories for adjustent
        if total_carbs != carbohydrates_calories:
            adjusted_carbs = carbohydrates_calories-total_carbs
            print(f"Adjust carbohydrate calories to:{adjusted_carbs}")

        if total_proteins != protein_calories:
            adjusted_proteins = protein_calories-total_proteins
            print(f"Adjust protein calories to:{adjusted_proteins}")

        if total_fats != fats_calories:
            adjusted_fats = fats_calories-total_fats
            print(f"Adjust fat calories to:{adjusted_fats}")
