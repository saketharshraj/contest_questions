# https://my.newtonschool.co/playground/code/8teijug4nw7e/

def question():
    return '''The Weirwood (Public Contest: August 2022)
            Time Limit: 6 sec
            Memory Limit: 512000 kB
            Problem Statement
            While Alicent and Rhaenyra were walking in the Godswood, they noticed a slight abnormality in one of the Weirwood trees. This poked an idea into Alicent's mind, and she decides to ask a puzzle to Rhaenyra.

            Alicent selects a tree with N nodes numbered from 1 to N, and gives Rhaenyra an empty array A. Initially, all the nodes in the tree are coloured white. Now, Alicent selects two nodes A and B (A may be equal to B) and colours these two nodes grey. Now, Rhaenyra has to do the following operation N times:

            1. Select a grey-coloured node X and colour it black. Then, select all the presently white coloured neighbours of X, and colour them grey. Push X to the end of A.

            Once she is done, all the nodes would be coloured black, and array A would be of size N. Now Rhaenyra has to answer how many different arrays A are possible after doing the above sequence of operations. Remember the order of elements in A matter, so [1, 2, 3] != [2, 1, 3].

            Since the answer can be very large, simply print it modulo 998244353.
            Input
            The first line contains 3 space-separated integers N, A, and B – the number of nodes in the tree, and the two nodes A and B which Alicent has coloured grey.
            Then N-1 lines follow, each line containing two integers X and Y representing an edge between nodes X and Y.

            Constraints:
            1 ≤ N ≤ 250,000
            1 ≤ A, B ≤ N
            1 ≤ X, Y ≤ N
            Output
            Print a single integer – the number of different possible arrays A modulo 998244353.
            Example
            Sample Input 1:
            3 1 3
            1 2
            2 3

            Sample Output 1:
            4

            Sample Explanation 1:
            The possible arrays are [1, 2, 3], [1, 3, 2], [3, 1, 2], [3, 2, 1].

            Sample Input 2:
            5 1 4
            1 2
            2 3
            3 4
            4 5

            Sample Output 2:
            25'''

