class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # THE MAGIC LOGIC:
        # - Sum of first 'n' odd numbers  = n^2
        # - Sum of first 'n' even numbers = n * (n + 1)
        #
        # Finding the GCD:
        # GCD(n^2, n * (n + 1)) 
        # = n * GCD(n, n + 1)  <-- Factor out n
        # = n * 1               <-- Consecutive numbers always have a GCD of 1
        # = n
        
        return n