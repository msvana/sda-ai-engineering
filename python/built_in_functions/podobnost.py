def jaccard_index(text1, text2):
    set1 = set(text1.split())
    set2 = set(text2.split())
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)

text1 = "I love programming in Python"
text2 = "Python programming is fun"

similarity = jaccard_index(text1, text2)
print(similarity)
