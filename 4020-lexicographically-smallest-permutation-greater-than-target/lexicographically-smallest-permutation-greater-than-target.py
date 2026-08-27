class Solution:

    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord("a")] += 1

        best_result = None

        for i in range(n):
            t_char_idx = ord(target[i]) - ord("a")

            # Try to place a character strictly greater than target[i] at position i
            for c in range(t_char_idx + 1, 26):
                if count[c] > 0:
                    prefix = target[:i] + chr(ord("a") + c)

                    # Temporarily use character c
                    count[c] -= 1

                    # Fill remaining characters in ascending order
                    suffix = "".join(
                        chr(ord("a") + ch) * count[ch] for ch in range(26)
                    )
                    candidate = prefix + suffix

                    if best_result is None or candidate < best_result:
                        best_result = candidate

                    # Backtrack
                    count[c] += 1
                    break

            # Try to match target[i] to continue matching prefix
            if count[t_char_idx] > 0:
                count[t_char_idx] -= 1
            else:
                break

        return best_result if best_result is not None else ""