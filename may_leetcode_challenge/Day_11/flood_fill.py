class Solution:

    def find_close_pixels(self, source_color, curr_position, image):
        result = []
        ROWS = len(image)
        COLS = len(image[0])

        r = curr_position[0]
        c = curr_position[1]

        if r + 1 < ROWS and c < COLS and image[r + 1][c] == source_color:
            result.append((r + 1, c))

        if r - 1 >= 0 and c < COLS and image[r - 1][c] == source_color:
            result.append((r - 1, c))

        if r < ROWS and c + 1 < COLS and image[r][c + 1] == source_color:
            result.append((r, c + 1))

        if r < ROWS and c - 1 >= 0 and image[r][c - 1] == source_color:
            result.append((r, c - 1))

        return result

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R = len(image)
        C = len(image[0])
        visited = [[False] * C for i in range(R)]

        next_pixel = [(sr, sc)]
        visited[sr][sc] = True

        source_color = image[sr][sc]
        while next_pixel:

            fill_color = next_pixel.pop()
            image[fill_color[0]][fill_color[1]] = newColor

            neighbors = self.find_close_pixels(source_color, fill_color, image)
            for n in neighbors:
                if not visited[n[0]][n[1]]:
                    next_pixel.append(n)
                    visited[n[0]][n[1]] = True

        return image