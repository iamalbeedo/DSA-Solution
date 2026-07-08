class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        m = len(s)
        MOD = 10**9 + 7

        # WHAT: Extract non-zero digits and store their original index references
        vals = []
        pos = []
        for i, char in enumerate(s):
            if char != '0':
                vals.append(int(char))
                pos.append(i)
                
        k = len(vals)

        # WHAT: Precompute base-10 powers modulo 10^9+7
        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # WHAT: Create prefix metrics for digit values and cumulative structural hashes
        pref_sum = [0] * (k + 1)
        pref_x = [0] * (k + 1)
        for i in range(k):
            pref_sum[i + 1] = pref_sum[i] + vals[i]
            pref_x[i + 1] = (pref_x[i] * 10 + vals[i]) % MOD

        # WHAT: Precompute tracking pointers to discover target intervals in O(1)
        next_non_zero = [k] * m
        prev_non_zero = [-1] * m

        # Populate pointer mapping pointing forward to the next non-zero digit
        curr_idx = k
        for i in range(m - 1, -1, -1):
            if s[i] != '0':
                curr_idx -= 1
            next_non_zero[i] = curr_idx

        # Populate pointer mapping pointing backward to the previous non-zero digit
        curr_idx = -1
        for i in range(m):
            if s[i] != '0':
                curr_idx += 1
            prev_non_zero[i] = curr_idx

        # WHAT: Execute queries efficiently
        ans = []
        for l, r in queries:
            idx_l = next_non_zero[l]
            idx_r = prev_non_zero[r]

            if idx_l > idx_r:
                ans.append(0)
            else:
                length = idx_r - idx_l + 1
                
                # Math isolation of numerical string ranges via structural prefixes
                x = (pref_x[idx_r + 1] - (pref_x[idx_l] * pow10[length]) % MOD) % MOD
                digit_sum = pref_sum[idx_r + 1] - pref_sum[idx_l]
                
                ans.append((x * digit_sum) % MOD)

        return ans