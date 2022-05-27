# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from ctypes.wintypes import WORD
from pickletools import string1
import string


def find_anagram(word,anagram):
   # [assignment] Add your code here
   word = input(" Type your first word:   ")
   anagram = input(" Type your Second word:  ")
   sorted_str1= sorted(word)
   sorted_str2= sorted(anagram)
   if (sorted(word)== sorted(anagram)):
      return True
   else:
      return False
   
print(find_anagram("word","anagram"))





