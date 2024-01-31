# mySol: 101/129 test cases passed
# failed case: [1,0,0,0,1,0,0]
# class Solution(object):
#     def canPlaceFlowers(self, flowerbed, n):
#         if len(flowerbed) <= 2:
#             return False 
#         for i in range(len(flowerbed)-1):
#             if i == 0 and flowerbed[i] == 0:
#                 flowerbed[i] = 1
#                 n -= 1
#             elif flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
#                 flowerbed[i] = 1
#                 n -= 1
#         return n == 0
            
# Editorial tab: approx same approach but handled first and last element well
# Time complexity: O(n) A single scan of the flowerbedflowerbedflowerbed array of size nnn is done.
# Space complexity: O(1) Constant extra space is used.
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        for i in range(len(flowerbed)):
            # Check if the current plot is empty.
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty.
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    count += 1         
                    if count >= n:
                        return True  
        return count >= n