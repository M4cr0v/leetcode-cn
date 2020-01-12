class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        length = len(s)
        left = 0
        right = 0
        max_length = 0
        while True:
            # Move the right flag
            while right < length and s[right] not in d:
                d[s[right]] = right
                right += 1
            max_length = max(max_length, right - left)
            if right >= length:
                break
            # Move the left flag
            new_left = d[s[right]] + 1
            for i in xrange(left, new_left):
                d.pop(s[i])
            left = new_left
        return max_length
