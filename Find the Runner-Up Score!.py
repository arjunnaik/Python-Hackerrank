if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
ans = list(set(arr))
ans.sort()
print(ans[-2])
