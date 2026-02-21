'''
Group Anagrams:
    Anagrams are words that contain the exact same letters in a different order.
    This function takes a list of words and groups all anagrams together.
'''


from collections import defaultdict
# defaultdict(list) --> automatically creates an empty list for any new key.

def group_anagrams(words: list[str]) -> list[list[str]]:
    anagram_map = defaultdict(list)

    for word in words:
        key = tuple(sorted(word))
        anagram_map[key].append(word)

    return list(anagram_map.values())
    
# Example:
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(words)
print(result)
