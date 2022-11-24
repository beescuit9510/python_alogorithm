def can_sum(target_sum, numbers, memo={}) -> bool:
    if target_sum in memo:
        return memo[target_sum]

    if target_sum == 0:
        return True

    if target_sum < 0:
        return False

    for at in range(0, len(numbers)):
        remainder = target_sum - numbers[at]

        if can_sum(remainder, numbers, memo):
            memo[remainder] = True
            return True

    return False


print(can_sum(8, [3, 3, 10, 11, 2, 1]))
# print(can_sum(18, 18))
