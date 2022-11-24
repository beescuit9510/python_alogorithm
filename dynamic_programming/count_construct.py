def count_construct(target, word_bank, memo={}):
    if target in memo:
        return memo[target]

    if target == '':
        return 1

    count = 0

    for word in word_bank:

        if target.startswith(word):
            new_target = target.replace(word, "", 1)

            count += count_construct(new_target, word_bank, memo)

    memo[target] = count

    return count


print(count_construct("target", ["ta", "r", "tar", "get"]))
print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                      ["e", "ee", "eee", "eeee", "eeeee"]))
