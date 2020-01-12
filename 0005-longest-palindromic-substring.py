class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length == 0:
            return ''
        compare = [[0 for x in xrange(0, length)] for x in xrange(0, length)] 
        max_i = 0
        max_j = 0
        max_length = 1
        for i in xrange(0, length):
            compare[i][i] = True
        for i in xrange(0, length-1):
            if s[i] == s[i+1]:
                compare[i][i+1] = True
                if max_length < 2:
                    max_length = 2
                    max_i = i
                    max_j = i + 1
        for i in reversed(xrange(0, length-1)):
            for j in xrange(i+2, length):
                if s[i] == s[j] and compare[i+1][j-1]:
                    compare[i][j] = True
                    if max_length < j - i + 1:
                        max_length = j - i + 1
                        max_i = i
                        max_j = j
        return s[max_i:max_j+1]
