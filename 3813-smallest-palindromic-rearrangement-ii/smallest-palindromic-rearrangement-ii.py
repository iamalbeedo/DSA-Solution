import math

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # Step 1: Count character frequencies in s
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1

        half = [0] * 26
        mid_char = ""
        m = 0

        # Step 2: Split frequencies into left half and center element
        for i in range(26):
            if freq[i] % 2 != 0:
                mid_char = chr(ord('a') + i)
            half[i] = freq[i] // 2
            m += half[i]

        # Combinatorics helper capped at target_k + 1 to prevent overflow
        def get_ways(f: list[int], target_k: int) -> int:
            ways = 1
            curr_len = 0
            for count in f:
                if count > 0:
                    curr_len += count
                    n = curr_len
                    r = count

                    if r > n - r:
                        r = n - r
                    cur_nCr = 1

                    for i in range(1, r + 1):
                        cur_nCr = cur_nCr * (n - i + 1) // i
                        if cur_nCr > target_k:
                            cur_nCr = target_k + 1
                            break

                    ways *= cur_nCr
                    if ways > target_k:
                        return target_k + 1
            return ways

        # Step 3: Return empty string if k exceeds total available permutations
        if get_ways(half, k) < k:
            return ""

        # Step 4: Build the left half character-by-character greedily
        first_half = []
        for _ in range(m):
            for c in range(26):
                if half[c] > 0:
                    half[c] -= 1
                    ways = get_ways(half, k)

                    if ways >= k:
                        first_half.append(chr(ord('a') + c))
                        break
                    else:
                        k -= ways
                        half[c] += 1  # Backtrack

        # Step 5: Assemble full palindrome
        left_str = "".join(first_half)
        right_str = left_str[::-1]

        return left_str + mid_char + right_str