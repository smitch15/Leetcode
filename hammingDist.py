def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    count = 0
    while (x != 0 or y != 0):
        if (x&1 ^ y&1):
            count += 1
        x >>= 1
        y >>= 1
    return count

def main():
    print(hammingDistance(15, 0))

main()