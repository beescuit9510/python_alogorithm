def island_count(grid):
    minimum_island = float('inf')

    row_end = len(grid)
    start = 0
    visited = set()

    def explore(row_index, col_index):
        key = str(row_index) + "," + str(col_index)

        if key in visited:
            return 0

        if row_index < 0 or col_index < 0 or row_index > row_end - 1 or col_index > len(grid[row_index]) - 1:
            return 0

        target = grid[row_index][col_index]
        visited.add(key)

        if target == 'W':
            return 0

        top = explore(row_index - 1, col_index)
        left = explore(row_index, col_index - 1)
        bottom = explore(row_index + 1, col_index)
        right = explore(row_index, col_index + 1)
        island_size = top + left + bottom + right + 1

        return island_size

    for row_index in range(start, row_end):
        col_end = len(grid[row_index])

        for col_index in range(start, col_end):
            island_size = explore(row_index, col_index)
            if island_size != 0 and island_size < minimum_island:
                minimum_island = island_size

    return minimum_island


grid = [
    ['L', 'W', 'W', 'W', 'W', 'W'],
    ['L', 'W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'W', 'W', 'L'],
    ['L', 'W', 'W', 'W', 'L', 'L'],
    ['L', 'W', 'W', 'W', 'W', 'W'],
    ['L', 'W', 'W', 'W', 'W', 'W'],
    ['L', 'W', 'W', 'W', 'W', 'W']
]

print(island_count(grid))
