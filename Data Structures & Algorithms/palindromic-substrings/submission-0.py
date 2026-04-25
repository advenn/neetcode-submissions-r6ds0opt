class Solution:
    def countSubstrings(self, s: str) -> int:

        """
        string: "ababd"

        :param s:
        :return:
        """
        if not s:
            return 0

        p1, p2 = 0, 0
        longest = [0, 0]
        seen = list()
        while p1 >= 0 and p2 < len(s):
            start, end = p1, p2

            if s[p1] == s[p2]:

                while start >= 0 and end < len(s):
                    if s[start] == s[end]:
                        seen.append(s[start: end + 1])
                        if end - start >= longest[1] - longest[0]:
                            longest = [start, end + 1]

                        start -= 1
                        end += 1

                    else:
                        break

            if p1 == p2:
                p2 += 1
            else:
                p1 = p2
        return len(seen)
