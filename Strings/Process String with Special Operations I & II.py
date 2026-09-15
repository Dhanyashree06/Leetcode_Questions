# 3612. Process String with Special Operations I

class Solution:
    def processStr(self, s):
        result = ""

        for ch in s:
            if 'a' <= ch <= 'z':
                result += ch
            elif ch == '*':
                if result:
                    result = result[:-1]
            elif ch == '#':
                result += result
            elif ch == '%':
                result = result[::-1]

        return result


#3614. Process String with Special Operations II

class Solution:
    def processStr(self, s, k):
        lengths = []
        cur_len = 0

        for ch in s:
            if 'a' <= ch <= 'z':
                cur_len += 1
            elif ch == '*':
                if cur_len > 0:
                    cur_len -= 1
            elif ch == '#':
                cur_len *= 2
            elif ch == '%':
                pass

            lengths.append(cur_len)

        if k >= cur_len:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            prev_len = lengths[i - 1] if i > 0 else 0

            if 'a' <= ch <= 'z':
                if k == prev_len:
                    return ch

            elif ch == '*':
                # Before '*' the string had one extra character.
                pass

            elif ch == '#':
                if k >= prev_len:
                    k -= prev_len

            elif ch == '%':
                k = prev_len - 1 - k

        return '.'
