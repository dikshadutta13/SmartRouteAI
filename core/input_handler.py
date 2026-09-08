def get_location(prompt, available_locations):
    while True:
        location = input(prompt).strip().upper()

        if location in available_locations:
            return location

        print(
            f"Invalid location. Choose from: "
            f"{', '.join(sorted(available_locations))}"
        )


def get_optimization_mode():
    print("\nOptimization Preference")
    print("-" * 30)
    print("1. Minimum Distance")
    print("2. Minimum Travel Time")
    print("3. Minimum Traffic")
    print("4. Balanced Route")

    while True:
        choice = input("\nEnter choice (1-4): ").strip()

        if choice in {"1", "2", "3", "4"}:
            return choice

        print("Invalid choice. Please enter 1, 2, 3 or 4.")