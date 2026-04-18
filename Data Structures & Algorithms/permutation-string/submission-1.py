# Input: s1 = "abc", s2 = "lecabee"
class Solution:
	def checkInclusion(self, s1: str, s2: str) -> bool:
		freq_map = defaultdict(int)
		l = 0
		if len(s1) > len(s2):
			return False

		s1_len = len(s1)
		s1_map = defaultdict(int)
		for i in range(len(s1)):
			s1_map[s1[i]] += 1

		for r in range(len(s2)):
			freq_map[s2[r]] += 1

			result = True
			for let, cnt in s1_map.items():
				result = result & (cnt == freq_map[let])
			if result:
				return True
			if r - l + 1 == s1_len:
				freq_map[s2[l]] -= 1
				l += 1
		return False