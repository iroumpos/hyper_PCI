import hypernetx as hnx

# Read dataset and create hypergraph
def create_graph(filepath):
    mygraph = {}

    with open(filepath, 'r') as file:
        for index, line in enumerate(file):
            # Assuming values are comma-separated on each line
            values = tuple(map(int, line.strip().split(' ')))
            mygraph[index] = values
    
    return mygraph