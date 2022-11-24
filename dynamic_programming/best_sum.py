def best_sum(target_sum, numbers, memo={}) -> bool:
    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    if target_sum in memo:
        return memo[target_sum]

    least = None

    for number in numbers:
        path = best_sum(target_sum - number, numbers, memo)

        if path is not None:
            path.append(number)

            if least is None or len(least) > len(path):
                least = path

    memo[target_sum] = least

    return least


# print(how_sum(7, [3, 3, 10, 11, 2, 1]))
# print(how_sum(300, [7, 14]))
# print(best_sum(300, [3, 10, 300]))
print(best_sum(7, [5, 3, 4, 7]))
# print(best_sum(15, [5, 3, 10, 300]))
# print(best_sum(300, [7, 14]))
