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
    explanations = {
        "addition": "Addition combines numbers to find their total. Add each value to the running sum; the order does not change the result.",
        "subtraction": "Subtraction finds the difference between numbers. The second number is taken away from the first, so changing their order can change the result.",
        "multiplication": "Multiplication finds the total of equal-sized groups. For whole numbers, multiply one value by the other; for example, 4 * 3 means three groups of four.",
        "division": "Division splits a value into equal groups or asks how many times one value fits into another. The first value is the dividend and the second is the divisor; division by zero is undefined.",
        "modulus": "Modulus returns the remainder left after dividing one number by another. For whole numbers, it tells you what is left after taking out as many complete groups of the divisor as possible.",
        "floor division": "Floor division divides the first number by the second and rounds the quotient down to the greatest integer less than or equal to it. With negative values, rounding down goes toward negative infinity.",
        "square root": "A square root is a value that, when multiplied by itself, gives the original number. For example, the principal square root of 25 is 5. In real numbers, square roots are defined for non-negative inputs.",
        "power": "A power repeatedly multiplies a base by itself according to an exponent. For a positive whole-number exponent, 2^3 means 2 * 2 * 2. A zero or negative exponent follows additional rules.",
        "logarithm": "A logarithm answers the question: what exponent on a chosen base gives this number? For example, log base 10 of 100 is 2 because 10^2 = 100. The input and base must be positive, and the base cannot be 1.",
        "sine": "Sine gives the ratio opposite side / hypotenuse for an angle in a right triangle. It is also a periodic function defined for any angle; check whether the calculator expects degrees or radians.",
        "cosine": "Cosine gives the ratio adjacent side / hypotenuse for an angle in a right triangle. It is also a periodic function defined for any angle; check whether the calculator expects degrees or radians.",
        "tangent": "Tangent gives the ratio opposite side / adjacent side for an angle in a right triangle, and equals sine divided by cosine. It is undefined at angles where cosine is zero; check whether the calculator expects degrees or radians.",
        "mean": "The mean, or arithmetic average, is found by adding all values and dividing by how many values there are. Every value contributes to the result, so unusually large or small values can affect it.",
        "mode": "The mode is the value or values that occur most often in a collection. A collection can have one mode, multiple tied modes, or no mode if every value occurs equally often.",
        "median": "The median is the middle value after sorting the data. With an odd number of values it is the center value; with an even number, it is the average of the two center values.",
        "range": "The range measures the spread from the smallest to the largest value. Subtract the minimum from the maximum; the result can be affected strongly by outliers.",
        "hyperbolic sine": "The hyperbolic sine, sinh(x), is (e^x - e^(-x)) / 2. It is an increasing function related to the ordinary sine function; its input is conventionally a real number in radians.",
        "hyperbolic cosine": "The hyperbolic cosine, cosh(x), is (e^x + e^(-x)) / 2. It is always at least 1 for real inputs and is symmetric around zero; its input is conventionally a real number in radians.",
        "hyperbolic tangent": "The hyperbolic tangent, tanh(x), is sinh(x) / cosh(x). For real inputs its values lie between -1 and 1; its input is conventionally a real number in radians.",
        "hyperbolic arcsine": "The inverse hyperbolic sine, asinh(x), returns the real value whose hyperbolic sine is x. It is defined for every real input and returns its result in radians.",
        "hyperbolic arccosine": "The inverse hyperbolic cosine, acosh(x), returns the non-negative value whose hyperbolic cosine is x. For real results, the input must be at least 1; the result is in radians.",
        "hyperbolic arctangent": "The inverse hyperbolic tangent, atanh(x), returns the value whose hyperbolic tangent is x. For real results, the input must be strictly between -1 and 1; the result is in radians.",
        "radian conversion": "Radians measure angles using the radius of a circle: one full turn is 2π radians. Convert degrees to radians by multiplying the degree value by π / 180.",
        "degree conversion": "Degrees divide a full turn into 360 parts. Convert radians to degrees by multiplying the radian value by 180 / π."
    }
    if calc in explanations:
        print(f"{calc.capitalize()}: {explanations[calc]}")
    else:
        print("Sorry, I don't have an explanation for that calculation.")


def example_input(calc):
    calc = normalize_calculation(calc)
    examples = {
        "addition": "For 5 + 3, start with 5 and add 3 more. The result is 8.",
        "subtraction": "For 10 - 4, take 4 away from 10. The result is 6.",
        "multiplication": "For 7 * 2, add 7 twice (7 + 7). The product is 14.",
        "division": "For 20 / 4, split 20 into 4 equal groups. Each group contains 5.",
        "modulus": "For 10 % 3, 3 fits into 10 three whole times (9), leaving a remainder of 1.",
        "floor division": "For 10 // 3, 10 / 3 is 3.333..., and rounding down gives the whole-number result 3.",
        "square root": "The square root of 16 is 4 because 4 multiplied by itself equals 16.",
        "power": "For 2^3, multiply the base 2 by itself 3 times: 2 * 2 * 2 = 8.",
        "logarithm": "log(100, 10) asks which power of 10 equals 100. Since 10^2 = 100, the answer is 2.",
        "sine": "sin(30°) is approximately 0.5. Sine relates an angle in a right triangle to opposite side / hypotenuse.",
        "cosine": "cos(60°) is 0.5. Cosine relates an angle in a right triangle to adjacent side / hypotenuse.",
        "tangent": "tan(45°) is 1. Tangent relates an angle in a right triangle to opposite side / adjacent side.",
        "mean": "For [1, 2, 3], add the values (1 + 2 + 3 = 6), then divide by the 3 values. The mean is 2.",
        "mode": "In [1, 2, 2, 3], the value 2 appears most often (twice), so the mode is 2.",
        "median": "Sort [1, 3, 2] into [1, 2, 3]. The middle value is 2, so the median is 2.",
        "range": "In [1, 3, 2], the largest value is 3 and the smallest is 1. Their difference (3 - 1) is 2.",
        "hyperbolic sine": "sinh(30°) is approximately 0.548 when 30° is converted to radians (about 0.524) before applying sinh.",
        "hyperbolic cosine": "cosh(30°) is approximately 1.140 when 30° is converted to radians (about 0.524) before applying cosh.",
        "hyperbolic tangent": "tanh(30°) is approximately 0.480 when 30° is converted to radians (about 0.524) before applying tanh.",
        "hyperbolic arcsine": "arcsinh(1) is approximately 0.881 radians. It is the value whose hyperbolic sine is 1.",
        "hyperbolic arccosine": "arccosh(2) is approximately 1.317 radians. It is the non-negative value whose hyperbolic cosine is 2.",
        "hyperbolic arctangent": "arctanh(0.5) is approximately 0.549 radians. It is the value whose hyperbolic tangent is 0.5.",
        "radian conversion": "To convert 180° to radians, multiply by π / 180. This gives π radians, one half-turn.",
        "degree conversion": "To convert π radians to degrees, multiply by 180 / π. This gives 180°, one half-turn."
    }
    if calc in examples:
        print(f"{calc.capitalize()} Example: {examples[calc]}")
    else:
        print("Sorry, I don't have an example for that calculation.")
    
math_mentor_ai()