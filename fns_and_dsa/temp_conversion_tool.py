# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if __name__ == "__main__":
    try:
        # Prompt user for temperature
        temp = float(input("Enter the temperature to convert: "))
        scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Perform conversion
        if scale == 'C':
            converted = convert_to_fahrenheit(temp)
            # Print output exactly like assignment example
            print(f"{temp}°C is {converted}")
        elif scale == 'F':
            converted = convert_to_celsius(temp)
            print(f"{temp}°F is {converted}")
        else:
            print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
# --- IGNORE ---ok