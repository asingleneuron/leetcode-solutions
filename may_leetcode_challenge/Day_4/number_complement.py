class Solution:

    def findComplement(self, num: int) -> int:
        return int("".join(map(lambda x: '0' if x == '1' else '1', bin(num)[2:])), 2)

