
n = int(input())
m = [[0]*n for _ in range(n)]
num = 1
start = 0
end= n - 1

while start <= end:
    for i in range(start, end+1):
        m[start][i] = num
        num += 1
    for i in range(start+1, end+1):
        m[i][end] = num
        num += 1
    for i in range(end-1, start-1, -1):
        m[end][i] = num
        num += 1
    for i in range(end-1, start, -1):
        m[i][start] = num
        num += 1
    start+= 1
    end-= 1

for r in m:
    print(*r)
                