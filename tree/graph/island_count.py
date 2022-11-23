def island_count(grid):
    island_count = 0

    row_end = len(grid)
    start = 0
    visited = set()

    def explore(row_index, col_index):
        key = str(row_index) + "," + str(col_index)

        if key in visited:
            return False

        if row_index < 0 or col_index < 0 or row_index > row_end-1 or col_index > len(grid[row_index])-1:
            return False

        target = grid[row_index][col_index]
        visited.add(key)

        if target == 'W':
            return False

        explore(row_index - 1, col_index)
        explore(row_index + 1, col_index)
        explore(row_index, col_index - 1)
        explore(row_index, col_index + 1)

        return True

    for row_index in range(start, row_end):
        col_end = len(grid[row_index])

        for col_index in range(start, col_end):
            if explore(row_index, col_index):
                island_count += 1

    return island_count

grid = [
['L','W','W','W','W','W'],
['L','W','W','W','L','W'],
['L','W','W','W','W','L'],
['L','W','W','W','L','L'],
['L','W','W','W','W','W'],
['L','W','W','W','W','W'],
['L','W','W','W','W','W']
]

print(island_count(grid))