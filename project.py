import time
import queue
import networkx as nx
import matplotlib.pyplot as plt

def order_bfs(graph, start_node):
    visited = set()
    q = queue.Queue()
    q.put(start_node)
    order = []
    while not q.empty():
        vertex = q.get()
        if vertex not in visited:
            order.append(vertex)
            visited.add(vertex)
            for node in graph[vertex]:
                if node not in visited:
                    q.put(node)
    return order

def order_dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
        
    order = []
    if start_node not in visited:
        order.append(start_node)
        visited.add(start_node)
        for node in graph[start_node]:
            if node not in visited:
                order.extend(order_dfs(graph, node, visited))
    return order

def visualize_search(order, title, G, pos):
    plt.figure()
    plt.title(title)
    for i, node in enumerate(order):
        plt.clf()
        plt.title(f"{title} - Step {i+1}/{len(order)}")
        node_colors = ['green' if n in order[:i+1] else 'skyblue' for n in G.nodes]
        nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=500, edge_color='gray', font_size=10, font_color='black')
        plt.draw()
        plt.pause(1)
    plt.show()
    time.sleep(0.5)

def generate_connected_random_graph(n, m):
    while True:
        G = nx.gnm_random_graph(n, m)
        if nx.is_connected(G):
            return G

# Get user input for graph parameters
num_nodes = int(input("Enter the number of nodes: "))
num_edges = int(input("Enter the number of edges: "))
start_node = int(input(f"Enter the starting node (0 to {num_nodes-1}): "))

# Generate a connected random graph with user-specified parameters
G = generate_connected_random_graph(num_nodes, num_edges)
pos = nx.spring_layout(G)

# Visualize BFS search starting from the user-specified node
visualize_search(order_bfs(G, start_node), 'BFS Visualization', G, pos)
visualize_search(order_dfs(G, start_node), 'DFS Visualization', G, pos)

