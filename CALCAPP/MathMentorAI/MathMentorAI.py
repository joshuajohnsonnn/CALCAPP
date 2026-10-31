## THIS IS NOT WORKING UP TO STANDARD. WORKING ON IT. PLEASE BE PATIENT. ##
## THANK YOU FOR YOUR UNDERSTANDING. ##

import math
from time import sleep

CALCULATION_ALIASES = {
    "add": "addition",
    "subtract": "subtraction",
    "multiply": "multiplication",
    "divide": "division",
    "mod": "modulus",
    "squareroot": "square root",
    "sqrt": "square root",
    "exponentiation": "power",
    "pow": "power",
    "log": "logarithm",
    "sin": "sine",
    "cos": "cosine",
    "tan": "tangent",
    "average": "mean",
    "avg": "mean",
    "most frequent": "mode",
    "middle value": "median",
    "difference between largest and smallest": "range",
    "floor div": "floor division",
    "floor divide": "floor division",
    "sinh": "hyperbolic sine",
    "cosh": "hyperbolic cosine",
    "tanh": "hyperbolic tangent",
    "arcsinh": "hyperbolic arcsine",
    "arccosh": "hyperbolic arccosine",
    "arctanh": "hyperbolic arctangent",
}

CALCAPP_FUNCTIONS = (
    "addition",
    "subtraction",
    "multiplication",
    "division",
    "modulus",
    "floor division",
    "square root",
    "power",
    "logarithm",
    "sine",
    "cosine",
    "tangent",
    "mean",
    "mode",
    "median",
    "range",
    "hyperbolic sine",
    "hyperbolic cosine",
    "hyperbolic tangent",
    "hyperbolic arcsine",
    "hyperbolic arccosine",
    "hyperbolic arctangent",
    "radian conversion",
    "degree conversion",
)


def normalize_calculation(calc):
    normalized = " ".join(calc.strip().lower().split())
    return CALCULATION_ALIASES.get(normalized, normalized)


def show_all_functions():
    print("\nCALCAPP can perform these calculations:")
    for function in CALCAPP_FUNCTIONS:
        print(f"- {function.capitalize()}")


def math_mentor_ai():
    print("\nHello! I am Math Mentor AI, your personal assistant for CALCAPP.")
    print("I can help you understand the available calculations and guide you through using this app.")
    print("You can show all calculator functions, get an explanation, or see an example input.")

    while True:
        print("\nWhat would you like help with?")
        print("1. Show all Functions of the calculator")
        print("--------------------------------")
        print("2. Explain a calculation")
        print("--------------------------------")
        print("3. Show an example input")
        print("--------------------------------")
        print("4. Exit Math Mentor AI")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            show_all_functions()
            sleep(3.5)  # Pause for a moment to let the user read the list
        elif choice == '2':
            calc = input("Which calculation would you like me to explain? ").lower()
            explain_calculation(calc)
            sleep(5)
        elif choice == '3':
            calc = input("Which calculation would you like an example for? ").lower()
            example_input(calc)
            sleep(5) 
        elif choice == '4':
            print("Goodbye! If you need help again, just call me.")
            break
        else:
            print("Invalid choice. Please try again.")

def explain_calculation(calc):
    calc = normalize_calculation(calc)
    import CALCAPP.MathMentorAI.MMAIexplanation as mmaiexplanation
    explanations = mmaiexplanation.explanations
    if calc in explanations:
        print(f"{calc.capitalize()}: {explanations[calc]}")
    else:
        print("Sorry, I don't have an explanation for that calculation.")


def example_input(calc):
    calc = normalize_calculation(calc)
    import CALCAPP.MathMentorAI.MMAIexamples as mmaiexamples
    examples = mmaiexamples.examples
    if calc in examples:
        print(f"{calc.capitalize()} Example: {examples[calc]}")
    else:
        print("Sorry, I don't have an example for that calculation.")
    
math_mentor_ai()