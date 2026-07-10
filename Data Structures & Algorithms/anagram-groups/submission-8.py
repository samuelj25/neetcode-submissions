class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for wrd in strs:
            count = [0] * 26
            for char in wrd:
                count[ord(char) - ord('a')] += 1
            groups[tuple(count)].append(wrd)
        
        return list(groups.values())
