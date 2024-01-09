# MySol: O(n), O(n)
# class Solution(object):
#     def mergeAlternately(self, word1, word2):
#         len_word1 = len(word1)
#         len_word2 = len(word2)
#         if len_word1 > len_word2:
#             loop_bound = len_word1
#         else:
#             loop_bound = len_word2
        
#         merged_str = ''
#         for i in range(loop_bound):
#             if i < len_word1:
#                 merged_str += word1[i]
#             if i < len_word2:
#                 merged_str += word2[i]
#         return merged_str

# From solution tab: O(n), O(n)
# class Solution(object):
#     def mergeAlternately(self, word1, word2):
#         len_word1 = len(word1)
#         len_word2 = len(word2)
#         merged_str = '' 
#         i = 0
#         while i < len_word1 or i < len_word2:
#             if i < len_word1:
#                 merged_str += word1[i]
#             if i < len_word2:
#                 merged_str += word2[i]
#             i += 1
#         return merged_str