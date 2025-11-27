import unittest
from main import calculate_pi_to_5_digits

class TestPiCalculation(unittest.TestCase):
    def test_pi_calculation(self):
        """Test that the calculated pi value is accurate to 5 decimal places"""
        # The expected value of Pi to 5 decimal places
        expected_pi = 3.14159
        
        # Call the function to calculate Pi
        calculated_pi = calculate_pi_to_5_digits()
        
        # Test that the calculated value matches the expected value
        self.assertEqual(calculated_pi, expected_pi)
        
    def test_pi_type(self):
        """Test that the returned value is a float"""
        self.assertIsInstance(calculate_pi_to_5_digits(), float)
        
    def test_pi_digits(self):
        """Test that the returned value has 5 decimal places"""
        pi_str = str(calculate_pi_to_5_digits())
        # Get the part after the decimal point
        decimal_part = pi_str.split('.')[1]
        # Check that we have exactly 5 digits after the decimal point
        self.assertEqual(len(decimal_part), 5)

if __name__ == "__main__":
    unittest.main()