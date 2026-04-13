class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [0] * len(nums)
        answer = 1
        count = 0
        for i, num in enumerate(nums):
            if num!=0:
                answer = answer * num
            if num == 0:
                count = count + 1

        for i, num in enumerate(nums):
            if count > 1:
                product[i] = 0
            elif count == 1:
                if num != 0:
                    product[i] = 0
                if num == 0:
                    product[i] = answer
            else:
                product[i] = int(answer / num)
        return product
            
            