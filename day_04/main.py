from day_04.grid import Grid


def read_data(filename):
    data = {}
    with open(filename) as f:
        data["order"] = [int(x) for x in f.readline().split(",")]
        grid_lines = f.read().splitlines()
        data["grids"] = []
        grid = []
        for line in grid_lines:
            if line == "":
                if grid:
                    data["grids"].append(grid)
                grid = []
            else:
                grid.append([int(x) for x in line.split()])
        data["grids"].append(grid)

    return data


def main():
    data = read_data("input.txt")

    # Create grids
    grids = []
    for grid_data in data["grids"]:
        grids.append(Grid(grid_data))

    # After each turn, check if a grid has won and store the winning result
    results = []
    for number in data["order"]:
        for grid in grids:
            result = grid.update(number)

            # Check if grid is complete
            if result:
                unmarked_sum = grid.get_unmarked_sum()
                results.append(unmarked_sum * number)

    print(int(results[0]))
    print(int(results[-1]))


if __name__ == "__main__":
    main()
