class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        sample = "123456789"
        ans = []
        
        # Outer loop controls the length of the window (from 2 digits up to 9 digits)
        for length in range(2, 10):
            # Inner loop moves the sliding window across the sample string
            for start in range(10 - length):
                # Slice the string to get a sequential substring and convert it to an integer
                num = int(sample[start:start + length])
                
                # Check if it falls within our requested range bounds
                if low <= num <= high:
                    ans.append(num)
                    
        return ans