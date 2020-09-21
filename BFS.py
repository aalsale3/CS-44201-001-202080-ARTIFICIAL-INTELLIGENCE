from collections import defaultdict
class GraphBFS: 
    
    # default constructor
    def __init__(self): 
        # default dictionary to store graph using adjacenct list
        self.graph = defaultdict(list) 
        
    # Function to add an edge from one node to another node in to the graph 
    def addEdgeToGraph(self,fromNode,toNode): 
        self.graph[fromNode].append(toNode)

    # Function to Traverse graph by Breadth First Search and print the Traversal result
    # It accept source Node or starting Node as the parameter to the Function
    def BreadthFirstSearch(self, sourceNode): 
        # Mark all the nodes in graph as not visited referenced by index
        visited = [False] * (len(self.graph)) 
        # Create a empty queue for Breadth First Search to store connected and unvisited nodes
        queue = [] 
        # Mark the starting node (passed as parameter to the function) as visited and enqueue it
        visited[ord(sourceNode)-65] = True
        queue.append(sourceNode) 
        # while the queue is not empty keep on Traversing the graph
        while queue: 
            # Dequeue a vertex from graph queue and print the vertex
            sourceNode = queue.pop(0) 
            print (sourceNode, end = " ") 
            # Get all adjacent vertices of the dequeued vertex sourceNode. If a adjacent has not been visited, then mark it visited and enqueue it 
            for adjacentNode in self.graph[sourceNode]: 
                if visited[ord(adjacentNode)-65] == False: 
                    queue.append(adjacentNode) 
                    visited[ord(adjacentNode)-65] = True

# Create a graph using the diagram given in the question
graphBfs = GraphBFS() 
graphBfs.addEdgeToGraph('A', 'B') 
graphBfs.addEdgeToGraph('A', 'C') 
graphBfs.addEdgeToGraph('B', 'A')
graphBfs.addEdgeToGraph('B', 'C')
graphBfs.addEdgeToGraph('B', 'D') 
graphBfs.addEdgeToGraph('C', 'A') 
graphBfs.addEdgeToGraph('C', 'B') 
graphBfs.addEdgeToGraph('C', 'D') 
graphBfs.addEdgeToGraph('C', 'E')
graphBfs.addEdgeToGraph('D', 'B') 
graphBfs.addEdgeToGraph('D', 'C')
graphBfs.addEdgeToGraph('D', 'E')
graphBfs.addEdgeToGraph('D', 'F')
graphBfs.addEdgeToGraph('E', 'C')
graphBfs.addEdgeToGraph('E', 'D')
graphBfs.addEdgeToGraph('E', 'F')
graphBfs.addEdgeToGraph('F', 'D')
graphBfs.addEdgeToGraph('F', 'E') 
print ("Following is Breadth First Traversal"
                  " (starting from vertex A)") 
# calling the BreadthFirstSearch function with starting Node as 'A'
graphBfs.BreadthFirstSearch('A')
