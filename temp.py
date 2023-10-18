def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius*9/5+32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = fahrenheit-32*5/9
    return celsius

celsius = 25
#fahrenheit = celsius*9/5+32
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} Celsius to Fahrenheit is {fahrenheit}")

"given a fahrenheit value return the converted celsius value"
fahrenheit = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit} Fahrenheit to Celsius is {celsius}")