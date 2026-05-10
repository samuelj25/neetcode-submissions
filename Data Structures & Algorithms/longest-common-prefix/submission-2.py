class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        for i in range(len(strs[0])): # loop through first word's char
            comp = strs[0][:i + 1]
            for word in strs[1:]: # loop through rest of words
                if word[:i + 1] != comp:
                    return comp[:i]
            ret = comp
        return ret