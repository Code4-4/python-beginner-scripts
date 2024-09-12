# temperature_converter.py
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    temp = float(input("Enter temperature: "))
    scale = input("Convert from (C/F): ").upper()
    if scale == "C":
        print(f"{temp} Celsius is {celsius_to_fahrenheit(temp)} Fahrenheit.")
    elif scale == "F":
        print(f"{temp} Fahrenheit is {fahrenheit_to_celsius(temp)} Celsius.")
    else:
        print("Invalid scale entered.")
