# 13. Roman to Integer

class Solution:
    def romanToInt(self, s):

        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s)):

            # subtract case
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]

            else:
                total += roman[s[i]]

        return total




# 12. Integer to Roman

class Solution:
    def intToRoman(self, num):

        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        result = ""

        for i in range(len(values)):

            while num >= values[i]:
                result += symbols[i]
                num -= values[i]

        return result