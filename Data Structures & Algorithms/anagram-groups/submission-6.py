class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in range(len(strs)):
            count = [0] * 26
            for j in range(len(strs[i])):
                count[ord(strs[i][j]) - ord('a')] += 1
            # abc = [1,1,1,0,...,0]
            key = tuple(count)
            if key not in seen:
                seen[key] = []
            seen[key].append(strs[i])
        
        res = []
        for value in seen.values():
            res.append(value)
        
        return res