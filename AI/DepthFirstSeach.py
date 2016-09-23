# coding: utf-8
file=open('input.txt','r')
temp = file.read().splitlines()
parent = {}
input = []
visited = []
graph = {}

for i in temp:
    data = i.split(',')
    input.append(data)

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


def testgoal(dest, node):
    if dest == node:
        print "%s Destination!\n" %node
        return True
    else:
        print "Try next\n\n"
        return False

def findPrevious(parent, start, dest):
    path = [dest]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

def findPathCost(path):
    pathCost = 0
    i=1
    current = path[0]
    while current != dest:
        pathCost = pathCost + int(graph[current][path[i]])
        current = path[i]
        i = i + 1
    return pathCost


def updatefrontier(q):
    popped = q.pop()
    return popped


def gsearch(frontier, graph, dest):
    flag = 0
    while flag==0:
        print "Frontier-> ", frontier
        if len(frontier) == 0:
            return "Destination node is not reachable from the Starting node"
        node = updatefrontier(frontier)
        visited.append(node)
        if testgoal(dest, node):
            return "%s reached" %node
        else:
            for child in expandnode(node, graph):
                if child in visited:
                    pass
                else:
                    frontier.append(child)
                    visited.append(child)
                    parent[child] = node
                    if dest == child:
                        path = findPrevious(parent, start, dest)
                        for item in path:
                            print item, "> ",
                        print "Total Cost = ", findPathCost(path)
                        flag = 1
                        break


def initializefrontier(start, dest, graph):
    frontier = [start]
    print gsearch(frontier, graph, dest)

def choosenode():
    data = raw_input()
    return data

if __name__ == "__main__":
    print "Source city:",
    start = choosenode()
    print "Destination city:",
    dest = choosenode()
    initializefrontier(start, dest, graph)
