print("Hello, Welcome to CALCAPP")
import MathMentorAI as MMAI
import tkinter as tk
from tkinter import messagebox

## This is still very much under development and is not a finished product. ##


print("The Order of Operations is addition, subtraction, multiplication, division, modulus, floor division, square root, power, logarithm, sine, cosine, tangent, mean, mode, median and range.")
print("hyperbolic sine, hyperbolic cosine, hyperbolic tangent, hyperbolic arcsine, hyperbolic arccosine, hyperbolic arctangent, radian conversion and degree conversion.")
choice = input("Please choose a calculation from the list above: ")

if choice == 'addition' or choice == 'add':
    import addCALC as addCALC
    
elif choice == 'subtraction' or choice == 'subtract':
    import subtractCALC as subtractCALC
    
elif choice == 'multiplication' or choice == 'multiply':
    import multiplyCALC as multiplyCALC
    
elif choice == 'division' or choice == 'divide':
    import divideCALC as divideCALC
    
elif choice == 'modulus' or choice == 'mod':
    import modulusCALC as modulusCALC
    
elif choice == 'floor division' or choice == 'floor division':
    import floordivisionCALC as floordivisionCALC
    
elif choice == 'square root' or choice == 'squareroot':
    import squarerootCALC as squarerootCALC
    
elif choice == 'power' or choice == 'exponentiation':
    import powerCALC as powerCALC
    
elif choice == 'logarithm' or choice == 'log':
    import logarithmCALC as logarithmCALC
    
elif choice == 'sine' or choice == 'sin':
    import sineCALC as sineCALC
    
elif choice == 'cosine' or choice == 'cos':
    import cosineCALC as cosineCALC
    
elif choice == 'tangent' or choice == 'tan':
    import tangentCALC as tangentCALC
    
elif choice == 'mean' or choice == 'average':
    import meanCALC as meanCALC
    
elif choice == 'mode' or choice == 'most frequent':
    import modeCALC as modeCALC # type: ignore

elif choice == 'median' or choice == 'middle value':
    import medianCALC as medianCALC # type: ignore
    
elif choice == 'range' or choice == 'difference between largest and smallest':
    import rangeCALC as rangeCALC # type: ignore
    
elif choice == 'hyperbolic sine' or choice == 'sinh':
    import hyperbolicsineCALC as hyperbolicsineCALC # type: ignore
    
elif choice == 'hyperbolic cosine' or choice == 'cosh':
    import hyperboliccosineCALC as hyperboliccosineCALC # type: ignore
    
elif choice == 'hyperbolic tangent' or choice == 'tanh':
    import hyperbolictangentCALC as hyperbolictangentCALC # type: ignore
    
elif choice == 'hyperbolic arcsine' or choice == 'arcsinh':
    import hyperbolicarcsineCALC as hyperbolicarcsineCALC # type: ignore
    
elif choice == 'hyperbolic arccosine' or choice == 'arccosh':
    import hyperbolicarccosineCALC as hyperbolicarccosineCALC # type: ignore
    
elif choice == 'hyperbolic arctangent' or choice == 'arctanh':
    import hyperbolicarctangentCALC as hyperbolicarctangentCALC # type: ignore
    
elif choice == 'radian conversion' or choice == 'radian conversion':
    import radianconversionCALC as radianconversionCALC # type: ignore
    
elif choice == 'degree conversion' or choice == 'degree conversion':
    import degreeconversionCALC as degreeconversionCALC # type: ignore
else:
    print("Invalid choice. Please try again.")


while choice not in ['addition', 'subtraction', 'multiplication', 'division', 'modulus', 'floor division', 'square root', 'power', 'logarithm', 'sine', 'cosine', 'tangent', 'mean', 'mode', 'median', 'range', 'hyperbolic sine', 'hyperbolic cosine', 'hyperbolic tangent', 'hyperbolic arcsine', 'hyperbolic arccosine', 'radian conversion', 'degree conversion']:
    print("Invalid choice. Please try again.")
    choice = input("Please choose a calculation from the list above: ")
    print("Error34: Invalid response 560174081764805634856306450")
