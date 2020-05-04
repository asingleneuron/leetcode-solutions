class Solution:

    def findComplement(self, num: int) -> int:
        '''

        :param num:
        :return: num

        Example:
            num = 5

            int("".join(map(lambda x: '0' if x == '1' else '1', bin(num)[2:])), 2)

            breakup of one-liner

            binary_bits = bin(num)[2:]  # Convert number to ints binary representation.

            rev_bits = ''.jon(map(lambda x: '0' if x == '1' else '1' , binary_bits)  # Reversing 1 and 0

            int(rev_bits, 2)    # Converting binary representation to decimal

        '''
        return int("".join(map(lambda x: '0' if x == '1' else '1', bin(num)[2:])), 2)

