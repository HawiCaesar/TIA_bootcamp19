import unittest
from temp_converter import convert_celcuius_to_farenheit

class TempConverterTest(unittest.TestCase):
	# given temp in celicus = correct value in Farrenheit

	def test_celcius_is_converted_to_farenheit(self):
		"""
			- F = C * 9/5 + 32
			- Data type of input
			- throw an exception when data type is incorrect
			- check for null values => throw an error
		"""

		actual = convert_celcuius_to_farenheit(10)
		expected  = 50

		self.assertEqual(actual ,expected, "Farenheit value should be 50")
		#self.assertEqual(convert_celcuius_to_farenheit("String"),, "Value should be 68")