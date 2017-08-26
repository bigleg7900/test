# encoding=utf-8


def test(word1, word2):
    length1 = len(word1) + 1
    length2 = len(word2) + 1

    dp = []
    for i in xrange(length1):
        tmp = []
        for j in xrange(length2):
            tmp.append(j)
        dp.append(tmp)

    for i in xrange(length1):
        dp[i][0] = i

    for i in xrange(length2):
        dp[0][i] = i

    for i in xrange(1, length1):
        for j in xrange(1, length2):
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1))

    return dp[length1 - 1][length2 - 1]

if __name__ == '__main__':
    print test('hello world', 'hwllo word')
