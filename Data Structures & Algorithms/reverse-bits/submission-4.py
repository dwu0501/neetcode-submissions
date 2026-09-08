class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        n = bin(n)
        for i in range (len(n)-1, 1, -1):
            if(int(n[i]) & 1):
                res |= (1 << (i))
        res = res << 32 - (len(n)-2)
        res = res >> 2
        return res
        