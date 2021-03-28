# N*M的棋盘上，小兵要从左下角走到右上角，只能向上或者向右走，问有多少种走法？ 
# 注意：这里说的N*M是指线段，而不是指几根竖线，几根横线。线段总是比线少1个的。下面的讨论都是基于线段的。

def solve(n, m):
    # 无格子
    if n == 0 or m == 0:
        return 0
    # 条状格子
    if n == 1 or m == 1:
        return 1
    return solve(n-1,m) + solve(n, m-1)


print(solve(3, 3))