print("Thank you for using CALCAPP!")

print("Make sure to come back next time! Goodbye!")
print( "((Refer a friend))")

## Please let us know where improvements can be made. ##

def perform_calculation():
    choice = calc_var.get() # type: ignore
    if choice == "":
        messagebox.showwarning("No Selection", "Please choose a calculation.")
        return
    try:
        if choice == 'addition':
            import addCALC as addCALC
        elif choice == 'subtraction':
            import subtractCALC as subtractCALC
        elif choice == 'multiplication':
            import multiplyCALC as multiplyCALC
        elif choice == 'division':
            import divideCALC as divideCALC
        elif choice == 'modulus':
            import modulusCALC as modulusCALC
        elif choice == 'floor division':
            import floordivisionCALC as floordivisionCALC
        elif choice == 'square root':
            import squarerootCALC as squarerootCALC
        elif choice == 'power':
            import powerCALC as powerCALC
        elif choice == 'logarithm':
            import logarithmCALC as logarithmCALC
        elif choice == 'sine':
            import sineCALC as sineCALC
        elif choice == 'cosine':
            import cosineCALC as cosineCALC
        elif choice == 'tangent':
            import tangentCALC as tangentCALC
        elif choice == 'mean':
            import meanCALC as meanCALC
        elif choice == 'mode':
            import modeCALC as modeCALC
        elif choice == 'median':
            import medianCALC as medianCALC
        elif choice == 'range':
            import rangeCALC as rangeCALC
        elif choice == 'hyperbolic sine':
            import hyperbolicsineCALC as hyperbolicsineCALC
        elif choice == 'hyperbolic cosine':
            import hyperboliccosineCALC as hyperboliccosineCALC
        elif choice == 'hyperbolic tangent':
            import hyperbolictangentCALC as hyperbolictangentCALC
        elif choice == 'hyperbolic arcsine':
            import hyperbolicarcsineCALC as hyperbolicarcsineCALC
        elif choice == 'hyperbolic arccosine':
            import hyperbolicarccosineCALC as hyperbolicarccosineCALC
        elif choice == 'hyperbolic arctangent':
            import hyperbolicarctangentCALC as hyperbolicarctangentCALC
        elif choice == 'radian conversion':
            import radianconversionCALC as radianconversionCALC
        elif choice == 'degree conversion':
            import degreeconversionCALC as degreeconversionCALC
        else:
            messagebox.showerror("Invalid Choice", "Invalid calculation selected.")
            return
        
        messagebox.showinfo("Success", f"{choice.title()} module imported and executed!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def open_math_mentor_ai():
    mentor = tk.Toplevel()
    mentor.title("Math Mentor AI")
    mentor.geometry("400x400")
    mentor.configure(bg="#e3f2fd")

    tk.Label(mentor, text="Calculation:", bg="#e3f2fd").pack(pady=(10, 0))
    calc_entry = tk.Entry(mentor, width=30)
    calc_entry.pack(pady=(0, 10))

    def show_explanation():
        calc = calc_entry.get().strip().lower()
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
        explanation = explanations.get(calc, "Sorry, I don't have an explanation for that calculation.")
        messagebox.showinfo("Explanation", explanation, parent=mentor)

    def show_example():
        calc = calc_entry.get().strip().lower()
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
        example = examples.get(calc, "Sorry, I don't have an example for that calculation.")
        messagebox.showinfo("Example", example, parent=mentor)

    def show_general_help():
        help_text = (
            "General Math Help:\n"
            "- Use addition, subtraction, multiplication, and division for basic arithmetic.\n"
            "- Use trigonometric functions (sine, cosine, tangent) for angles.\n"
            "- Use logarithms for exponential calculations.\n"
            "- Use mean, median, and mode for statistics.\n"
            "- Use hyperbolic functions for advanced math.\n"
        )
        messagebox.showinfo("General Math Help", help_text, parent=mentor)





