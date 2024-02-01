# # MyApproach
# # Time: O(n)
# # Space: O(n)
# class Solution(object):
#     def reverseWords(self, s):
#         list_s = s.split() # string to list
#         reverse_s = ''
#         while len(list_without_space) > 1: # pop from list until 1 element
#             reverse_s += list_without_space.pop() + ' '
#         return reverse_s + list_without_space.pop() # pop the last (first) element

# From soluion tab (better than previous)
# Time: O(n)
# Space: O(1)
class Solution(object):
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])

# # From soluion tab 
# # Time: O(n)
# # Space: O(1)
# class Solution(object):
#     def reverseWords(self, s):
#         return ' '.join(reversed(s.split()))