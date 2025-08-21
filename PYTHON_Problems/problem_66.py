# Given a list of words, group the anagrams together.
# ["eat", "tea", "tan", "ate", "nat", "bat"]
# # Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]



from collections import defaultdict

def group_anagrams(words):
    anagram_map = defaultdict(list)

    for word in words:
        # Sort letters to create a unique key for anagrams
        key = ''.join(sorted(word))
        anagram_map[key].append(word)

    return list(anagram_map.values())


# Test
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))



# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
