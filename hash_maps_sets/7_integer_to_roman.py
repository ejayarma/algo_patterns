class Solution:
    def intToRoman(self, num: int) -> str:
        
        numerals = {
            1000: 'M',
            900 : 'CM',
            500 : 'D',
            400 : 'CD',
            100 : 'C',
            90 : 'XC',
            50  : 'L',
            40  : 'XL',
            10  : 'X',
            9  : 'IX',
            5   : 'V',
            4   : 'IV',
            1   : 'I',
        }
        
        roman_digits = []
        remainder = num
        for (k, v) in numerals.items():
            if remainder > 0:
                place_digit = (remainder // k)
                remainder -= place_digit * k
                roman_digits.append(place_digit * v)
            
                print('remainder', remainder, 'place_digit', place_digit, 'place_value', place_digit * k, 'roman_digit', place_digit * v)
            
        return ''.join(roman_digits)
            

solve = Solution()
print(solve.intToRoman(3749))