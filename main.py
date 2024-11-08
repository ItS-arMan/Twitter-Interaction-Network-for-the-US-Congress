import matplotlib.pyplot as plt
import numpy as py
import pandas as pd
import networkx as nx

G = nx.read_edgelist('congress.edgelist', create_using=nx.DiGraph())
G_undirected = nx.to_undirected(G)

nodes = G.number_of_nodes()
edges = G.number_of_edges()
density = nx.density(G_undirected)
diameter = nx.diameter(G_undirected)
radius = nx.radius(G_undirected)
degree = [deg for node, deg in G.degree()]
mean_degree = py.mean(degree)
var_degree = py.var(degree)
max_degree = py.max(degree)
lwcc = max(nx.weakly_connected_components(G), key=len)
lscc = max(nx.strongly_connected_components(G), key=len)

normalized_closeness_centrality = nx.closeness_centrality(G_undirected)
top_nodes = sorted(normalized_closeness_centrality.items(), key=lambda item: item[1], reverse=True)[:3]

plt.figure(figsize=(12, 8))
pos = nx.kamada_kawai_layout(G)
nx.draw(G, pos,
        with_labels=False,
        node_color='lightblue',
        node_size=20,  # Adjust the size for better fit
        alpha=0.6)  # Set transparency for better visibility

plt.title("Graph Visualization (Directed)")
plt.show()

plt.hist(degree, edgecolor='black', bins=40)
plt.title("Degree Distribution")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.show()

plt.scatter(range(len(degree)), sorted(degree, reverse=True), marker='.')
plt.title("Degree Centrality Distribution")
plt.xlabel("Node Index")
plt.ylabel("Degree")
plt.show()

summery = pd.DataFrame({
    "Metric": [
        "Nodes", "Edges", "Density",
        "Diameter", "Radius", "Degrees",
        "Mean Degrees", "Degree Variance",
        "Max Degrees", "Largest Weakly Connected Components",
        "Number of Largest Weakly Connected Components",
        "Largest Strongly Connected Components",
        "Number of Largest Strongly Connected Components ",
        "Top 3 Nodes by Closeness Centrality"
    ],
    "Values": [
        nodes, edges, density,
        diameter, radius, degree,
        mean_degree, var_degree,
        max_degree, lwcc, len(lwcc),
        lscc, len(lscc), top_nodes
    ]
})

summery.to_excel("network_analysis_results.xlsx", index=False)
