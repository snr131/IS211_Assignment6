def convert(fromUnit, toUnit, value):
    '''Convert temperatures Celsius (C), Fahrenheit (F), Kelvin (K),'''
    '''and convert distances miles (m), yards (yd), meters (m)'''
    if fromUnit == "C" and toUnit == "K":
        k = value + 273.15
        return k
    elif fromUnit == "C" and toUnit == "F":
        f = (value * (9/5)) + 32
        return f
    elif fromUnit == "K" and toUnit == "C":
        c = value - 273.15
        return c
    elif fromUnit == "K" and toUnit == "F":
        f =  (value * (9/5)) - 459.67
        return f
    elif fromUnit == "F" and toUnit == "C":
        c = (value - 32) * (5/9)
        return c
    elif fromUnit == "F" and toUnit == "K":
        k = (value + 459.67) * (5/9)
        return k
    elif fromUnit == "mi" and toUnit == "yd":
        yd = value * 1760
        return yd
    elif fromUnit == "yd" and toUnit == "mi":
        mi = value / 1760
        return mi
    elif fromUnit == 'yd' and toUnit == 'm':
        m = value / 1.0936133
        return m
    elif fromUnit == 'm' and toUnit == 'yd':
        yd = value * 1.0936133
        return yd
    elif fromUnit == 'm' and toUnit == 'mi':
        mi = value / 1609.344
        return mi
    elif fromUnit == 'mi' and toUnit == 'm':
        m = value * 1609.344
        return m
    elif fromUnit == toUnit:
        return value
    else: 
        raise ConversionNotPossible('Temperature cannot convert to distance, and vice versa')


class  ConversionNotPossible(ValueError):
    pass
