from search import GraphProblem, romania_map, depth_first_graph_search, uniform_cost_search, breadth_first_graph_search
from notebook import show_map

graph_problem = GraphProblem('Arad', 'Bucharest', romania_map)
node = depth_first_graph_search(graph_problem)

print(node)
while node.parent is not None and not node == graph_problem.initial:
    node = node.parent
    print(node)

node_colors = {node: 'white' for node in romania_map.locations.keys()}
node_positions = romania_map.locations
node_label_pos = {k: [v[0], v[1] - 10] for k, v in romania_map.locations.items()}
edge_weights = {(k, k2): v2 for k, v in romania_map.graph_dict.items() for k2, v2 in v.items()}

romania_graph_data = {'graph_dict': romania_map.graph_dict,
                      'node_colors': node_colors,
                      'node_positions': node_positions,
                      'node_label_positions': node_label_pos,
                      'edge_weights': edge_weights
                      }

show_map(romania_graph_data)
