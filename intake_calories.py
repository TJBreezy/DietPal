def main():
    # Get the total number of calories expended from the user
    calories = input("Enter the total number of calories expended in a day: ")

    # Convert the input to an integer
    calories = int(calories)

    # Prompt the user for whether they want to do a bulk or cut
    goal = input("Do you want to do a bulk or cut? ")

    # Modify the total number of calories based on the user's goal
    if goal.lower() == "bulk":
        calories += 250
    elif goal.lower() == "cut":
        calories -= 500

    # Print the total number of calories and the user's goal
    print("The total number of calories expended is:", calories)
    print("Your goal is to:", goal)


if __name__ == "__main__":
    main()
