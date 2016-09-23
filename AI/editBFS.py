dict_graph = {}
frontier = []
explored = []

class myNode():
    def __init__(self, state=None, parent=None, action=[], cost=[]):
        self.STATE = state
        self.PARENT = parent
        self.ACTION = action
        self.PATH_COST = cost

class alg():
    def __init__(self):
        '''
        dict_graph['state'] = node
        '''
        self.dict_graph = {}
        self.frontier = []
        self.explored = []

    def read_data(self, filename):
        '''
        Return list of lists for the data read from the input file
        '''
        input_file = open(filename,'r')
        data = []
        for line in input_file:
            data.append(line.strip().split(','))
        return data
        
    def initialize_graph(self, data):
        for d in data:
            if(d[0] in self.dict_graph.keys()):
                self.dict_graph[d[0]].ACTION.append(d[1])
                self.dict_graph[d[0]].PATH_COST.append(d[2])
            else:
                inputNode = myNode(state=d[0], action=[d[1]], cost=[d[2]])
                self.dict_graph[d[0]] = inputNode

            if(d[1] in self.dict_graph.keys()):
                self.dict_graph[d[1]].ACTION.append(d[0])
                self.dict_graph[d[1]].PATH_COST.append(d[2])
            else:
                inputNode = myNode(state=d[1], action=[d[0]], cost=[d[2]])
                self.dict_graph[d[1]] = inputNode
        return 

    def initializeFrontier(self, inputNode):
        for list in inputNode:
            if list.STATE == "Arad":
                frontier.append(list)
                break
        return frontier

    def chooseNode(self, myNode, dict_graph):
        for node in dict_graph[myNode]:
            if node == dict_graph[myNode].STATE:
                return node
        return False        


    def expandNode(self, parentNode, actionNode, dict_graph):
        node = chooseNode(self, actionNode, dict_graph)
        for list in dict_graph[parentNode].ACTION:
            if actionNode == list.STATE:
                return list
        return False
  

    def updateFrontier(self, node):
        if node.STATE not in frontier:
            frontier.append(node.STATE)
        else:
            frontier.remove(node.STATE)    
        return frontier
        

    def testGoal(self, inputNode, goal='Bucharest'):
        if(inputNode.STATE == goal):
            return True
        return False

    def bfs_graph_search(self, graph):
        frontier = self.initializeFrontier(graph)
        testGoalResult = self.testGoal(dict_graph.STATE)
        if testGolaResult == True:
            return True
        else:
            while frontier:
                node = updateFrontier(frontier)
                explored = dict_graph[node].STATE
                for action in dict_graph[explored].ACTION:
                    actionState = self.expandNode(explored, action, dict_graph)
                    if actionState.STATE not in frontier:
                        testgolaRsult1 = self.testGoal(actionState.STATE)
                        if testGolaResult1 == True:
                            explored.append(actionState.STATE)
                        else:    
                            frontier = self.updateFrontier(actionState.STATE)
            return explored

def main():
    bfs = alg()
    filename = 'inout.txt'
    data = alg.read_data(filename)
    graph = alg.initialize_graph(data)
    solution = alg.bfs_graph_search(graph)
    for list in solution:
        print list

if __name__ == "__main__":
    main()    








