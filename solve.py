input = """\
.S.......
.XXXXXXX.
.X.X.X.X.
.X.XXX.M.
.X.X...X.
.X.....X.
.XXXXXXX.
........."""

 


def main():
    grid = {}
    visited = {}
    start_pos = None
    end_pos = None
    move = 0
    moves = [1,2,3]
    for y, line in enumerate(input.splitlines()):
        for x, char in enumerate(line):
            grid[(x, y)] = char
            if char == 'S':
                start_pos = (x, y)
            if char == 'M':
                end_pos = (x, y)



    print(solve(grid, start_pos, end_pos, visited, move, moves))
    print(visited)

def solve(grid, pos, end_pos, visited, move, moves):
    step = moves[move%3]
    if (pos, step) in visited:
        return None
    if pos == end_pos:
        return [pos]
    visited[(pos, step)] = True
    for neighbour in get_moves(pos, grid, step):
        poslist = solve(grid, neighbour, end_pos, visited, move+1, moves)
        if poslist is not None:
            return [pos] + poslist
    return None
            
def get_moves(pos, grid, step):
    x, y = pos
    neighbours = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        neighbour = (x, y)
        for i in range(step):
            neighbour = (neighbour[0] + dx, neighbour[1] + dy)
            if neighbour in grid and grid[neighbour] != '.':
                continue
            else:
                break
        else:
            neighbours.append(neighbour)
    return neighbours

            
if __name__ == "__main__":
    main()