from typing import List
def maxProfit(prices: List[int]) -> int:
        l=0
        r=1
        maxP=0
        while r<len(prices):
            if prices[l]<prices[r]:
                p=prices[r]-prices[l]
                maxP=max(maxP,p)
            else:
                l=r
            r+=1
        return maxP
def main():
    prices=[7,1,5,3,6,4]
    print(maxProfit(prices))

if __name__ == "__main__":
    main()