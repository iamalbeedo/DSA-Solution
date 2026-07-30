class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        total_pushes = 0
        
        for i in range(n):
            # i // 8 + 1 gives 1 for first 8, 2 for next 8, etc.
            total_pushes += (i // 8) + 1
            
        return total_pushes