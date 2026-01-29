# run_temp_converter.py
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def run_temp_converter():
    f = float(input("Enter Fahrenheit: ").strip())
    c = fahrenheit_to_celsius(f)
    print(f"{f}F = {c:.2f}C")


if __name__ == "__main__":
    run_temp_converter()

  
  
    # Test runs only when you run this file directly
    
    
    
    


