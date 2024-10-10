maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

n = len(maze)
m = len(maze[0])

solution = (4, 0)

start = (0, 0)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def maze_func(x, y, solution):
    if (x, y) == solution:
        return True

    maze[x][y] = 1

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 0:
            if maze_func(nx, ny, solution):
                return True

    maze[x][y] = 0

    return False

found_path = maze_func(start[0], start[1], solution)

print("Path found:", found_path)
