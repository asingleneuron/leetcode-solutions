class Solution:

    def checkForSlope(self, coordinates):
        flag = True
        y_diff = coordinates[1][1] - coordinates[0][1]
        x_diff = coordinates[1][0] - coordinates[0][0]

        if x_diff != 0:
            prev_slope = y_diff / x_diff
        else:
            prev_slope = 0

        for i in range(2, len(coordinates)):

            y_diff = coordinates[i][1] - coordinates[i - 1][1]
            x_diff = coordinates[i][0] - coordinates[i - 1][0]
            if x_diff != 0:
                slope = y_diff / x_diff
            else:
                slope = 0

            if prev_slope != slope:
                flag = False
                return flag
        return flag

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        return self.checkForSlope(coordinates)

