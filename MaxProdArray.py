from typing import List
def maxProduct(nums: List[int]) -> int:
        res=max(nums)
        mini =1
        maxi=1
        for i in range(len(nums)):
            temp=maxi*nums[i]
            maxi=max(temp, mini*nums[i], nums[i])
            mini= min(temp, mini *nums[i], nums[i])
            res=max(res,maxi)
        return res

def main():
    # nums=[2,3,-2,4] # 6
    nums=[-2,-3,-4] # 12
    print(maxProduct(nums))

if __name__ == "__main__":
    main()