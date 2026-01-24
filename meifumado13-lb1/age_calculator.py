# age_calculator.py
from datetime import date

def calculate_age(birth_year):
    """Calculates age based on birth year."""
    current_year = date.today().year
    return current_year - birth_year

def run_age_calculator():
    """Runs the age calculator with user input."""
    birth_year = int(input("Enter your birth year: "))
    age = calculate_age(birth_year)
    print(f"You are {age} years old.")
    return age
  
if __name__ == "__main__":
 run_age_calculator()