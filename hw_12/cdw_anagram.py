def cdw_anagrams(word, words):
    return [ann_ for ann_ in words if sorted(word) == sorted(ann_)]


print(cdw_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
