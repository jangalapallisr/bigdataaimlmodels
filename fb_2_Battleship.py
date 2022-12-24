from typing import List
def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    print(sum(sum(G,[])))
    return (sum(sum(G,[]))/(R*C))

if __name__ =='__main__':
    R = 2
    C = 3
    G = [[0, 0, 1],[1, 0, 1]]
    print(getHitProbability(R, C, G))
    R = 2
    C = 2
    G = [[1, 1],[1, 1]]
    print(getHitProbability(R, C, G))