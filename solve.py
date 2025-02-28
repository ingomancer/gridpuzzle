from time import sleep

puzzle = """\
S.....
XXXXXX
X.X..X
X.XXXX
X.X..X
X....M
X....X
XXXXXX
"""

visited = {}

def main():
    grid = {}
    start_pos = None
    end_pos = None
    move = 0
    moves = [1, 2, 3]
    for y, line in enumerate(puzzle.splitlines()):
        for x, char in enumerate(line):
            grid[(x, y)] = char
            if char == "S":
                start_pos = (x, y)
            if char == "M":
                end_pos = (x, y)

    solution = solve(grid, start_pos, end_pos, move, moves)
    for pos in solution:
        print_grid_with_pos(grid, pos)
        print()
    print(solution)
    print(len(solution))


def solve(grid, pos, end_pos, move, moves):
    step = moves[move % 3]
    if (pos, step) in visited:
        if visited[(pos, step)] <= move:
            return None
        else:
            visited[(pos, step)] = move
    if pos == end_pos:
        return [pos]
    visited[(pos, step)] = move
    shortest_solve = None
    for neighbour in get_moves(pos, grid, step):
        poslist = solve(grid, neighbour, end_pos, move + 1, moves)
        if poslist is not None:
            if shortest_solve is None:
                shortest_solve = poslist
            elif len(shortest_solve) > len(poslist):
                shortest_solve = poslist
    if shortest_solve is None:
        return None
    else: 
        return [pos] + shortest_solve



def print_grid_with_pos(grid, pos):
    for y in range(8):
        for x in range(6):
            if (x, y) == pos:
                print("O", end="")
            else:
                print(grid[(x, y)], end="")
        print()


def get_moves(pos, grid, step):
    x, y = pos
    neighbours = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        neighbour = (x, y)
        for i in range(step):
            neighbour = (neighbour[0] + dx, neighbour[1] + dy)
            if neighbour in grid and grid[neighbour] != ".":
                continue
            else:
                break
        else:
            neighbours.append(neighbour)
    return neighbours


if __name__ == "__main__":
    main()
