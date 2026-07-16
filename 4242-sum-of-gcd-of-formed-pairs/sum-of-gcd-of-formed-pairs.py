import math

class Solution:
    def gcdSum(self, arr: list[int]) -> int:
        n = len(arr)
        prefi = []
        mx = 0
        
        # Extract intermediate GCD pairs using the running maximum value tracking variable
        for num in arr:
            if num > mx:
                mx = num
            prefi.append(math.gcd(mx, num))
            
        # Sort the processed dataset to position matching extremes at the array boundaries
        prefi.sort()
        
        i = 0
        j = n - 1
        total_sum = 0
        
        # Advance inward symmetrically to match elements from opposite ends of the sorted sequence
        while i < j:
            total_sum += math.gcd(prefi[i], prefi[j])
            i += 1
            j -= 1
            
        return total_sum