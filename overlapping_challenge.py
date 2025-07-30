# Word Overlapping

def overlap(word1, word2):
    max_overlap = 0
    # Checks for the longest match between word1 and word2
    for i in range(1, min(len(word1), len(word2)) + 1):
        if word1.lower()[-i:] == word2.lower()[:i]:
            max_overlap = i
    return word1.lower() + word2[max_overlap:].lower()


print(overlap("sweden", "denmark"))
# output = "swedenmark"

print(overlap("honey", "milk"))
# output = "honeymilk"

print(overlap("dodge", "dodge"))
# output = "dodge"
