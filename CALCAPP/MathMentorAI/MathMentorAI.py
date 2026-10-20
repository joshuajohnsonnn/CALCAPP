## THIS IS NOT WORKING UP TO STANDARD. WORKING ON IT. PLEASE BE PATIENT. ##
## THANK YOU FOR YOUR UNDERSTANDING. ##

import math

def math_mentor_ai():
    print("\nHello! I am Math Mentor AI, your personal assistant for CALCAPP.")
    print("I can help you understand the available calculations and guide you through using this app.")
    print("Here are some things I can do for you:")
    print("1. Explain what each calculation does.")
    print("2. Provide examples of inputs for calculations.")
    print("3. Help you choose the right calculation for your needs.")
    print("4. Answer general math-related questions.")

    while True:
        print("\nWhat would you like help with?")
        print("1. Explain a calculation")
        print("2. Show an example input")
        print("3. Exit Math Mentor AI")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            calc = input("Which calculation would you like me to explain? ").lower()
            explain_calculation(calc)
        elif choice == '2':
            calc = input("Which calculation would you like an example for? ").lower()
            example_input(calc)
        elif choice == '3':
            print("Goodbye! If you need help again, just call me.")
            break
        else:
            print("Invalid choice. Please try again.")

def explain_calculation(calc):
    explanations = {
        "addition": "Adds two numbers together.",
        "subtraction": "Subtracts the second number from the first.",
        "multiplication": "Multiplies two numbers together.",
        "division": "Divides the first number by the second.",
        "modulus": "Finds the remainder when the first number is divided by the second.",
        "floor division": "Performs division and rounds down to the nearest whole number.",
        "square root": "Finds the square root of a number.",
        "power": "Raises a number to the power of another number.",
        "logarithm": "Finds the logarithm of a number to a specified base.",
        "sine": "Finds the sine of an angle (in degrees).",
        "cosine": "Finds the cosine of an angle (in degrees).",
        "tangent": "Finds the tangent of an angle (in degrees).",
        "mean": "Calculates the average of a list of numbers.",
        "mode": "Finds the most frequently occurring number(s) in a list.",
        "median": "Finds the middle value in a sorted list of numbers.",
        "range": "Calculates the difference between the largest and smallest numbers in a list.",
        "hyperbolic sine": "Finds the hyperbolic sine of an angle (in degrees).",
        "hyperbolic cosine": "Finds the hyperbolic cosine of an angle (in degrees).",
        "hyperbolic tangent": "Finds the hyperbolic tangent of an angle (in degrees).",
        "hyperbolic arcsine": "Finds the inverse hyperbolic sine of a number.",
        "hyperbolic arccosine": "Finds the inverse hyperbolic cosine of a number.",
        "hyperbolic arctangent": "Finds the inverse hyperbolic tangent of a number.",
        "radian conversion": "Converts an angle from degrees to radians.",
        "degree conversion": "Converts an angle from radians to degrees."
    }
    if calc in explanations:
        print(f"{calc.capitalize()}: {explanations[calc]}")
    else:
        print("Sorry, I don't have an explanation for that calculation.")

def example_input(calc):
    examples = {
        "addition": "Example: 5 + 3 = 8",
        "subtraction": "Example: 10 - 4 = 6",
        "multiplication": "Example: 7 * 2 = 14",
        "division": "Example: 20 / 4 = 5",
        "modulus": "Example: 10 % 3 = 1",
        "floor division": "Example: 10 // 3 = 3",
        "square root": "Example: √16 = 4",
        "power": "Example: 2^3 = 8",
        "logarithm": "Example: log(100, 10) = 2",
        "sine": "Example: sin(30°) = 0.5",
        "cosine": "Example: cos(60°) = 0.5",
        "tangent": "Example: tan(45°) = 1",
        "mean": "Example: Mean of [1, 2, 3] = 2",
        "mode": "Example: Mode of [1, 2, 2, 3] = 2",
        "median": "Example: Median of [1, 3, 2] = 2",
        "range": "Example: Range of [1, 3, 2] = 2 (3 - 1)",
        "hyperbolic sine": "Example: sinh(30°) = 0.547",
        "hyperbolic cosine": "Example: cosh(30°) = 1.140",
        "hyperbolic tangent": "Example: tanh(30°) = 0.462",
        "hyperbolic arcsine": "Example: arcsinh(1) = 0.881",
        "hyperbolic arccosine": "Example: arccosh(2) = 1.317",
        "hyperbolic arctangent": "Example: arctanh(0.5) = 0.549",
        "radian conversion": "Example: 180° = π radians",
        "degree conversion": "Example: π radians = 180°"
    }
    if calc in examples:
        print(f"{calc.capitalize()} Example: {examples[calc]}")
    else:
        print("Sorry, I don't have an example for that calculation.")
    
math_mentor_ai()