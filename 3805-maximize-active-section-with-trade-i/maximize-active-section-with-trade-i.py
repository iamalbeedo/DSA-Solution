class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # Count total original '1's in string s
        ones = s.count('1')
        
        # Augment boundaries so edge cases uniformize into standard zero-surrounded blocks
        s = "1" + s + "1"
        
        n = len(s)
        i = 0
        ans = ones  # Default answer if no valid trade can be made
        
        # Skip initial boundary '1's to reach the first '0' block
        while i < n and s[i] == '1':
            i += 1
            
        # Measure the first contiguous '0' block length (c10)
        c10 = 0
        while i < n and s[i] == '0':
            c10 += 1
            i += 1
            
        # Slide window across subsequent [1-block] -> [0-block] pairs
        while i < n:
            
            # Measure the middle '1' block length (c11)
            c11 = 0
            while i < n and s[i] == '1':
                c11 += 1
                i += 1
                
            # Stop if there is no middle '1' block remaining
            if c11 == 0:
                break
                
            # Measure the right '0' block length (c20)
            c20 = 0
            while i < n and s[i] == '0':
                c20 += 1
                i += 1
                
            # Stop if there is no right '0' block to complete the trade sandwich
            if c20 == 0:
                break
                
            # Calculate potential total active section count after trading this middle block
            ans = max(ans, ones + c10 + c20)
            
            # Slide window: current right '0' block becomes the left '0' block for the next pass
            c10 = c20
            
        return ans