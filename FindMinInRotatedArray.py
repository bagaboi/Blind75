from typing import List
def findMin(nums: List[int]) -> int:
    p1=0
    p2=1
    while p2!=len(nums):
        if nums[p1]>nums[p2]:
            return nums[p2]
        p1+=1
        p2+=1
    return nums[0]
def main():
    # nums=[3,4,5,1,2] # 1
    nums=[4,5,6,7,0,1,2] # 0
    print(findMin(nums))

if __name__ == "__main__":
    main()