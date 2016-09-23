# coding: utf-8
file=open('input.txt','r')
adjacencyList = []
adjacencyList=file.read().splitlines()

input=[]
explored=[]
for i in adjacencyList:
    data=i.split(',')
    input.append(data)
#print input

graph={}

for row in input:
    if row[0] in graph.keys():
        graph[row[0]][row[1]]=row[2]
        if row[1] not in graph.keys():
            graph[row[1]]={}
            graph[row[1]][row[0]]=row[2]
        else:
            graph[row[1]][row[0]]=row[2]

    else:
        graph[row[0]]={}
        graph[row[0]][row[1]]=row[2]
        if row[1] not in graph.keys():
            graph[row[1]]={}
            graph[row[1]][row[0]]=row[2]
        else:
            graph[row[1]][row[0]]=row[2]



#print graph

def expandnode(node, graph):
    childrens = graph[node]
    if len(childrens) == 0:
        print "node %s is a dead end" %node
    return childrens

def testgoal(dest, node):
    print "Reached Destination? %s" %node
    if dest == node:
        print "Reached Destination!!!!\n"
        return True
    else:
        print "Not yet!!!\n\n"
        return False

def updatefrontier(q):
    popped = q[0]
    del(q[0])
    return popped

def graphsearch(frontier, graph, dest):
    while True:
        print "Frontier: ", frontier
        if len(frontier) == 0:
            return "Destination node is not reachable from the Starting node"
        node = updatefrontier(frontier)
        explored.append(node)
        if testgoal(dest, node):
            return "Destination reached %s" %node
        else:
            for child in expandnode(node, graph):
                if child in explored:
                    pass
                else:
                    frontier.append(child)


def initializefrontier(start, dest, graph):
    frontier = [start]
    print graphsearch(frontier, graph, dest)
    print "Path:"
    print explored


if __name__ == "__main__":
    import json
    gprint = json.dumps(graph)
    print "The provided graph: %s" %gprint
    print "Using BFS search strategy"
    print "Enter the starting node:"
    start = raw_input()
    print "Enter the destination node:"
    dest = raw_input()
    initializefrontier(start, dest, graph)