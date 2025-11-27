def greeting():
    print ("Hi there!")

def calculate_pi_to_5_digits():
    """
    Calculate the value of Pi to the 5th digit (3.14159) using the Nilakantha series.
    The series is: π = 3 + 4/(2×3×4) - 4/(4×5×6) + 4/(6×7×8) - 4/(8×9×10) + ...
    Returns the value of Pi accurate to 5 decimal places.
    """
    pi = 3.0
    sign = 1
    denominator = 2
    
    # Run enough iterations to get 5 decimal places of accuracy
    # For Nilakantha series, this should be more than sufficient
    for i in range(1000):
        term = 4.0 / (denominator * (denominator + 1) * (denominator + 2))
        pi += sign * term
        sign *= -1
        denominator += 2
        
        # Check if we've reached the desired precision
        if abs(pi - 3.14159) < 0.000001:
            break
    
    # Return pi rounded to 5 decimal places
    return round(pi, 5)