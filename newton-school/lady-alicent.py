# https://my.newtonschool.co/playground/code/5km47j91xmf6/

def question():
    return '''Lady Alicent and Dragons (Public Contest: August 2022)
    Time Limit: 3 sec
    Memory Limit: 128000 kB
    Problem Statement
    Lady Alicent wants to impress the king, so she asked a stonemason to carve a dragon. But we know that dragons are magical, and their internal structure is in the form of trees. However, the stonemason couldn't understand that sacred magic, so he wants you to answer some queries he has.

    You are given a tree consisting of N nodes numbered from 1 to N. Each edge of the tree contains a label with an English lowercase character. Let path(X, Y) be defined as the string obtained by concatenating characters on the simple path from vertex X to vertex Y.

    You need to answer Q queries. Each query consists of 2 vertices U and V. You need to find the number of vertices X such that, path(U, X) is strictly lexicographically smaller than path(U, V).

    Since the number of queries can be large, just print the bitwise-xor of the answers of each query.
    Input
    The first line contains two space-separated integers N and Q.
    The next N-1 lines each contain two space-separated integers X and Y followed by an English lowercase character C, denoting an edge between vertices X and Y whose label is C.
    The next Q lines each contain two space-separated integers U and V, representing a query.

    Constraints:
    1 ≤ N ≤ 4000
    1 ≤ Q ≤ 5×105
    1 ≤ X, Y ≤ N
    1 ≤ U, V ≤ N
    Output
    Print a single integer – the bitwise-xor of the answers of all the queries.
    Example
    Sample Input:
    5 2
    1 2 a
    2 3 b
    1 4 a
    4 5 c
    1 3
    4 5

    Sample Output:
    1

    Sample Explanation:
    Answer for first query is 2 as:
    path(1,3) = ab
    Lexicographically smaller paths with starting vertex as 1:
    path(1,2) = a
    path(1,4) = a

    Answer for second query is 3 as:
    path(4,5) = c
    Lexicographically smaller paths with starting vertex as 4:
    path(4,1) = a
    path(4,2) = aa
    path(4,3) = aab'''


