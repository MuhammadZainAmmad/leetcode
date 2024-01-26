class Solution(object):
    # from editorial tab
    """
    Time complexity: O(m+n)O(m + n)O(m+n)
    We need to compare the two concatenations of length O(m+n)O(m + n)O(m+n), it takes O(m+n)O(m + n)O(m+n) time.
    We calculate the GCD using binary Euclidean algorithm, it takes log⁡(m⋅n)\log(m \cdot n)log(m⋅n) time.
    To sum up, the overall time complexity is O(m+n)O(m + n)O(m+n).
    Space complexity: O(m+n)O(m + n)O(m+n)
    We need to compare the two concatenations of length O(m+n)O(m + n)O(m+n).
    """
    def gcdOfStrings(self, str1, str2): # Euclidean algorithm for GCD
        def computeGCD(x, y):
            while(y):
                x, y = y, x % y
            return abs(x)

        if str1 + str2 != str2 + str1:
            return ''
        max_len = computeGCD(len(str1), len(str2))
        return str1[:max_len]