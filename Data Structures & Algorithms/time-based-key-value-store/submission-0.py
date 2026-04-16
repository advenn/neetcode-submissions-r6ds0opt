from collections import defaultdict


class TimeMap:

	def __init__(self):
		self.lookup = defaultdict(list)

	def set(self, key: str, value: str, timestamp: int) -> None:
		self.lookup[key].append((timestamp, value))

	def get(self, key: str, timestamp: int) -> str:
		lookup_arr = self.lookup.get(key)
		if not (lookup_arr) :
			return ""

		l, r = 0, len(lookup_arr) - 1
		candidate = None
		while l <= r:
			mid = (l + r) // 2
			if timestamp == lookup_arr[mid][0]:
				return lookup_arr[mid][1]

			if timestamp > lookup_arr[mid][0]:
				l = mid + 1
				candidate = lookup_arr[mid]

			else:
				r = mid - 1
		if candidate:
			return candidate[-1]
		return ""
