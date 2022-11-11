import numpy as np
import math


def read_data(filename):
    with open(filename) as f:
        data = []
        for line in f.read().splitlines():
            data.append([int(char) for char in line])

    return data


def get_low_points(grid):
    low_point_vals = []
    low_points = []
    for i in range(grid.shape[1]):
        for j in range(grid.shape[0]):
            # Check if the point is considered a low point
            x_min = i - 1 if i - 1 >= 0 else None
            x_max = i + 1 if i + 1 < grid.shape[1] else None
            y_min = j - 1 if j - 1 >= 0 else None
            y_max = j + 1 if j + 1 < grid.shape[0] else None
            neighbour_indices = [(x_min, j),
                                 (i, y_min),
                                 (x_max, j),
                                 (i, y_max)]
            neighbour_vals = [grid[y, x] for (x, y) in neighbour_indices if x is not None and y is not None]
            if 0 not in [grid[j, i] < val for val in neighbour_vals]:
                low_point_vals.append(grid[j, i])
                low_points.append((i, j))
    return low_point_vals, low_points


def flood_fill(x, y, grid, visited):
    if x < 0 or x >= grid.shape[1] or y < 0 or y >= grid.shape[0]:
        return
    if (x, y) in visited:
        return
    if grid[y, x] == 9:
        return
    visited.append((x, y))
    flood_fill(x - 1, y, grid, visited)
    flood_fill(x + 1, y, grid, visited)
    flood_fill(x, y - 1, grid, visited)
    flood_fill(x, y + 1, grid, visited)
    return visited


def main():
    grid = np.matrix(read_data("input.txt"))
    low_point_vals, low_points = get_low_points(grid)
    print(sum(low_point_vals) + len(low_point_vals))
    sizes = []
    for low_point in low_points:
        basin = flood_fill(low_point[0], low_point[1], grid, [])
        sizes.append(len(basin))
        sizes.sort(reverse=True)
    print(math.prod(sizes[:3]))


if __name__ == "__main__":
    main()
