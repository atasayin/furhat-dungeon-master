class Maze:
    def __init__(self, grid, start_point, end_point):
        self.isWin = False
        grid[end_point[0]][end_point[1]] = 2
        self.grid = grid
        self.start_point = start_point
        self.current_point = start_point
        self.end_point = end_point

    def isValid(self, point):
        return self.grid[point[0]][point[1]] != 1

    def move(self, dv):
        move_point = self.current_point[0] + \
            dv[0], self.current_point[1] + dv[1]

        if self.grid[move_point[0]][move_point[1]] == 0:
            print(f"Moved from {self.current_point} to {move_point}")
            self.current_point = move_point
            return True
        elif self.grid[move_point[0]][move_point[1]] == 1:
            print(f"Cannot move from {self.current_point} to {move_point}")
            return False
        elif self.grid[move_point[0]][move_point[1]] == 2:
            self.current_point = move_point
            self.win()
            return True

    def moveLeft(self):
        return self.move((0, -1))

    def moveRight(self):
        return self.move((0, 1))

    def moveUp(self):
        return self.move((-1, 0))

    def moveDown(self):
        return self.move((1, 0))

    def win(self):
        self.isWin = True
        print(f"You have reached the end point at {self.current_point}")

    def hint(self):
        return self.solver()[0]

    def solver(self):
        visited = []
        q = []
        q.append((self.current_point, []))
        visited.append(self.current_point)

        while q:
            cell, path = q.pop(0)
            if self.end_point == cell:
                return path

            for dv in {(0, -1), (0, 1), (1, 0), (-1, 0)}:
                move_point = cell[0] + dv[0], cell[1] + dv[1]

                if self.isValid(move_point) and move_point not in visited:
                    newPath = path.copy()
                    newPath.append(dv)
                    q.append((move_point, newPath))
                    visited.append(move_point)
