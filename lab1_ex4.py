import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-W", type=int)
parser.add_argument("-w", type=int, nargs='+')
parser.add_argument("-n", type=int)
args = parser.parse_args()


def knapsack(w, wt, n):
    dp = [[0 for i in range(w + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(w + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif wt[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wt[i - 1]] + wt[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][w]


print(knapsack(args.W, args.w, args.n))
