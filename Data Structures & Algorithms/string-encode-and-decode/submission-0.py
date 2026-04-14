class Solution:

	def encode(self, strs: List[str]) -> str:
		"""Encodes a list of strings to a single string.
		layout: length#string
		"""

		resp = ""
		for word in strs:
			resp += f"{len(word)}#{word}"
		return resp

	def decode(self, s: str) -> List[str]:
		"""Decodes a single string to a list of strings.
		layout: 5#Hello5#World
		"""
		resp = []
		while s:
			length, s = s.split("#", 1)
			length = int(length)
			w = s[:length]
			resp.append(w)
			s = s[length:]
		return resp