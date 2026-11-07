class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        gDict = {}
        for n in hand:
            gDict[n] = gDict.get(n, 0) + 1
        gDict = dict(sorted(gDict.items()))
        
        for index in gDict:
            if(gDict[index] == 0):
                continue
            for i in range(1,groupSize):
                if ((index+i) not in gDict or gDict[index+i] < gDict[index]):
                    return False
                gDict[index+i] -= gDict[index]
                
        return True