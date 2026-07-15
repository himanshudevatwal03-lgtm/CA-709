def tsp(dist):
    n = len(dist)
    INF = float('inf')

    # dp[mask][u] = minimum cost to visit cities in mask and end at u
    dp = [[INF] * n for _ in range(1 << n)]

    # Start from city 0
    dp[1][0] = 0

    for mask in range(1 << n):
        for u in range(n):
            if dp[mask][u] == INF:
                continue

            for v in range(n):
                if mask & (1 << v):
                    continue  # already visited

                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(
                    dp[new_mask][v],
                    dp[mask][u] + dist[u][v]
                )

    full_mask = (1 << n) - 1
    ans = INF

    # Return to starting city (0)
    for u in range(n):
        ans = min(ans, dp[full_mask][u] + dist[u][0])

    return ans


# Example
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print("Minimum cost:", tsp(dist))
