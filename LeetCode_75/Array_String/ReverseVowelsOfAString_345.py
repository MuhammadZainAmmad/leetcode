# # MyImplementation
# # Time: O(n)
# # Space: O(n)
# class Solution(object):
#     def reverseVowels(self, s):
#         vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
#         s_vowels = []
#         for idx in range(len(s)): # O(n)
#             if s[idx] in vowels: # O(1)
#                 s_vowels.append(s[idx])
#                 s = s[:idx] + '_' + s[idx+1:]
#         for idx in range(len(s)): # O(n)
#             if s[idx] == '_':
#                 s = s[:idx] + s_vowels.pop() + s[idx+1:]
#         return s

# From sol tab: two pointer 
# Time O(n)
# Space O(n)
# much faster than my approach
class Solution(object):
    def reverseVowels(self, s):
        # Convert the input string to a character array.
        word = list(s)
        start = 0
        end = len(s) - 1
        vowels = "aeiouAEIOU"
        
        # Loop until the start pointer is no longer less than the end pointer.
        while start < end:
            # Move the start pointer towards the end until it points to a vowel.
            while start < end and vowels.find(word[start]) == -1:
                start += 1
            
            # Move the end pointer towards the start until it points to a vowel.
            while start < end and vowels.find(word[end]) == -1:
                end -= 1
            
            # Swap the vowels found at the start and end positions.
            word[start], word[end] = word[end], word[start]
            
            # Move the pointers towards each other for the next iteration.
            start += 1
            end -= 1
        
        # Convert the character array back to a string and return the result.
        return "".join(word)