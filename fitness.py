from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Enter your gender (M/F) ").lower
    birth_str = input("Enter your birthday (YYYY-MM-DD) ")
    pounds = float(input("Enter your weight in pounds  "))
    inches = float(input("Enter your height in inches "))

    age = compute_age(birth_str)
    weight = kg_from_lb(pounds)
    height = cm_from_in(inches)
    bmi = body_mass_index(weight, height)
    bmr = basal_metabolic_rate(gender, weight, height, age)
    # Print the results for the user to see.
    years = age 
    print(f"Age (years): {years} ")
    print(f"Weight (kg): {weight:.2f}")
    print(f"Height (cm): {height:.2f} ")
    print(f"Body mass index: {bmi:.1f} ")
    print(f"Basal metabolic rate (kcal/day): {bmr:.0f} ")
    pass


def compute_age(birth_str):
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    age = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        age -= 1

    return age


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    weight = pounds * 0.45359237 

    return weight


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    height = inches * 2.54
    
    return height


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = (10000 * weight) / (height**2)

    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender == "f":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else: bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)


    return bmr

main()
# Call the main function so that
# this program will start executing