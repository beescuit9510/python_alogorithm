def can_construct(target, word_bank, memo={}):
    if target in memo:
        return memo[target]

    if target == '':
        return True

    for word in word_bank:

        if target.startswith(word):
            new_target = target.replace(word, "", 1)

            if can_construct(new_target, word_bank, memo):
                memo[target] = True
                return memo[target]

    memo[target] = False

    return memo[target]


print(can_construct("target", ["ta", "r", "r", "tar", "get"]))
print(
    can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]))
