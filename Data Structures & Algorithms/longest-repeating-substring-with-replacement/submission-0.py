from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        longest = 0
        l = 0
        freq_map = defaultdict(int)

        for r in range(len(s)):
            freq_map[s[r]] += 1
            window_size = r - l + 1
            to_replace = window_size - max(freq_map.values())
            if to_replace <= k:
                longest = max(longest, window_size)
            else:
                freq_map[s[l]] -= 1
                l += 1
        return longest