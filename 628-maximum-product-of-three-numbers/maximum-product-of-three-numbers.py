class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        # Step 1: Initialize max variables to negative infinity 
        # and min variables to positive infinity
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')
        
        # Step 2: Iterate through every number to find top 3 max and top 2 min
        for n in nums:
            # Update the top 3 maximum values
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n > max2:
                max3 = max2
                max2 = n
            elif n > max3:
                max3 = n
                
            # Update the top 2 minimum values
            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n
                
        # Step 3 & 4: Compare the product of 3 largest vs. (2 smallest * 1 largest)
        return max(max1 * max2 * max3, min1 * min2 * max1)

# Time Complexity: O(N)
# Space Complexity: O(1)