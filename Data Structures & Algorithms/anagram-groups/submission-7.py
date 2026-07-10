class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for wrd in strs:
            count = [0] * 26
            for char in wrd:
                count[ord(char) - ord('a')] += 1
            if (tuple(count) not in groups):
                groups[tuple(count)] = []
            groups[tuple(count)].append(wrd)
        
        res = []
        for value in groups.values():
            res.append(value)
        
        return res
