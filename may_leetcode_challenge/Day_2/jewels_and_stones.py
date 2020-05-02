'''
Jewels and Stones

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:

Input: J = "z", S = "ZZ"
Output: 0

Note:

    S and J will consist of letters and have length at most 50.
    The characters in J are distinct.


'''


class Solution:
    def numJewelsInStones_using_dict(self, J: str, S: str) -> int:
        # print(S)
        number_of_jewels = 0
        stones_dictionary = {}
        for s in S:
            stones_dictionary[s] = stones_dictionary.setdefault(s, 0) + 1

        for j in J:
            number_of_jewels += stones_dictionary.setdefault(j, 0)
        return number_of_jewels

    def numJewelsInStones(self, J: str, S: str) -> int:
        # print(S)
        number_of_jewels = 0
        for j in J:
            number_of_jewels += S.count(j)

        return number_of_jewels



