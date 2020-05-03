from collections import Counter

class Solution:

    def canConstruct_using_single_dictionary(self, ransomNote: str, magazine: str) -> bool:
        '''

        :param ransomNote: string contains lowercase from a - z
        :param magazine: string contains lowercase from a - z
        :return: true/false

        Time complexity : O (n)
            Assume magazine has n letters and ransomNote has m letters
            T1 (time_complexity of creating dictionary of magazine letters) = O (n)
            T2 (one for loop for checking rnote construction) = O (m)

            T = T1 + T2
              = O(n) + O(m)
              = O(n) + O(n) if m==n
              = O(2n)

            T = O (n)
        '''

        magazine_dict = {}
        for _ in magazine:
            magazine_dict[_] = magazine_dict.setdefault(_, 0) + 1

        for rnote in ransomNote:
            if magazine_dict.setdefault(rnote, 0) - 1 < 0:
                return False
            else:
                magazine_dict[rnote] -= 1

        return True

    def canConstruct_using_two_dictionaries(self, ransomNote: str, magazine: str) -> bool:
        '''

        :param ransomNote: string contains lowercase from a - z
        :param magazine: string contains lowercase from a - z
        :return: true/false

        Time Complexity : O(n)

        '''

        ransom_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)
        # print(ransom_counter)
        # print(magazine_counter)

        for k,v in ransom_counter.items():
            if magazine_counter[k] < v:
                return False

        return True


    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        return self.canConstruct_using_two_dictionaries(ransomNote, magazine)
        # return self.canConstruct_using_single_dictionary(ransomNote, magazine)