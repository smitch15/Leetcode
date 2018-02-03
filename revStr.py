"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""

def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    print(s)
    t = ''
    s = list(s)
    if (s == ""):
        return ""
    for i in range(len(s)):
        # print(i)
        first = s[i]
        last = s[len(s)-1-i]
        s[i] = last
        s[len(s)-1-i] = first
        if i >= (len(s)-1)//2:
            break
    t = t.join(s)
    return t

def main():
    print(reverseString("a."))
    print(reverseString("hello"))

main()