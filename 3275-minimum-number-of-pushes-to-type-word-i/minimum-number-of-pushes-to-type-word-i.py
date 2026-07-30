class Solution:
    def minimumPushes(self, word: str) -> int:
        # Step 1: Count frequencies
        freq = [0] * 26
        for char in word:
            freq[ord(char) - ord('a')] += 1

        # Step 2: Sort in descending order
        freq.sort(reverse=True)

        total_pushes = 0

        # Step 3: Accumulate cost greedily
        for idx in range(26):
            if freq[idx] == 0:
                break
            
            push_cost = (idx // 8) + 1
            total_pushes += push_cost * freq[idx]

        return total_pushes