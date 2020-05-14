class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        modified = 0
        for i in range(k):
            # print("digit:",i)
            # print(i,num)

            if len(num) > 1:
                j = 1
                while j < len(num) and num[j] >= num[j - 1]:
                    # print(j-1, j)
                    j += 1

                if j > 1:
                    j -= 1
                    num = num.replace(num[j], '', 1)
                    # print(num)
                    modified += 1
                    # break
                elif num[0] > num[j]:
                    num = num.replace(num[0], '', 1)
                    # print(num)
                    modified += 1

                    # break
            else:
                num = ""

        if k - modified:
            num = num[: len(num) - (k - modified)]

        if len(num):
            return str(int(num))
        else:
            return "0"