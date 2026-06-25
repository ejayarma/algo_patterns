class Solution:
    def romanToInt(self, s: str) -> int:
        
        numerals = {
            'M'  :  1000,
            'CM' :  900 ,
            'D'  :  500 ,
            'CD' :  400 ,
            'C'  :  100 ,
            'XC' :  90  ,
            'L'  :  50  ,
            'XL' :  40  ,
            'X'  :  10  ,
            'IX' :  9   ,
            'V'  :  5   ,
            'IV' :  4   ,
            'I'  :  1   ,
        }
        
        left = 0
        num = 0
        for (k, v) in numerals.items():
            if left < len(s) and k.startswith(s[left]):
                while s[left:left + len(k)] == k:
                    num += v
                    left += len(k)
        return  num
    
solve = Solution()
print(solve.romanToInt('I'))
print(solve.romanToInt('IV'))
print(solve.romanToInt('III'))
print(solve.romanToInt('LVIII'))
print(solve.romanToInt('MCMXCIV'))