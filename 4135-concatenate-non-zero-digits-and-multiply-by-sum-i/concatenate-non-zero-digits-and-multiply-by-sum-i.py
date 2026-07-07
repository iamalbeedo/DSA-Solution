class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        digit_sum = 0
        multiplier = 1

        # WHAT: Extract digits from right to left using arithmetic operators
        # WHY: Avoids memory allocation overhead from turning integers into strings or arrays
        while n > 0:
            digit = n % 10
            
            if digit != 0:
                # Place the digit on the left side of our building value 'x'
                x += digit * multiplier
                # Step up the multiplier place value by a factor of 10
                multiplier *= 10
                # Accumulate the digit into our total sum
                digit_sum += digit
                
            n //= 10  # Drop the lowest digit
            
        return x * digit_sum