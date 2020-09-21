from collections import defaultdict 
class GraphDFS: 
    
    # default constructor 
    def __init__(self): 
        # default dictionary to store graph using adjacenct list
        self.graph = defaultdict(list) 
  
    # Function to add an edge to graph 
    def addEdgeToGraph(self,fromNode,toNode): 
        self.graph[fromNode].append(toNode)
    
    # Function to Traverse graph by Depth First Search and return the Traversal result
    # It accept source Node or starting Node and already visited nodes as the parameter to the Function
    def DepthFirstSearch(self,node,visitedNodes):
        # Check if the node is already present in visited nodes
        if node not in visitedNodes:
            # If a node has not been visited, then add it to visited nodes and loop through its adjacenct nodes
            visitedNodes.append(node)
            # Loop through the adjacenct nodes and make recursive calls to DepthFirstSearch with current looped node and visited nodes 
            for adjacenctaNode in self.graph[node]:
                # recursive calling
                self.DepthFirstSearch(adjacenctaNode,visitedNodes)
        # If a node has been visited then return the visitedNodes ( as it contains the order in which the nodes are visited)
        return visitedNodes
        
# Create a graph using the diagram given in the question
graphDfs = GraphDFS() 
graphDfs.addEdgeToGraph('A', 'B') 
graphDfs.addEdgeToGraph('A', 'C') 
graphDfs.addEdgeToGraph('B', 'A')
graphDfs.addEdgeToGraph('B', 'C')
graphDfs.addEdgeToGraph('B', 'D') 
graphDfs.addEdgeToGraph('C', 'A') 
graphDfs.addEdgeToGraph('C', 'B') 
graphDfs.addEdgeToGraph('C', 'D') 
graphDfs.addEdgeToGraph('C', 'E')
graphDfs.addEdgeToGraph('D', 'B') 
graphDfs.addEdgeToGraph('D', 'C')
graphDfs.addEdgeToGraph('D', 'E')
graphDfs.addEdgeToGraph('D', 'F')
graphDfs.addEdgeToGraph('E', 'C')
graphDfs.addEdgeToGraph('E', 'D')
graphDfs.addEdgeToGraph('E', 'F')
graphDfs.addEdgeToGraph('F', 'D')
graphDfs.addEdgeToGraph('F', 'E')
print ("Following is Depth First Traversal"
                  " (starting from vertex A)") 
# calling the DepthFirstSearch function with starting Node as 'A'
visitedOrder = graphDfs.DepthFirstSearch('A',[])
print(' '.join(visitedOrder))