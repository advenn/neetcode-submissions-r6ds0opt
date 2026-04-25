class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        string: "ababd"

        :param s:
        :return:
        """
        if not s:
            return ""

        p1, p2 = 0, 0
        longest = [0, 0]
        while p1 >= 0 and p2 < len(s):
            start, end = p1, p2
            # print(f"{p1 = }, {p2 = } {start = } {end = }  {start >= 0 and end < len(s)}")

            if s[p1] == s[p2]:


                while start >= 0 and end < len(s):
                    # print(f"{p1 = }, {p2 = } {start = } {end = } {longest = }")
                    if s[start] == s[end]:
                        if end - start >= longest[1] - longest[0]:
                            longest = [start, end+1]

                        start -= 1
                        end += 1

                    else:
                        break

            if p1 == p2:
                p2 += 1
            else:
                p1 = p2

        return s[longest[0]: longest[1]]