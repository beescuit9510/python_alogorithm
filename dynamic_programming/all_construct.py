def all_construct(target, word_bank, memo={}):
    if target in memo:
        return memo[target]

    if target == '':
        return [[]]

    all_constructs = []

    for word in word_bank:

        if target.startswith(word):
            suffix = target.replace(word, "", 1)

            suffix_ways = all_construct(suffix, word_bank, memo)

            all_constructs += [way + [word] for way in suffix_ways]

    memo[target] = all_constructs

    return all_constructs


# print(all_construct("aaa", ["a","aaa","aa"]))
# print(all_construct("target", ["ta", "r", "tar", "get"]))
print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(all_construct("aaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa",]))

# print(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
#                       ["e", "ee", "eee", "eeee", "eeeee"]))
