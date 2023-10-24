# Lab2.py

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    # Read a sequence of numbers from the user
    input_str = input("Enter some numbers separated by commas (e.g. 5, 67, 32): ")

    # Use split() to create a list of strings
    numbers_as_strings = input_str.split(",")

    # Convert the list of strings to a list of floats
    numbers_as_floats = [float(num) for num in numbers_as_strings]

    # Return the list of floats
    return numbers_as_floats

def calc_average(temperatures):
    return sum(temperatures) / len(temperatures)

def find_min_max(temperatures):
    min_temp = min(temperatures)
    max_temp = max(temperatures)
    return [min_temp, max_temp]

def sort_temperature(temperatures):
    return sorted(temperatures)

def calc_median_temperature(temperatures):
    sorted_temps = sorted(temperatures)
    n = len(sorted_temps)
    if n % 2 == 0:
        mid1 = sorted_temps[n // 2 - 1]
        mid2 = sorted_temps[n // 2]
        return (mid1 + mid2) / 2
    else:
        return sorted_temps[n // 2]

# Lab2.py

def calc_average_temperature(temperatures):
    if not temperatures:
        return 0.0  # Handle division by zero if the list is empty
    return sum(temperatures) / len(temperatures)

def calc_min_max_temperature(temperatures):
    if not temperatures:
        return [0, 0]  # Handle an empty list by returning [0, 0]

    min_temp = int(min(temperatures))
    max_temp = int(max(temperatures))
    return [min_temp, max_temp]
5

# Example usage:
if __name__ == "__main__":
    display_main_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        temps = get_user_input()
        average_temp = calc_average(temps)
        print("Average Temperature:", average_temp)

    elif choice == 2:
        temps = get_user_input()
        min_max_temp = find_min_max(temps)
        print("Min Temperature:", min_max_temp[0])
        print("Max Temperature:", min_max_temp[1])

    elif choice == 3:
        temps = get_user_input()
        sorted_temps = sort_temperature(temps)
        print("Sorted Temperatures:", sorted_temps)

    elif choice == 4:
        temps = get_user_input()
        median_temp = calc_median_temperature(temps)
        print("Median Temperature:", median_temp)

    elif choice == 5:
        print("Quitting program.")

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
