# Temperature Converter

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose option (1/2): ")

if choice == "1":
    c = float(input("Enter temperature in Celsius: "))
    result = celsius_to_fahrenheit(c)
    print("Temperature in Fahrenheit:", result)

elif choice == "2":
    f = float(input("Enter temperature in Fahrenheit: "))
    result = fahrenheit_to_celsius(f)
    print("Temperature in Celsius:", result)

else:
    print("Invalid choice")