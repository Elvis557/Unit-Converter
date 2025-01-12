def unit_converter():
    print("Unit Converter")
    print("1. Meters to Kilometers")
    print("2. Grams to Kilograms")
    print("3. Centimeters to Meters")
    print("4. Exit")

    while True:
        choice = input("Choose an option: ")
        if choice == "4":
            print("Goodbye!")
            break

        value = float(input("Enter the value to convert: "))

        if choice == "1":
            print(f"{value} meters = {value / 1000} kilometers")
        elif choice == "2":
            print(f"{value} grams = {value / 1000} kilograms")
        elif choice == "3":
            print(f"{value} cm = {value / 100} meters")
        else:
            print("Invalid choice!")

unit_converter()
