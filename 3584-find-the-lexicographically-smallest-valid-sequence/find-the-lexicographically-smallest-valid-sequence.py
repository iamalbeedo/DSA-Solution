class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)

        # Precompute maximum matching suffix length of word2 from index i in word1
        suffix = [0] * (n + 1)
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
            suffix[i] = m - 1 - j

        result = []
        j = 0
        modified = False

        for i in range(n):
            if j == m:
                break

            is_match = (word1[i] == word2[j])

            if is_match:
                result.append(i)
                j += 1
            elif not modified and suffix[i + 1] >= m - 1 - j:
                result.append(i)
                j += 1
                modified = True

        return result if len(result) == m else []