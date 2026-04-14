class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagrams = defaultdict(list)

        for index, string in enumerate(strs):
            anagrams[tuple(sorted(string))].append(index)

        for anagram, elems in anagrams.items():
            for elem_index, strs_index in enumerate(elems):
                elems[elem_index] = strs[strs_index]

        return list(anagrams.values())
        