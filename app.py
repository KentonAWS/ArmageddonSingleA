from meifumado13_lb1.run_age_calculator import run_age_calculator
from kenton_lab1.greeting import greeting
from Lab1_ec.ask_hobby import ask_hobby
from solomon_lab1.ask_lucky import ask_lucky
from atreides_lab1.run_temp_converter import run_temp_converter


def main():
    while True:
        print("\n===== TEAM APPLICATION =====")
        print("1. Calculate Age (meifumado13/vlad)")
        print("2. Greeting (Kenton)")
        print("3. ask_hobby (Ephraim)")
        print("4. ask_lucky (Solomon)")
        print("5. run_temp_converter (Atreides/Saad)")
        print("6. Exit")
        print("============================")

        choice = input("Select option (1-6): ").strip()

        if choice == "1":
            run_age_calculator()
        elif choice == "2":
            greeting()
        elif choice == "3":
            ask_hobby()
        elif choice == "4":
            ask_lucky()
        elif choice == "5":
            run_temp_converter()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()