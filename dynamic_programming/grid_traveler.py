def grid_traveler(m, n, memo={}):
    if m <= 0 or n <= 0:
        return 0

    if m == 1 and n == 1:
        return 1

    coordinate = str(m) + ',' + str(n)

    if coordinate in memo:
        return memo[coordinate]

    memo[coordinate] = grid_traveler(m - 1, n, memo) + grid_traveler(m, n - 1, memo)

    return memo[coordinate]


print(grid_traveler(2, 3))
print(grid_traveler(18, 18))
