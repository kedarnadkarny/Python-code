socks = input()
socks = int(socks)
hash=[]
data = input().split(' ')
hash = data
visited = []

graph={}

for item in hash:
    if item in graph.keys():
        graph[item] = graph[item] + 1
    else:
        graph[item] = 1

total = 0
for item in graph.keys():
    total = int(graph[item]/2) + total

print(total)