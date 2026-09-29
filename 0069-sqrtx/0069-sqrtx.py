class Solution:
    def mySqrt(self, x: int) -> int:
        answer = 0
        for i in range(x+1):
            if i * i <=  x:
                answer = i
            else:
                break
        return answer