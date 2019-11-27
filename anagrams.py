#  Given a word W and a string S, find all starting indices in S which are anagrams of W.
## For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.

import string
def ana_indexes(W, S):  # W 'ab', S 'abxaba'

    def counts_eqv(counts1, counts2):
        # letter counts is finite length, so constant time comparison
        return list(sorted(counts1.items())) == list(sorted(counts2.items()))

    Scounts = {let: 0 for let in string.ascii_lowercase}
    Wcounts = {let: 0 for let in string.ascii_lowercase}
    for let in W:
        Wcounts[let] += 1

    endindex = len(S) - 1
    windows_len = len(W)
    indexes = []

    # We can do this in O( n ) time by working backward,
    # and maintaing a letter count for each backward sliding window

    while endindex >= 0:

        if endindex <= ((len(S) - 1) - windows_len):
            Scounts[S[endindex]] += 1
            Scounts[S[endindex + windows_len]] -= 1

            if counts_eqv(Scounts, Wcounts):
                indexes.append(endindex)

        # When we have enough letters going backward, thats when we start comparing
        elif endindex == ((len(S) - 1) - (windows_len - 1)):
            Scounts[S[endindex]] += 1
            if counts_eqv(Scounts, Wcounts):
                indexes.append(endindex)

        # We still dont' have enough letters
        else:
            Scounts[S[endindex]] += 1

        endindex -= 1

    return indexes

assert ana_indexes("ab", "abxaba") == [4, 3, 0]




