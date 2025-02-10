# Exercise 2: Temperature Conversion

def convertToCelsiusAsk():
    fahrenheit_temp = float(input("What is the temperature in Fahrenheit you wish to convert to degrees Celsius? "))
    celsuis_temp = (fahrenheit_temp - 32) * 5 / 9
    print("The temperature " + str(fahrenheit_temp) + " degrees Fahrenheit is " + str(celsuis_temp) + " degrees Celsius.")

def convertToFarenheitAsk():
    celsius_temp = float(input("What is the temperature in Celsius you wish to convert to degrees Fahrenheit? "))
    fahrenheit_temp = celsius_temp * 9/5 + 32
    print("The temperature " + str(celsius_temp) + "d egrees Celsius is " + str(fahrenheit_temp) + " degrees Fahrenheit.")

convertToCelsiusAsk()

def convertToCelsius(farenheit_input):
    celsius_output = (farenheit_input - 32) * 5 / 9
    return celsius_output

def convertToFarenheit(celsius_input):
    farenheit_output = celsius_input * 9/5 + 32
    return farenheit_output

assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFarenheit(0) == 32
assert convertToFarenheit(100) == 212
assert convertToCelsius(convertToFarenheit(15)) == 15

print(convertToCelsius(0))
print(convertToCelsius(180))
print(convertToFarenheit(0))
print(convertToFarenheit(100))
print(convertToCelsius(convertToFarenheit(15)))