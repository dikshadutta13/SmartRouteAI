def display_menu():
    print("\n")
    print("=" * 60)
    print("                  SMARTROUTE AI")
    print("=" * 60)
    print("1. View City Map")
    print("2. Find Route")
    print("3. Compare Algorithms")
    print("4. Update Traffic Conditions")
    print("5. View Performance Report")
    print("6. Exit")
    print("=" * 60)


def get_menu_choice():
    while True:
        choice = input("Enter your choice (1-6): ").strip()

        if choice in {"1", "2", "3", "4", "5", "6"}:
            return choice

        print("Invalid choice. Please enter a number from 1 to 6.")