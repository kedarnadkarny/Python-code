# coding: utf-8
from Queue import PriorityQueue

file=open('input.txt','r')
tempList = file.read().splitlines()
temp = []
path_cost = 0
queue = PriorityQueue()
visited = ''
input=[]

explored=[]
for i in tempList:
    data = i.split(',')
    input.append(data)

graph={}

for row in input:
    if row[0] in graph.keys():
        # if node exists in graph, add city2 and distance
        graph[row[0]][row[1]]=row[2]
        if row[1] not in graph.keys():
            # If city2 not in graph, add
            graph[row[1]] = {}
            # add city1 and distance to city2
            graph[row[1]][row[0]]=row[2]
        else:
            # city2 present, so add city1 and distance
            graph[row[1]][row[0]]=row[2]

    else:
        # Assign Node in graph
        graph[row[0]]={}
        # Add city2 and distance to city1
        graph[row[0]][row[1]]=row[2]
        if row[1] not in graph.keys():
            # Assign city2 to graph
            graph[row[1]]={}
            # Add city1 and distance to city2
            graph[row[1]][row[0]]=row[2]
        else:
            # Add city1 and distance to city
            graph[row[1]][row[0]]=row[2]

def expandnode(node, graph):
    childrens = graph[node]
    if len(childrens) == 0:
        print "node %s is a dead end" %node
    return childrens

def updatefrontier(q):
    popped = q[0]
    del (q[0])
    return popped

def findPathCost(node, i):
    pathCost = 0
    i=1
    current = node[0]
    while current != dest:
        pathCost = pathCost + int(graph[current][node[i]])
        current = node[i]
        i = i + 1
    return pathCost

def graphsearch(frontier, graph, goal, start):
    global visited
    visited = set()
    global queue
    queue.put((0, start))

    while queue:
        cost, node = queue.get()
        if node not in visited:
            visited.add(node)

            if node == goal:
                return queue
            for i in expandnode(node, graph):
                if i not in visited:
                    total_cost = cost + int(graph[node][i])
                    queue.put((total_cost, i))


def initializefrontier(start, dest, graph):
    frontier = [start]
    out = graphsearch(frontier, graph, dest, start)
    print "Node Traversal: ",
    for item in visited:
        print item, "> ",
    for item in out.queue:
        if item[1] == dest:
            print "Total Cost = ", item[0]


def choosenode():
    data = raw_input()
    return data

if __name__ == "__main__":
    print "Source city:",
    start = choosenode()
    print "Destination city:",
    dest = choosenode()
    initializefrontier(start, dest, graph)