class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        # Line 1: Sort the array and remove duplicate values using set().
        # WHY: 'set(arr)' keeps only unique numbers. 'sorted(...)' arranges them from smallest to largest.
        sorted_unique = sorted(set(arr))
        
        # Line 2: Create an empty dictionary (Hash Map) to store our ranks.
        # WHY: We need a quick way to map a number (like 10) to its rank (like 1).
        rank_map = {}
        
        # Line 3: Loop through the sorted unique numbers along with a counter starting at 1.
        # WHY: 'enumerate(..., 1)' gives us both the index/rank (starting from 1) and the number itself.
        for rank, num in enumerate(sorted_unique, 1):
            rank_map[num] = rank # Store the relationship: {number: rank}
            
        # Line 4: Replace each number in the original array with its rank from the dictionary.
        # WHY: We loop through the original 'arr', fetch the rank of each number from 'rank_map', and collect them in a new list.
        return [rank_map[num] for num in arr]