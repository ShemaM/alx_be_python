# Global conversion factors
# These are defined at the top and are accessible (read-only) inside functions
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    # Reading the global variable FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    # Reading the global variable CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if __name__ == "__main__": 
    
    try:
        # Input validation: ensure the temperature is numeric
        temp = float(input("Enter the temperature to convert: "))

        # Input validation: clean input and ensure correct unit (C/F)
        scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Perform conversion based on user input
        if scale == 'C':
            converted = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted}°F")  # Include unit in output
        elif scale == 'F':
            converted = convert_to_celsius(temp)
            print(f"{temp}°F is {converted}°C")  # Include unit in output
        else:
            # Error message if user enters invalid scale
            print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        # Error message if user enters a non-numeric temperature
        print("Invalid temperature. Please enter a numeric value.")
