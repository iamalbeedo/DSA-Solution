class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        half_len = n // 2
        
        # Step 1 & 2: Extract and sort the first half
        left = "".join(sorted(s[:half_len]))
        
        # Step 3: Extract middle character if length is odd
        mid = s[half_len] if n % 2 != 0 else ""
        
        # Step 4 & 5: Reverse the left half for the right side and concatenate
        right = left[::-1]
        
        return left + mid + right