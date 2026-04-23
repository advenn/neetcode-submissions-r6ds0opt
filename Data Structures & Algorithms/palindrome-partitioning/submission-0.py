class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(sub):
            return sub == sub[::-1]

        result = []

        def backtrack(start, current: list):
            """
            
            :param start:
            :param current:
            :return:
            """
            if start == len(s):
                result.append(current[:])
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    current.append(substring)
                    backtrack(end, current)
                    current.pop()

        backtrack(0, [])
        return result
