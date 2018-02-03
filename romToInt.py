def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    val = 0
    if (s == ""):
        return val
    romToInt = {'I':1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    while (len(s) > 0):
        rem = 1
        first = romToInt[s[0]]
        if (len(s) > 1):
            second = romToInt[s[1]]
            if (second > first):
                rem = 2
                val += second - first
            else:
                val += first
        else:
            val += first
        s[rem:]
    return val

def main():
    romanToInt("X")

main()
