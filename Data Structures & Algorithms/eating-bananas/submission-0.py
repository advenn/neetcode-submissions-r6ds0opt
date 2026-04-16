from math import ceil
from typing import List


class Solution:
	def minEatingSpeed(self, piles: List[int], h: int) -> int:
		l, r = 1, max(piles)
		result = r
		while l <= r:
			k = (l + r) // 2
			hours = sum(ceil(pile / k) for pile in piles)
			if hours > h:
				l = k + 1
			elif hours <= h:
				result = k
				r = k - 1

		return result