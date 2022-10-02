class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=[]
        cnt =0
        for i in nums:
            if i!=0:
                l.append(i)
            else:
                cnt+=1
        for i in range(cnt):
            l.append(0)
        
        nums[:] = l[:]
