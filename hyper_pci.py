import hypernetx as hnx
import numpy as np
from wrapper import create_graph

#Strict HyperPCI
def strict_hyperpci(G,graph):
    results = {}
    for node in list(G.nodes):
        for threshold in range(1,G.degree(node) + 1):
            total = 0
            for curr in list(G.neighbors(node)):
                # Find the real neighbours
                num_of_appears = 0
                for edge in graph.values():
                    if len(edge) > 2 and curr in edge and node in edge:
                        num_of_appears = num_of_appears + 1
                if(G.degree(curr)- num_of_appears > threshold):
                    total = total + 1
            if(total <= threshold):
                break
        results[node] = threshold
    
    return results
    

#Loose HyperPCI
def loose_hyperpci(G,graph):
    results = {}
    for node in list(G.nodes):
        temp = 1
        maxim = -np.inf
        # Get max degree of hyperedge neighbors
        for curr in list(G.neighbors(node)):
            num_of_appears = 0
            for edge in graph.values():
                if len(edge) > 2 and curr in edge and node in edge:
                    num_of_appears = num_of_appears + 1
                    temp = G.degree(curr) - num_of_appears
            if(temp >= maxim):
                maxim = temp

        results[node] = maxim
    
    return results
    
# Additivie HyperPCI
def additive_hyperpci(G,graph):
    results = {}
    for node in list(G.nodes):
        binary_neighbors = G.neighbors(node)
        hyper_neighbors = []
        deg = 0
        for curr in list(G.neighbors(node)):
            for edge in graph.values():
                if len(edge) > 2 and curr in edge and node in edge:
                    to_remove = curr
                    hyper_neighbors.append(curr)
                    if to_remove in binary_neighbors:
                        binary_neighbors.remove(to_remove)
        for temp_node in hyper_neighbors:
            deg += G.degree(temp_node) - 1
        if len(hyper_neighbors) == 0:
            num = 1
        else:
            num = int(deg / len(hyper_neighbors))
        results[node] = num
    
    return results

if __name__ == "__main__":
    # Replace the filepath with the wanted one
    filepath = '/cat-edge-algebra-questions/hyperedges.txt'
    graph = create_graph(filepath)
    G = hnx.Hypergraph(graph)
    
    strict_results = strict_hyperpci(G,graph)
    loose_results = loose_hyperpci(G,graph)
    additive_results = additive_hyperpci(G,graph)
    
    # Write results to file in table format
    with open('hyperpci_results.txt', 'w') as f:
        f.write("node | value from strict function | value from loose function | value from the additive function\n")
        for node in strict_results.keys():
            f.write(f"{node} | {strict_results[node]} | {loose_results[node]} | {additive_results[node]}\n")
    
