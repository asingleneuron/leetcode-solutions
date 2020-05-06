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
            Go through the list and see if current number and current+ len(nums)/2 are same if yes we got the majority
            element.

        Time complexity: O (nlogn)
        '''


        half = len(nums) // 2
        nums = sorted(nums)
        # print(nums)
        for i in range(0, half + 1):
            # print(i,i+half,nums[i],nums[i+half])
            if nums[i] == nums[i + half]:
                return nums[i]

    def majorityElement(self, nums: List[int]) -> int:
        return self.majorityElement_using_counter(nums)
        #return self.majorityElement_with_sorting(nums)
