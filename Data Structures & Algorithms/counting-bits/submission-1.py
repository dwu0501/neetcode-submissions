class Solution:
    def countBits(self, n: int) -> List[int]:
        def isPower(n: int):
            return n & (n-1) == 0
        if(n == 0): return [0]
        ls = [None]*(n+1)
        ls[0] = 0
        ls[1] = 1
        power = 1
        for i in range(2, n+1):
            if(isPower(i)):
                ls[i] = 1
                power *= 2
            else:
                ls[i] = ls[i-power]+1
        
        return ls



