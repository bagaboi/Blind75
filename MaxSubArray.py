from typing import List
def maxSubArray(nums: List[int]) -> int:
        res=nums[0]
        total=0
        for ele in nums:
            if total<0:
                total=0
            total+=ele
            res=max(res,total)
        return res
def main():
    nums=[-2,1,-3,4,-1,2,1,-5,4] # 6
    # nums=[5,4,-1,7,8] # 23
    print(maxSubArray(nums))

if __name__ == "__main__":
    main()