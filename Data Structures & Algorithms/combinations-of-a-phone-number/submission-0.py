
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Input: digits = "34"

        Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
        :param digits:
        :return:
        """
        if not digits:
            return []
        letters = {
            '2': set("abc"),
            '3': set("def"),
            '4': set("ghi"),
            '5': set("jkl"),
            '6': set("mno"),
            '7': set("pqrs"),
            '8': set("tuv"),
            '9': set("wxyz")
        }

        answer = []

        def backtrack(current: list, num_pointer: int):
            if len(current) == len(digits):
                answer.append("".join(current))
                return

            for letter in letters[digits[num_pointer]]:
                current.append(letter)
                backtrack(current, num_pointer + 1)
                current.pop()

        backtrack([], 0)
        return answer
