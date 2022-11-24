def how_sum(target_sum, numbers, memo={}) -> bool:
    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    if target_sum in memo:
        return memo[target_sum]

    for number in numbers:
        remainder = target_sum - number

        path = how_sum(remainder, numbers, memo)

        if path is not None:
            path.append(number)
            memo[target_sum] = path

            return memo[target_sum]

    memo[target_sum] = None

    return None


# print(how_sum(7, [3, 3, 10, 11, 2, 1]))
# print(how_sum(300, [7, 14]))
print(how_sum(15, [5, 3, 10, 300]))
# print(how_sum(300, [300]))
# print(how_sum(300, [7, 14]))

