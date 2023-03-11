def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
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
    weight = float(input('Enter your weight in kilograms: '))
    height = float(input('Enter your height in meters: '))

    # Calculate and display the BMI
    bmi = calculate_bmi(weight, height)
    print(bmi)

    # Ask the user if they want to continue
    response = input('Do you want to continue? (y/n) ')
    if response.lower() == 'n':
        break

print('Thank you for using the BMI calculator!')
