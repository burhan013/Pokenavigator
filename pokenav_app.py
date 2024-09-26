
def bmi_calc(height, weight):
    return weight / (height**2)

def bmi_check(height, weight):
    if height <= 0 and weight <= 0:
        return "Error - Height and weight must be positive numbers."
    elif weight <= 0:
        return "Error - Weight must be a positive number."
    elif height <= 0:
        return "Error - Height must be a positive number."
    else:
        return None

def categorize_bmi(bmi):
    if bmi < 29:
        return f"BMI = {bmi:.2f}. The Pokemon is underweight."
    elif bmi < 53:
        return f"BMI = {bmi:.2f}. The Pokemon is healthy."
    elif bmi < 85:
        return f"BMI = {bmi:.2f}. The Pokemon is overweight."
    else:
        return f"BMI = {bmi:.2f}. The Pokemon is obese."

def bmi_print():
    try:
        input_height = float(input("Input height in meters"))
        input_weight = float(input("Input weight in kilograms"))

        if input_height <= 0 or input_weight <= 0:
            print("Error - Height and weight must be positive numbers.")
            return

        bmi = bmi_calc(input_height, input_weight)
        result = categorize_bmi(bmi)
        print(result)

    except ValueError:
        print("Error - Please enter valid numbers for height and weight. ")

def grab_hashtag():
    sentence = input("Type your post: ") 
    hashtags = {word for word in sentence.split() if word.startswith("#")}
    
    if hashtags:
        print("\nHashtags found:\n" + "\n".join(hashtags))
    else:
        print("\nNo hashtags found.\n")

def is_palindrome(word):
    cleaned_word = word.lower()
    return cleaned_word == cleaned_word[::-1]

def get_palindrome():
    pokemon = input("Type your Pokemon name:  ")

    if is_palindrome(pokemon):
        print (f"\nThe name '{pokemon}' is a palindrome.\n")
    else:
        print(f"\nThe name '{pokemon}' is not a palindrome.\n")
    
def fitness_tracker():

    steps_input = input("Step count per day: ").strip()

    if steps_input == "":
        num = 0
        print(f"Error - Invalid input. The program needs 7 numbers; you typed {num} numbers.")
        return
    else:
        steps_strings = steps_input.split(",")
        num = len(steps_strings)
    
    
    if len(steps_strings) != 7:
        print(f"Error - Invalid input. The program needs 7 numbers; you typed {num} numbers.")
        return


    steps = []
    for s in steps_strings:
        steps.append(int(s.strip()))


    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    max_steps = max(steps)
    min_steps = min(steps)

    mean_steps = sum(steps)/len(steps)

    squared_difference = sum((x - mean_steps) ** 2 for x in steps)
    variance = squared_difference / len(steps)
    deviation = variance**0.5


    for i in range (len(steps)):
        if steps[i] == max_steps:
            most_active_day = weekdays[i]

    for i in range (len(steps)):
        if steps[i] == min_steps:
            least_active_day = weekdays[i]

    rounded_deviation = round(deviation, 2)
    rounded_mean = round(mean_steps, 2)

    print(f"\nSteps Statistics: {rounded_mean:.2f} + / - {rounded_deviation:.2f} per day.")
    print(f"Most active day: {most_active_day}. Least active day: {least_active_day}.\n")

def create_acronym():
    pokemon_name = input("Type your Pokemon name: ")

    shortening_factor = int(input("Type your shortening factor: "))

    acronym = "" 

    
    for i in range(shortening_factor - 1, len(pokemon_name), shortening_factor):
        acronym += pokemon_name[i] 

    print(f"\nAbbreviated name: {acronym.upper()}\n")

def get_pokemon_traits():
    pokemon_name = input("Type your Pokemon name: ").capitalize()
    pokemon_type = input("Type your Pokemon type (Water, Fire, Grass): ").capitalize()

    if pokemon_type == "Fire":
        print(f"\n{pokemon_name} is a Fire-type Pokemon! It is strong against Grass-type Pokemons and weak against Water-type Pokemons.\n")
    elif pokemon_type == "Water":
        print(f"\n{pokemon_name} is a Water-type Pokemon! It is strong against Fire-type Pokemons and weak against Grass-type Pokemons.\n")
    elif pokemon_type == "Grass":
        print(f"\n{pokemon_name} is a Grass-type Pokemon! It is strong against Water-type Pokemons and weak against Fire-type Pokemons.\n")
    else:
        print("\nError - The Pokemon type provided is not valid. Valid types: Water, Fire, Grass.\n") 

def match_zodiac_sign():
    zodiac_signs = ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini",
                    "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"]

    elements = ["Earth", "Air", "Water", "Fire", "Earth", "Air",
                "Water", "Fire", "Earth", "Air", "Water", "Fire"]

    eeveelutions = ["Leafeon", "Jolteon", "Vaporeon", "Flareon", "Leafeon", "Jolteon",
                        "Vaporeon", "Flareon", "Leafeon", "Jolteon", "Vaporeon", "Flareon"]


    user_month = int(input("Enter your birth month (a number between 1-12): "))
    if 1 <= user_month <= 12:   
        index = user_month - 1  

        zodiac_sign = zodiac_signs[index]
        element = elements[index]
        eeveelution = eeveelutions[index]

        print(f"\nZodiac sign: {zodiac_sign}")
        print(f"Element: {element}")
        print(f"Eeveelution: {eeveelution}\n")
    else:
        print("\nError - The month index provided is not valid. Choose between 1 and 12.\n")

def menu_input():
    input1 = int(input("Type your option: "))
    while input1 not in range(1,9):
        print("Error - Invalid option. Please input a number between 1 and 8.")
        input1= int(input())
    else:
        return input1

def main():
    menu_state = 0
    menu_msg = f"""\nWelcome to the Main Menu. Choose one of the options below:

    1. Exit
    2. Identify hashtags
    3. Detect a palindrome
    4. Create an acronym
    5. Get Pokemon traits
    6. Match zodiac sign and element
    7. BMI calculator
    8. Fitness and health tracker

    """
    end_msg = f"""Thank you for playing! See you next time!"""

    while menu_state != 1:
        print(menu_msg)
        menu_state = menu_input()
        match menu_state:
            case 1:
                print(end_msg)
                continue
            case 2:
                grab_hashtag()
            case 3:
                get_palindrome()
            case 4:
                print
                create_acronym()
            case 5:
                print
                get_pokemon_traits()
            case 6:
                print
                match_zodiac_sign()
            case 7:
                bmi_print()
            case 8:
                fitness_tracker()

if __name__ == "__main__":
    main()
