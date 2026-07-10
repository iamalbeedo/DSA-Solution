import math
class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[int]:
        # WHAT: Pair up values with their original indices and sort them.
        # WHY: Enables continuous sliding window evaluation on numbers.
        sorted_pairs = sorted([(nums[i], i) for i in range(n)])
        
        # WHAT: Map original index keys to their relative index placement within sorted_pairs.
        pos = [0] * n
        for sorted_idx, (_, original_idx) in enumerate(sorted_pairs):
            pos[original_idx] = sorted_idx
            
        # Determine bit width limit dynamically based on graph size
        max_l = int(math.log2(n)) + 2
        up = [[0] * n for _ in range(max_l)]
        
        # WHAT: Two-pointer sliding window computation for single baseline jumps.
        r = 0
        for l in range(n):
            while r + 1 < n and sorted_pairs[r + 1][0] - sorted_pairs[l][0] <= maxDiff:
                r += 1
            up[0][l] = r
            
        # WHAT: Precompute binary lifting powers table.
        for j in range(1, max_l):
            for i in range(n):
                up[j][i] = up[j - 1][up[j - 1][i]]
                
        ans = []
        
        # WHAT: Execute queries via O(log N) jump evaluation checks.
        for u_orig, v_orig in queries:
            u, v = pos[u_orig], pos[v_orig]
            if u > v:
                u, v = v, u
                
            if u == v:
                ans.append(0)
            elif up[0][u] >= v:
                ans.append(1)
            elif up[-1][u] < v:
                ans.append(-1)
            else:
                steps = 0
                for j in range(max_l - 1, -1, -1):
                    if up[j][u] < v:
                        steps += (1 << j)
                        u = up[j][u]
                ans.append(steps + 1)
                
        return ans