class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            x_str = str(x)
            n, leng = 1, len(x_str)
            for s in x_str:
                if s == x_str[leng-n]:
                    pass
                else:
                    return False
                n += 1
            return True