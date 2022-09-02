# https://my.newtonschool.co/playground/code/o2wbtmgzjatw/

def question():
    return '''Golden Coins (Public Contest: August 2022)
        Time Limit: 3 sec
        Memory Limit: 128000 kB
        Problem Statement
        Rhaenyra always likes to predict the future and prepare accordingly. She recently came across a new game. The game is as follows:

        There is a coordinate plane and the player starts at (0, 0). Each minute, the player walks from (x, y) to (x, y+1) with a probability of P/Q, or to (x+1, y) with a probability of R/S, or stops immediately with probability 1-(P/Q)-(R/S). Here, P, Q, R, S are non-negative integers such that Q, S > 0 and (P/Q)+(R/S) < 1. Once the player stops, he never moves again. Furthermore, the player will stop walking after N minutes.

        Golden coins have also been placed at coordinates (m*D, n*D) (for all m, n ≥ 0), i.e. at all the positions where both the x and y-coordinates are multiples of D. Barriers have also been placed at K positions, (x1, y1), (x2, y2), ... (xK, yK), with the maximum value of xi's being M. If the player walks into a barrier, he will stop immediately and would never move again. If the player walks into a golden coin (including position (0, 0)), he will immediately pick up the coin without losing time. The position of a golden coin and barrier is guaranteed not to collide.

        Rhaenyra is eager to play this game. However, due to her nature, she first wants to calculate the expected number of golden coins she would collect. If the expected number of golden coins is X/Y (where X and Y are non-negative integers with Y > 0), print XY-1 mod 998244353.
        Input
        The first line contains two integers A and B, where A is PQ-1 mod 998244353, and B is RS-1 mod 998244353.
        The second line contains four integers N, D, M and K.
        Then K lines follow, where the ith line contains two integers xi and yi – the position of the ith barrier.

        Constraints:
        0 ≤ A, B < 998244353
        1 ≤ N ≤ 1018
        1 ≤ D, M ≤ 1000
        0 ≤ K ≤ 50
        0 ≤ xi ≤ M, 0 ≤ yi
        xi + yi ≤ N
        (xi , yi) is not at a position containing a golden coin.
        Output
        If the expected number of golden coins is X/Y (where X and Y are non-negative integers with Y > 0), print XY-1 mod 998244353.
        Example
        Sample Input 1:
        1 1
        2 2 5 1
        1 0

        Sample Output 1:
        2

        Sample Input 2:
        1 2
        2 2 5 0

        Sample Output 2:
        6'''

