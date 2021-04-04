import conversions
import conversions_refactored
import unittest


class ConversionFunctions(unittest.TestCase):
    known_C_to_K_conversions = ((300, 573.15),
        (500, 773.15),
        (0, 273.15),
        (-130, 143.15),
        (-273.15, 0))

    def test_convertCelsiusToKelvin(self):
        for celsius, expected in self.known_C_to_K_conversions:
            actual = conversions.convertCelsiusToKelvin(celsius)
            self.assertAlmostEqual(expected, actual, places=2, msg="Celsius to  Kelvin conversion failed")

    def test_convertKelvinToCelsius(self):
        for expected, kelvin in self.known_C_to_K_conversions:
            actual = conversions.convertKelvinToCelsius(kelvin)
            self.assertAlmostEqual(expected, actual, places=2, msg='Kelvin to Celsius conversion failed')

    known_C_to_F_conversions = ((300, 572),
    (500, 932),
    (0, 32),
    (-130, -202),
    (-273.15, -459.67))

    def test_convertCelsiusToFahrenheit(self):
        for celsius, expected in self.known_C_to_F_conversions:
            actual = conversions.convertCelsiusToFahrenheit(celsius)
            self.assertAlmostEqual(expected, actual, places=2, msg='Celsius to Fahrenheit conversion failed')

    def test_convertFahrenheitToCelsius(self):
        for expected, fahrenheit in self.known_C_to_F_conversions:
            actual = conversions.convertFahrenheitToCelsius(fahrenheit)
            self.assertAlmostEqual(expected, actual, places=2, msg='Fahrenheit to Celsius conversion failed')

    known_K_to_F_conversions = ((573.15, 572),
    (773.15, 932),
    (273.15, 32),
    (143.15, -202),
    (0, -459.67))

    def test_convertKelvinToFahrenheit(self):
        for kelvin, expected in self.known_K_to_F_conversions:
            actual = conversions.convertKelvinToFahrenheit(kelvin)
            self.assertAlmostEqual(expected, actual, places=2, msg='Kelvin to Fahrenheit conversion failed')

    def test_convertFahrenheitToKelvin(self):
        for expected, fahrenheit in self.known_K_to_F_conversions:
            actual = conversions.convertFahrenheitToKelvin(fahrenheit)
            self.assertAlmostEqual(expected, actual, places=2, msg='Fahrenheit to Kelvin conversion failed')

    '''Test conversions_refactored temperature'''

    def test_convertCtoK(self):
        fromUnit = 'C'
        toUnit = 'K'
        for value, expected in self.known_C_to_K_conversions:
            actual = conversions_refactored.convert(fromUnit, toUnit, value)
            self.assertAlmostEqual(expected, actual, places=2, msg="Celsius to  Kelvin conversion failed")
        
    def test_convertCtoF(self):
        fromUnit = 'C'
        toUnit = 'F'
        for value, expected in self.known_C_to_F_conversions:
            actual = conversions_refactored.convert(fromUnit, toUnit, value)
            self.assertAlmostEqual(expected, actual, places=2, msg="Celsius to  Fahrenheit conversion failed")

    def test_convertKtoC(self):
        fromUnit = 'K'
        toUnit = 'C'
        for expected, value in self.known_C_to_K_conversions:
            actual = conversions_refactored.convert(fromUnit, toUnit, value)
            self.assertAlmostEqual(expected, actual, places=2, msg="Kelvin to  Celsius conversion failed")

    def test_convertKtoF(self):
        fromUnit = 'K'
        toUnit = 'F'
        for value, expected in self.known_K_to_F_conversions:
            actual = conversions_refactored.convert(fromUnit, toUnit, value)
            self.assertAlmostEqual(expected, actual, places=2, msg="Kelvin to  Fahrenheit conversion failed")

    def test_convertFtoC(self):
        fromUnit = 'F'
        toUnit = 'C'
        for expected, value in self.known_C_to_F_conversions:
            actual = conversions_refactored.convert(fromUnit, toUnit, value)
            self.assertAlmostEqual(expected, actual, places=2, msg="Fahrenheit to Celsius conversion failed")

    def test_convertFtoK(self):
        fromUnit = 'F'
        toUnit = 'K'
        for expected, value in self.known_K_to_F_conversions:
            actual = conversions_refactored.convert(fromUnit, toUnit, value)
            self.assertAlmostEqual(expected, actual, places=2, msg="Fahrenheit to Kelvin conversion failed")

    '''Test conversions_refactored distance: mi, yd, m'''

    known_mi_to_yd_conversions = ((1, 1760),
        (0.00056818, 1),
        (2, 3520),
        (0.00113636, 2),
        (100, 176000))

    def test_convert_mi_to_yd(self):
        fromUnit = 'mi'
        toUnit = 'yd'
        for value, expected in self.known_mi_to_yd_conversions:
            actual = conversions_refactored.convert(fromUnit, toUnit, value)
            self.assertAlmostEqual(expected, actual, places=2, msg="Miles to yards conversion failed")

    def test_convert_yd_to_mi(self):
        fromUnit = 'yd'
        toUnit = 'mi'
        for expected, value in self.known_mi_to_yd_conversions:
            actual = conversions_refactored.convert(fromUnit, toUnit, value)
            self.assertAlmostEqual(expected, actual, places=2, msg="Yards to miles conversion failed")

    known_yds_to_m_conversions = ((1, 0.9144),
        (1.0936133, 1),
        (2, 1.8288),
        (2.1872266, 2),
        (100, 91.44))

    def test_convert_yd_to_m(self):
        fromUnit = 'yd'
        toUnit = 'm'
        for value, expected in self.known_yds_to_m_conversions:
            actual = conversions_refactored.convert(fromUnit, toUnit, value)
            self.assertAlmostEqual(expected, actual, places=2, msg='Yards to meters conversion failed')

    def test_convert_m_to_yd(self):
        fromUnit = 'm'
        toUnit = 'yd'
        for expected, value in self.known_yds_to_m_conversions:
            actual = conversions_refactored.convert(fromUnit, toUnit, value)
            self.assertAlmostEqual(expected, actual, places=2, msg='Meters to yards conversion failed')

    known_m_to_mi_conversions = ((1, 0.00062137),
        (1609.344, 1),
        (2, 0.00124274),
        (3218.688, 2),
        (100, 0.06213712))

    def test_convert_m_to_mi(self):
        fromUnit = 'm'
        toUnit = 'mi'
        for value, expected in self.known_m_to_mi_conversions:
            actual = conversions_refactored.convert(fromUnit, toUnit, value)
            self.assertAlmostEqual(expected, actual, places=2, msg='Meters to miles conversion failed')

    def test_convert_mi_to_m(self):
        fromUnit = 'mi'
        toUnit = 'm'
        for expected, value in self.known_m_to_mi_conversions:
            actual = conversions_refactored.convert(fromUnit, toUnit, value)
            self.assertAlmostEqual(expected, actual, places=2, msg='Miles to meters conversion failed')

    known_unit_to_self_conversions = ((0, 0),
        (1, 1),
        (10, 10),
        (-1, -1),
        (-10, -10))

    conversion_possibilities = [('C', 'C'), ('C', 'F'), ('C', 'K'), ('F', 'F'), ('F', 'K'), ('K', 'K')]

    def test_convertCToSelf(self):
        fromUnit = 'C'
        toUnit = 'C'
        for value, expected in self.known_unit_to_self_conversions:
            actual = conversions_refactored.convert(fromUnit, toUnit, value)
            self.assertEqual(actual, expected, msg='Unit to same unit conversion failed')

    def test_convertKToSelf(self):
        fromUnit = 'K'
        toUnit = 'K'
        for value, expected in self.known_unit_to_self_conversions:
            actual = conversions_refactored.convert(fromUnit, toUnit, value)
            self.assertEqual(actual, expected, msg='Unit to same unit conversion failed')

    def test_convertFToSelf(self):
        fromUnit = 'F'
        toUnit = 'F'
        for value, expected in self.known_unit_to_self_conversions:
            actual = conversions_refactored.convert(fromUnit, toUnit, value)
            self.assertEqual(actual, expected, msg='Unit to same unit conversion failed')

    def test_convertmiToSelf(self):
        fromUnit = 'mi'
        toUnit = 'mi'
        for value, expected in self.known_unit_to_self_conversions:
            actual = conversions_refactored.convert(fromUnit, toUnit, value)
            self.assertEqual(actual, expected, msg='Unit to same unit conversion failed')

    def test_convertydToSelf(self):
        fromUnit = 'yd'
        toUnit = 'yd'
        for value, expected in self.known_unit_to_self_conversions:
            actual = conversions_refactored.convert(fromUnit, toUnit, value)
            self.assertEqual(actual, expected, msg='Unit to same unit conversion failed')

    def test_convertmToSelf(self):
        fromUnit = 'm'
        toUnit = 'm'
        for value, expected in self.known_unit_to_self_conversions:
            actual = conversions_refactored.convert(fromUnit, toUnit, value)
            self.assertEqual(actual, expected, msg='Unit to same unit conversion failed')

    
class BadInput(unittest.TestCase):

    conversion_not_possible = (('C', 'm'),
    ('K', 'mi'),
    ('F', 'yd'),
    ('m', 'K'), 
    ('mi', 'F'),
    ('yd', 'C'))

    def test_ConversionNotPossible(self):
        '''covert should fail when attempting to convert temperature to distance and vice versa'''
        for fromUnit, toUnit in self.conversion_not_possible:
            self.assertRaises(conversions_refactored.ConversionNotPossible, conversions_refactored.convert, fromUnit, toUnit, value=100)


if __name__ == '__main__':
    unittest.main()
