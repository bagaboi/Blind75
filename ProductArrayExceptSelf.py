from typing import List
def productExceptSelf(nums: List[int]) -> List[int]:
        answer=[]
        pref=[1] * len(nums)
        suff=[1] * len(nums)
        for i in range(1,len(nums)):
            pref[i]=pref[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            suff[i]=suff[i+1]*nums[i+1]
        for i in range(len(nums)):
            val=pref[i]*suff[i]
            answer.append(val)
        return answer
def main():
    nums=[1,2,3,4]
    # nums=[-1,1,0,-3,3]
    print(productExceptSelf(nums))

if __name__ == "__main__":
    main()