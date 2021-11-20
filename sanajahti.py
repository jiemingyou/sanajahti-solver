from collections import deque


class Game:
    '''
    A class representing the game board.
    Contains tiles.
    '''
    def __init__(self, tiles: list, words):
        self.words = words
        self.tiles = tiles
        self.makeboard()
    
    _tiles = []

    def makeboard(self):
        for i in range(0, 16, 4):
            self._tiles.append(
                self.tiles[i:i+4]
            )

    def __call__(self, x: int, y: int):
        if (0 <= x < 4 and 0 <= y < 4):
            return self._tiles[x][y]

    def __repr__(self):
        for row in self._tiles:
            print("  ".join(row).upper())
        return ""

    def next(self, x: int, y: int):

        def check(a: int, b: int) -> bool:
            return (0 <= a < 4 and 0 <= b < 4)

        dir = [(x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1),(x+1, y), (x-1, y), (x, y+1), (x, y-1) ]
        values = [((i, j), (self._tiles[i][j])) for (i,j) in dir if check(i, j)]
        return values
        
        
    def solve(self):
        ans = []
        
        def dfs(x: int, y: int, curr: str, wordsleft: set):
            if (x,y) in visited:
                return
            visited.append((x,y))

            remaining = {i for i in wordsleft if i.startswith(curr)}

            # No matching words left -> go back one letter
            if not remaining:
                visited.pop()
                return

            # Add current words and add new letter
            if curr in remaining:
                ans.append(curr)

            neighbours = self.next(x, y)
            for (coords, letter) in neighbours:
                dfs(*coords, curr+letter, remaining)
            visited.pop()

        visited = deque()
        for x in range(4):
            for y in range(4):
                dfs(x, y, self._tiles[x][y], self.words)

        return sorted(list(set(ans)), key=len, reverse=True)