from typing import List

N = 6
D = [1, 2, 3, 3, 2, 1]
K = 1
def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    # Write your code here
    window = {}
    eatenCounter = 0
    for i in range(N):
        # print(D[i])

        if not D[i] in window or (eatenCounter - window[D[i]]) > K:
            window[D[i]] = eatenCounter
            # print(window)
            eatenCounter +=1
        else: print("Eaten",D[i])

    return eatenCounter

print(getMaximumEatenDishCount(N,D,K))

