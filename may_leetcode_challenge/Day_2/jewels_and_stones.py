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
        '''
            This is faster than naive approach
            We are creating a dictionay which has stones as a key and number of times that stones appears is in the value.
            Assume we have n stones in S, so the time complexity of creating the dictionary will be O (n)
            
            Now we pick each jewel and look for the jewel occurences in dictionary.
            Assume we have m jewels in J, so the time compelxity of finding occurences of all the jewels is O(m)
            
            Overall Time complexity : 
                O (m + n)
                    n and m can have maximum 50 (same number of stones)
                    so m == n, 
                O ( n + n ) 
                O ( 2n )
                
                overall time complexity is O (n)
        '''
        number_of_jewels = 0
        stones_dictionary = {}
        for s in S:
            stones_dictionary[s] = stones_dictionary.setdefault(s, 0) + 1

        for j in J:
            number_of_jewels += stones_dictionary.setdefault(j, 0)
        return number_of_jewels
    

    def numJewelsInStones(self, J: str, S: str) -> int:
        '''
            This is a naive approach. 
            Where we pick one jewel from J and count all of the occurences in S 
            
            Time Complexity : O ( m * n )
            Explanation: 
                Assume m is the number of jewels in J, and n is the number of stones in S
                So will be counting occurences of jewel in S, to count all of the occurences, we need to look for all of the stones 
                starting from index 0 to index n-1. So the time complexity for this will be O (n)
                
                We need to do this m time, because we have m distinct types of jewels. So multiplying m * n
            
        '''        
        number_of_jewels = 0
        for j in J:
            number_of_jewels += S.count(j)

        return number_of_jewels



