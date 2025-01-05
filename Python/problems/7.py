class Solution:
    def reverse(self, x: int) -> int:
        # Define max range and initialize multiplier for sign
        high = 0
        mul = 1
        
        # Set range and sign based on the input
        if x < 0:
            high = 2**31  # For negative numbers
            mul = -1
        else:
            high = 2**31 - 1  # For positive numbers
        
        # Work with the absolute value of x
        x = abs(x)
        rev = 0
        
        while x:
            dig = x % 10
            
            # Check if adding the digit will overflow
            if rev <= (high - dig) // 10:
                rev = 10 * rev + dig  # Update reversed number
            else:
                return 0  # Return 0 if overflow occurs
            
            x = x // 10  # Remove the last digit
        
        return mul * rev
