def overlap(word1, word2):
    if not word1:  # If first word is empty, return the second word
        return word2
    elif not word2:  # If second word is empty, return the first word
        return word1
    word1,word2 = word1.lower(), word2.lower()
    
    if word1 == word2:  # If both words are identical, return either word
        return word1
    elif word2[0] in word1:  # If first character of word2 is not in word1, concatenate words
        start = word1.index(word2[0])
        if word1[start:] == word2[:len(word1[start:])]:  # If end of word1 matches start of word2
            return word1[:start]+word2
    return word1 + word2


# ============TESTS===========#
# my tester function does not #
# account for theese types of #
#          tests D:           #

print("testing - ",overlap("sweden", "denmark"))

print("testing - ",overlap("honey", "milk"))

print("testing - ",overlap("dodge", "dodge"))

print("testing - ",overlap("Maniquen", "English"))

print("testing - ",overlap("somebody", "mebody"))
