# https://my.newtonschool.co/playground/code/yjeryh1ckk6o/

def question():
    return '''Stepstones (Public Contest: August 2022)
    Time Limit: 1 sec
    Memory Limit: 128000 kB
    Problem Statement
    It is a moment of triumph in Stepstones, as they have captured all the ships from Westeros. To celebrate this occasion, they have prepared a problem for you to solve:

    You are given an integer R, and an array A consisting of positive integers. You can do this operation at most once (possibly zero times):
    • Choose any element of the array. Replace it with any integer X, such that 1 ≤ X ≤ R.

    Find the maximum possible GCD of the entire array.
    Input
    The first line consists of two space-separated integers N and R.
    The second line consists of N space-separated integers – A1, A2 ... AN.

    Constraints:
    2 ≤ N ≤ 105
    1 ≤ R ≤ 105
    1 ≤ Ai ≤ 105
    Output
    Print a single integer – the maximum possible GCD of the array.
    Example
    Sample Input 1:
    3 10
    2 3 4

    Sample Output 1:
    2

    Sample Explanation 1:
    We can change the second element from 3 to 2. Then the GCD of the array becomes gcd(2, 2, 4) = 2, which is the maximum possible.

    Sample Input 2:
    2 3
    10 15

    Sample Output 2:
    5

    Sample Explanation 2:
    We do need to perform any operation. The GCD of the array is gcd(10, 15) = 5, which is the maximum possible.

    Sample Input 3:
    3 5
    11 6 12

    Sample Output 3:
    3

    Sample Explanation 3:
    We can change the first element from 11 to 3. Then the GCD of the array becomes gcd(3, 6, 12) = 3, which is the maximum possible.'''
