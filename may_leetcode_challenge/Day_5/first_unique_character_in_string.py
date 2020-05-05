class Solution:
    def firstUniqChar_naive(self, s: str) -> int:
        '''

        :param s: string that contains lowercase characters
        :return: index of first non repeating character

        Naive approach
        Time Complexity : O(n^2)
        '''
        for i, l in enumerate(s):
            if s.count(l) == 1:
                return i
        return -1

    def firstUniqChar_using_dict(self, s: str) -> int:
        '''

        :param s: string that contains lowercae characters
        :return: index of first non repeating character

        Create dictionary , character as key and number of times that character appears as value
        return the index of first character that has count 1

        Time Complexity: O(n)
        '''
        count = collections.Counter(s)

        for k, v in count.items():
            if v == 1:
                return s.index(k)
        return -1

    def firstUniqChar(self, s: str) -> int:
        return self.firstUniqChar_using_dict(s)