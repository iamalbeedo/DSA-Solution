class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Map out the absolute final appearance index for every unique character in the string
        last_index = {char: i for i, char in enumerate(s)}
        
        # Use a hash set container to quickly audit character existence inside our building window
        seen = set()
        stack = []
        
        for i, curr in enumerate(s):
            # Skip processing if this character is already elementally captured inside our path
            if curr in seen:
                continue
                
            # Pop characters off if they are alphabetically larger and guaranteed to show up again later
            while stack and stack[-1] > curr and last_index[stack[-1]] > i:
                seen.remove(stack.pop())
                
            # Add the current valid character sequence to both tracking containers
            stack.append(curr)
            seen.add(curr)
            
        return "".join(stack)