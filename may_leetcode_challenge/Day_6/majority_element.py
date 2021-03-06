class Solution:
    def majorityElement_using_counter(self, nums: List[int]) -> int:
        '''

        :param nums: list of numbers which contain the majority element
        :return: the majority element

        Majority element is the element which appears more than len(nums)/ 2
        Approach:
            Use counter collection which create a dictionary of numbers as key and number of times it appears as value.
            Look for the key which value is more than len(nums)/2

        Time Complexity: O(n)

        '''

        half = len(nums) // 2
        d = collections.Counter(nums)
        for k, v in d.items():
            if v > half:
                return k

    def majorityElement_with_sorting(self, nums: List[int]) -> int:
        '''

        :param nums: list of numbers which contain the majority element
        :return: the majority element

        Majority element is the element which appears more than len(nums)/ 2

        Approach:
            This approach will use sorting. Sort the nums list in ascending order.
            As we know majority element appears more than len(nums) / 2. So just return nums[len(nums)//2] element.

        Time complexity: O (nlogn)
        '''


        half = len(nums) // 2
        nums.sort()
        return nums[half]

    def majorityElement(self, nums: List[int]) -> int:
        return self.majorityElement_using_counter(nums)
        #return self.majorityElement_with_sorting(nums)
