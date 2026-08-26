class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        n = len(s)
        i = 0
        count = 0
        length = float('inf')
        ans = s

        for j in range(n):

            if s[j] == '1':
                count += 1

            while i < n and (count > k or s[i] == '0'):
                if s[i] == '1':
                    count -= 1
                i += 1

            if count == k:
                curr_len = j - i + 1
                curr = s[i:j + 1]

                if curr_len < length:
                    length = curr_len
                    ans = curr

                elif curr_len == length and curr < ans:
                    ans = curr

        return "" if length == float('inf') else ans