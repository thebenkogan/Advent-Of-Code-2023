from aoc import read_input
import networkx as nx

lines = read_input()

G = nx.Graph()

for line in lines:
    label, conns = line.split(": ")
    conns = conns.split(" ")
    for conn in conns:
        G.add_edge(label, conn, capacity=1)

start = "fml"
# find a node that has the longest shortest path from the start
# if start was in one of the partitions, this one should be in the other
end = max(nx.shortest_path(G, start).items(), key=lambda x: len(x[1]))[0]

val, partition = nx.minimum_cut(G, start, end)
print(len(partition[0]) * len(partition[1]))
