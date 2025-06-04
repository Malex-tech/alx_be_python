# temp_conversion_tool.py

# Guidance:
# Define global variables for conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Guidance:
# This function converts Fahrenheit to Celsius using the global conversion factor
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Guidance:
# This function converts Celsius to Fahrenheit using the global conversion factor
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Prompt user for temperature input
        temp_input = input("Enter the temperature to convert: ")
        
        # Input validation: must be numeric
        temperature = float(temp_input)

        # Prompt user for the unit of the temperature
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Decision logic based on unit
        if unit == "F":
            # Convert from Fahrenheit to Celsius
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        elif unit == "C":
            # Convert from Celsius to Fahrenheit
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        else:
            # Handle invalid temperature unit
            raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")
    except ValueError as e:
        print(f"Error: {e}")
        print("Invalid temperature. Please enter a numeric value.")

# Guidance:
# This script demonstrates the concept of global variables and scope in function use.
# We're using global conversion factors without modifying them, so no `global` keyword is needed inside the functions.

if __name__ == "__main__":
    main()