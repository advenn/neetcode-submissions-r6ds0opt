class Solution:
	def isPalindrome(self, s: str) -> bool:
		l, r = 0, len(s) - 1
		borders = ((ord("A"), ord("Z")), (ord("a"), ord("z")), (ord("0"), ord("9")))
		while l < r:
			while (l < r) and not any([b[0] <= ord(s[l]) <= b[1] for b in borders]): l += 1
			while (l < r) and not any([b[0] <= ord(s[r]) <= b[1] for b in borders]): r -= 1

			if s[l].lower() == s[r].lower():
				l += 1
				r -= 1
			else:
				return False

		return True
