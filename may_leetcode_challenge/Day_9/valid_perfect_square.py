class Solution:
    def naive_isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        else:
            digits = len(str(num))
            biggest_number = int('9' * ((digits // 2) + 1)) if digits > 1 else num // 2
            for i in range(biggest_number, 0, -1):
                if i * i == num:
                    return True
                elif i * i < num:
                    return False
            return False

    def isPerfectSquare(self, num: int) -> bool:
        return self.naive_isPerfectSquare(num)

