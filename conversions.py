
def convertCelsiusToKelvin(celsius):
    '''Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins'''
    kelvins = celsius + 273.15
    return kelvins


def convertCelsiusToFahrenheit(celsius):
    '''Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit'''
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit


def convertKelvinToCelsius(kelvin):
    '''Converts Celsius to Kelvin'''
    celsius = kelvin - 273.15
    return celsius


def convertKelvinToFahrenheit(kelvin):
    '''Converts Celsius to Fahrenheit'''
    fahrenheit =  (kelvin * (9/5)) - 459.67
    return fahrenheit


def convertFahrenheitToKelvin(fahrenheit):
    '''Converts Fahrenheit to kelvin'''
    kelvin = (fahrenheit + 459.67) * (5/9)
    return kelvin


def convertFahrenheitToCelsius(fahrenheit):
    '''Converts Celsius to Fahrenheit'''
    celsius = (fahrenheit - 32) * (5/9)
    return celsius
