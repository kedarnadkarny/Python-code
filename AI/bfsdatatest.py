graph = {'Timisoara': {'Lugoj': '111', 'Arad': '118'}, 'Drobeta': {'Craiova': '120', 'Mehadia': '75'}, 'Arad': {'Zerind': '75', 'Timisoara': '118', 'Sibiu': '140'}, 'Pitesti': {'Craiova': '138', 'Bucharest': '101', 'Rimnicu Vilcea': '97'}, 'Craiova': {'Drobeta': '120', 'Pitesti': '138', 'Rimnicu Vilcea': '146'}, 'Eforie': {'Hirsova': '86'}, 'Neamt': {'Iasi': '87'}, 'Hirsova': {'Eforie': '86', 'Urziceni': '98'}, 'Fagaras': {'Bucharest': '211', 'Sibiu': '99'}, 'Sibiu': {'Oradea': '151', 'Rimnicu Vilcea': '80', 'Fagaras': '99', 'Arad': '140'}, 'Vaslui': {'Iasi': '92', 'Urziceni': '142'}, 'Urziceni': {'Bucharest': '85', 'Vaslui': '142', 'Hirsova': '98'}, 'Oradea': {'Zerind': '71', 'Sibiu': '151'}, 'Mehadia': {'Drobeta': '75', 'Lugoj': '70'}, 'Lugoj': {'Timisoara': '111', 'Mehadia': '70'}, 'Zerind': {'Oradea': '71', 'Arad': '75'}, 'Iasi': {'Neamt': '87', 'Vaslui': '92'}, 'Giurgiu': {'Bucharest': '90'}, 'Rimnicu Vilcea': {'Craiova': '146', 'Pitesti': '97', 'Sibiu': '80'}, 'Bucharest': {'Pitesti': '101', 'Fagaras': '211', 'Urziceni': '85', 'Giurgiu': '90'}}
explored = ['Arad', 'Zerind', 'Timisoara', 'Sibiu', 'Oradea', 'Lugoj', 'Rimnicu Vilcea', 'Fagaras', 'Mehadia', 'Craiova', 'Pitesti', 'Bucharest']
temp =     ['Bucharest', 'Pitesti', 'Craiova', 'Mehadia', 'Fagaras', 'Rimnicu Vilcea', 'Lugoj', 'Oradea', 'Sibiu', 'Timisoara', 'Zerind', 'Arad']
parents =  {'Pitesti': '101', 'Fagaras': '211', 'Urziceni': '85', 'Giurgiu': '90'}
final_path = {}
"""
for key, value in graph.items():
    print key, value
"""

tempParents={}
k = temp[0]
startNode = 'Arad'
node = temp
visited = []
i=0
ParentIsStartNode = 0
while k!=startNode:
    if node[i] == k and node[i] not in visited:
        item = node[i]
        parents = graph[item]
        for key, value in parents.items():
            if key in explored and key not in visited:
                tempParents[key] = value
            if key == startNode:
                ParentIsStartNode = 1
        x = min(tempParents.items(), key=lambda x: int(x[1]))
        print x
        k = x[0]
        visited.append(item)
        tempParents = {}
        final_path[x[0]] = x[1]
        i = i + 1
    else:
        i = i+1

# Also check if parent node is startNode