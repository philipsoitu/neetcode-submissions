class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        occurences_of_zero = 0

        for x in nums:
            if x == 0:
                occurences_of_zero += 1
            else:
                prod *= x
        
        if occurences_of_zero == 0:
            return [prod//x for x in nums]
        elif occurences_of_zero == 1:
            return [prod if x == 0 else 0 for x in nums]
        else:
            return [0 for x in nums]
        