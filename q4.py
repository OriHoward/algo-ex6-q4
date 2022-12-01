import math
import networkx as nx


def check_for_negative_cycle_bellman_ford(curr_graph, source):
    try:
        nx.bellman_ford_predecessor_and_distance(curr_graph, source,
                                                 weight=lambda source_edge, dest_edge, weight: math.log2(
                                                     curr_graph.get_edge_data(source_edge, dest_edge).get(
                                                         "weight")))
        print("Couldn't find any negative cycles")
    except:
        find_negative_cycle(curr_graph, source)


def find_negative_cycle(curr_graph, source):
    negative_cycle = nx.find_negative_cycle(curr_graph, source, weight=lambda source_edge, dest_edge, weight: math.log2(
        curr_graph.get_edge_data(source_edge, dest_edge).get("weight")))
    result = 1
    for node_ind in range(len(negative_cycle) - 1):
        curr_weight = curr_graph.get_edge_data(negative_cycle[node_ind], negative_cycle[node_ind + 1]).get("weight")
        result *= curr_weight
    print(f"Found a negative cycle: {negative_cycle} \n"
          f"Cycle multiplication is: {result:.2f} --> {result:.2f} < 1")


if __name__ == '__main__':
    DiGraph_one = nx.DiGraph()
    DiGraph_two = nx.DiGraph()
    DiGraph_three = nx.DiGraph()

    # first DiGraph - has a cycle which its edges multiplication <1
    DiGraph_one.add_node(1)
    DiGraph_one.add_node(2)
    DiGraph_one.add_node(3)

    DiGraph_one.add_edge(1, 2, weight=0.25)
    DiGraph_one.add_edge(2, 3, weight=0.5)
    DiGraph_one.add_edge(3, 1, weight=7)

    # second DiGraph - no negative cycles
    DiGraph_two.add_node(1)
    DiGraph_two.add_node(2)
    DiGraph_two.add_node(3)
    DiGraph_two.add_node(4)
    DiGraph_two.add_node(5)

    DiGraph_two.add_edge(1, 2, weight=0.2)
    DiGraph_two.add_edge(2, 3, weight=10)
    DiGraph_two.add_edge(3, 4, weight=3)
    DiGraph_two.add_edge(4, 5, weight=1)
    DiGraph_two.add_edge(5, 4, weight=2)
    DiGraph_two.add_edge(4, 3, weight=5)
    DiGraph_two.add_edge(3, 2, weight=0.1)
    DiGraph_two.add_edge(2, 1, weight=20)

    # third DiGraph
    DiGraph_three.add_node(1)
    DiGraph_three.add_node(2)
    DiGraph_three.add_node(3)
    DiGraph_three.add_node(4)

    DiGraph_three.add_edge(1, 2, weight=0.2)
    DiGraph_three.add_edge(2, 3, weight=0.9)
    DiGraph_three.add_edge(3, 4, weight=11)
    DiGraph_three.add_edge(4, 5, weight=2)
    DiGraph_three.add_edge(5, 4, weight=13)
    DiGraph_three.add_edge(4, 3, weight=0.3)
    DiGraph_three.add_edge(3, 2, weight=0.1)
    DiGraph_three.add_edge(2, 1, weight=2)

    print("First graph:")
    check_for_negative_cycle_bellman_ford(DiGraph_one, 1)
    print("")
    print("Second graph:")
    check_for_negative_cycle_bellman_ford(DiGraph_two, 3)
    print("")
    print("Third graph: ")
    check_for_negative_cycle_bellman_ford(DiGraph_three, 3)
    check_for_negative_cycle_bellman_ford(DiGraph_three, 1)
