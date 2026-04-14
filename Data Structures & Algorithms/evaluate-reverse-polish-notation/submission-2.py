class Solution:
	def evalRPN(self, tokens: List[str]) -> int:
		stack = []
		ops = ['+', '-', '/', '*']
		for e in tokens:
			if e not in ops:
				stack.append(int(e))
			else:
				# print(stack)
				first, second = stack.pop(), stack.pop()
				# print(second, first)
				if e == "+":
					stack.append(second + first)
				elif e == '-':
					stack.append(second - first)
				elif e == '*':
					stack.append(second * first)
				else:
					stack.append(int(second / first))

		return int( stack.pop())