from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    di={}
    for i in range(len(nums)):
        r=target-nums[i]
        if r in di.keys():
            return [i,di[r]]
        di[nums[i]]=i

def main():
    nums=[2,7,11,5]
    target=9
    print(twoSum(nums,target))

if __name__ == "__main__":
    main()
