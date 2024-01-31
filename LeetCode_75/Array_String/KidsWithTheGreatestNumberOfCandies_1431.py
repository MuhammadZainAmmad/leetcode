class Solution(object):
    # my_sol: O(n), O(1)
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]