import ctypes

class Solution:
    def firstAlphabet(self, S):
        # code here
        lst = S.split(" ")
        char = ''
        for item in lst:

            char += item[0]

        print(lst)
        print(char)

first = Solution()

first.firstAlphabet("my name is amit kumar gautam")