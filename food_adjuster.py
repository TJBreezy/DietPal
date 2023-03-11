foods = {
        "maize flour": (365, "carbs"),
        "spinach": (23, "carbs"),
        "cabbage": (25, "carbs"),
        "vegetable oil": (884, "fats"),
        "chapati": (155, "carbs"),
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
        "fried chicken": (277, "protein"), 
        "nescafe powder": (455.6, "carbs"),
        "onion samosa": (250, "carbs"),
        "chips": (319, "carbs"),
        "boiled beans": (127, "proteins"),
        "chicken liver": (116, "protein"),
        "chicken gizzards": (94, "protein")
}

# Continuously prompt the user to enter a food and number of calories until they enter "done"
total_calories = 0
carbs = 0
fats = 0
proteins = 0

while True:
    food = input("Enter a food (or 'done' to exit): ")
    if food.lower() == "done":
        break
    if food in foods:
        calories, macronutrient = foods[food]
        calories_consumed = float(input("Enter number of calories consumed: "))
        total_calories += calories_consumed
        if macronutrient == "carbs":
            carbs += calories_consumed
        elif macronutrient == "fats":
            fats += calories_consumed
        elif macronutrient == "proteins":
            proteins += calories_consumed
    else:
        print(f"{food} is not in the dictionary. Please try again.")
#input factors
carb_x=input("Input carb factor:")
protein_x = input("Input protein factor:")
fat_x = input("Input fat factor:")
# Calculate the number of grams of each macronutrient
try:
    carbs_grams = carbs / (float(carb_x)/100)
except (ZeroDivisionError, ValueError):
    carbs_grams = 0
try:
    fats_grams = fats / (float(fat_x)/100)
except (ZeroDivisionError, ValueError):
    fats_grams = 0
try:
    proteins_grams = proteins / (float(protein_x)/100)
except (ZeroDivisionError, ValueError):
    proteins_grams = 0


print(f"Total calories: {total_calories}")
print(f"Carbohydrates: {carbs} calories ({carbs_grams:.2f} grams)")
print(f"Fats: {fats} calories ({fats_grams:.2f} grams)")
print(f"Proteins: {proteins} calories ({proteins_grams:.2f} grams)")
