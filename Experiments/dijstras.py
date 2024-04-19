import heapq
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Node:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.neighbours = []

    def __lt__(self, other):
        # Define a comparison method for nodes
        return id(self) < id(other)

def generate_neighbors(nodes, threshold_distance):
    for i, node1 in enumerate(nodes):
        for j, node2 in enumerate(nodes):
            if node1.z == node2.z or (node1.z != node2.z and node1.x >= 8 and node2.x >=8): #If the floors are not the same AND #If the node is at the end of the hall
                if i != j: #If the nodes are not the same
                    distance = ((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2 + (node1.z - node2.z) ** 2) ** 0.5
                    if distance <= threshold_distance:
                        node1.neighbours.append((node2, distance))
                        node2.neighbours.append((node1, distance))

def dijkstra(graph, start, goal):
    heap = [(0, start, [])]
    visited = set()
    while heap:
        (cost, current, path) = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)
        path = path + [current]
        if current == goal:
            return path
        for (next_node, weight) in graph[current]:
            heapq.heappush(heap, (cost + weight, next_node, path))
    return []

def visualize_path(all_nodes, optimal_path):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Extract x, y, z coordinates from all nodes
    all_x = [node.x for node in all_nodes]
    all_y = [node.y for node in all_nodes]
    all_z = [node.z for node in all_nodes]

    # Extract x, y, z coordinates from the optimal path
    path_x = [node.x for node in optimal_path]
    path_y = [node.y for node in optimal_path]
    path_z = [node.z for node in optimal_path]

    # Visualize all nodes in one color
    ax.scatter(all_x, all_y, all_z, color='gray', marker='o', label='All Nodes')

    # Visualize the optimal path in another color
    ax.plot(path_x, path_y, path_z, linestyle='dashed', color='blue', label='Optimal Path')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Altitude')

    ax.legend()
    
    plt.show()

# Example usage:
nodes = [
    Node(0, 0, 1), Node(2, 0, 1), Node(4, 0, 1), Node(6, 0, 1), Node(8, 0, 1),
    Node(1, 2, 1), Node(3, 2, 1), Node(5, 2, 1), Node(7, 2, 1), Node(9, 2, 1),
    Node(0, 0, 2), Node(2, 0, 2), Node(4, 0, 2), Node(6, 0, 2), Node(8, 0, 2),
    Node(1, 2, 2), Node(3, 2, 2), Node(5, 2, 2), Node(7, 2, 2), Node(9, 2, 2)
]

generate_neighbors(nodes, threshold_distance=3)

# Run Dijkstra's algorithm and visualize the most optimal path
graph = {node: node.neighbours for node in nodes}
start_node = nodes[0]
goal_node = nodes[15]
optimal_path = dijkstra(graph, start_node, goal_node)
visualize_path(nodes, optimal_path)
#if optimal_path:
#    visualize_path(nodes, optimal_path)
#else:
#    print("No path found.")
