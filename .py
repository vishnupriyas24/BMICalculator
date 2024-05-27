def calculate_bmi(weight, height):
    """Calculate BMI using the formula: weight (kg) / (height (m) ^ 2)"""
    bmi = weight / (height ** 2)
    return bmi
def classify_bmi(bmi):
    """Classify BMI into categories"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
def main():
    print("Welcome to the BMI Calculator")
    try:
        weight = float(input("Please enter your weight in kilograms: "))
        height = float(input("Please enter your height in meters: "))
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        print(f"Your BMI is: {bmi:.2f}")
        print(f"According to your BMI, you are: {category}")
    except ValueError:
        print("Please enter valid numerical values for weight and height.")
if __name__ == "__main__":
    main()
