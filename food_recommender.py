# Prompt the user for the goal number of calories
import random
goal_calories = input("Enter the goal number of calories: ")

# Convert the input to an integer
goal_calories = int(goal_calories)

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
    "fried groundnuts": (567, "fats"),
    "bananas": (89, "carbs"),
    "maziwa lala": (60, "proteins"),
    "kale": (33, "carbs"),
    "fried chicken": (277, "proteins"),
    "nescafe powder": (455.6, "carbs"),
    "onion samosa": (250, "carbs"),
    "chips": (319, "carbs"),
    "peanuts": (597, "fats"),
    "sugar": (387, "carbs"),
    "pineapple": (50, "carbs"),
    "goat liver": (236, "proteins"),
    "watermelon": (30, "carbs"),
    "passion fruit": (97, "carbs"),
    "farmer's smokies": (220, "proteins"),
    "quencher": (52, "carbs"),
    "grapes": (67, "carbs"),
    "apple": (52, "carbs"),
    "beetroot": (44, "carbs"),
    "mango": (60, "carbs"),
    "yoghurt": (108, "proteins"),
    "mirinda": (38, "carbs"),
    "soft scones": (354, "carbs")

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
carbohydrates_percentage = random.randint(min_carbohydrates, max_carbohydrates)
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
print("Protein:", protein_percentage)
print("Carbohydrates:", carbohydrates_percentage)
print("Fats:", fats_percentage)

# Calculate the number of calories needed for each macronutrient based on the percentage and caloric goal
protein_calories = goal_calories * protein_percentage / 100
carbohydrates_calories = goal_calories * carbohydrates_percentage / 100
fats_calories = goal_calories * fats_percentage / 100

# Print the number of calories needed for each macronutrient
print("Protein:", protein_calories, "calories")
print("Carbohydrates:", carbohydrates_calories, "calories")
print("Fats:", fats_calories, "calories")

# Initialize a list to store the names and amounts of the inputted foods
food_list = []

# Prompt the user for the number of foods they want to input
num_foods = input("Enter the number of foods you want to input: ")

# Convert the input to an integer
num_foods = int(num_foods)

# Prompt the user for the name and amount of each food
for i in range(num_foods):
    name = input(f"Enter the name of food #{i+1}: ")
    amount = input(f"Enter the amount of food #{i+1} in grams: ")

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
        adjusted_carbs = total_carbs-carbohydrates_calories
        print(f"Adjust carbohydrate calories by:{adjusted_carbs}")

    if total_proteins != protein_calories:
        adjusted_proteins = total_proteins-protein_calories
        print(f"Adjust protein calories by:{adjusted_proteins}")

    if total_fats != fats_calories:
        adjusted_fats = total_fats-fats_calories
        print(f"Adjust fat calories by:{adjusted_fats}")
