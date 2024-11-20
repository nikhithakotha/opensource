def solve():
    x, y, z = map(int, input().split())
    total_minutes_needed = x * y
    total_minutes_available = z * 24 * 60
    print("YES" if total_minutes_needed <= total_minutes_available else "NO")
solve()
