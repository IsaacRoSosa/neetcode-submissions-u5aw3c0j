from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Iniciamos las variables del diccionario como una lista vacia
        anagram_map = defaultdict(list)
        anagrams = []

        for s in strs:
            orderedString = "".join(sorted(s))
            anagram_map[orderedString].append(s)

        for value in anagram_map.values():
            anagrams.append(value)
        return anagrams
        