class Solution:
    def singleNonDuplicate_with_Xor(self, nums: List[int]) -> int:
        result = 0
        for _ in nums:
            result ^= _
        return result

    def singleNonDuplicateUtil(self, nums, low, high):
        if low >= high:
            # print(low, high)
            return nums[high]
        else:
            mid = (low + high) // 2
            if mid % 2 == 0:
                mid -= 1
            # print( nums[mid-1], nums[mid], nums[mid+1])
            # print("lmh:",low, mid, high)
            if (nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]):
                # print("Found")
                return nums[mid]
            else:
                if nums[mid] == nums[mid + 1]:
                    return self.singleNonDuplicateUtil(nums, low, mid - 1)
                else:
                    return self.singleNonDuplicateUtil(nums, mid + 1, high)

    def singleNonDuplicate_rec(self, nums: List[int]) -> int:
        return self.singleNonDuplicateUtil(nums, 0, len(nums) - 1)

    def singleNonDuplicate_iterative(self, nums: List[int]) -> int:
        '''
            [1, 2, 2, 6, 6, 7, 7]

            mid is 3
            nums[mid-1], nums[mid], nums[mid+1]
            2, 6, 6 if mid and mid+1 are same, single non duplicate will be on left side else right side

            [1, 2, 2, 6, 6]
            mid is 2 : even index
            nums[mid-1], nums[mid], nums[mid+1]
            2, 2, 6 our logic got reversed here so we deduct -1 from mid
            new mid will be 1
            1, 2, 2 will fit into our logic of identifying the single non duplicate number
        '''
        low = 0
        high = len(nums) - 1
        ans = -1
        while low < high:

            mid = (low + high) // 2
            # print(low, high, mid)
            if mid % 2 == 0:  # if mid index is even, shift
                mid -= 1

            if nums[mid - 1] < nums[mid] and nums[mid] < nums[mid + 1]:
                ans = mid
                return nums[ans]
            else:
                if nums[mid] == nums[mid + 1]:
                    high = mid - 1
                else:
                    low = mid + 1

        return nums[high]

    def singleNonDuplicate(self, nums: List[int]) -> int:
        self.singleNonDuplicate_iterative(nums)
