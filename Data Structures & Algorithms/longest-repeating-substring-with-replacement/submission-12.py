class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        l, r = 0, 0
        max_length = 0
        max_freq = 0

        while ((l <= r) and (r < len(s))):
            freq[ord(s[r]) - ord('A')] += 1
            max_freq = max(max_freq, freq[ord(s[r]) - ord('A')])

            if ((r - l + 1) - max_freq <= k):
                max_length = max(max_length, r - l + 1)
            else:
                while ((r - l + 1) - max_freq > k):
                    freq[ord(s[l]) - ord('A')] -= 1
                    l += 1
                    max_freq = max(freq)
            r += 1

        return max_length
