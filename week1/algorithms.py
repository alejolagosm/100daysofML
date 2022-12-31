# A functon to check if two words are anagrams of each other
def is_anagram(word1: str, word2: str) -> bool:
  if(len(word1) != len(word2)):
    return False
  max = len(word2)-1
  
  if all(letter == word2[max - idx] for max, letter in enumerate(word1)):
    return True
  
  return False

