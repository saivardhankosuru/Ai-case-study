import heapq

def greedy_best_first_search(start_node, goal_node, get_neighbors, heuristic):
    """
    Finds a path from start_node to goal_node using GBFS.

    Args:
        start_node: The starting node.
        goal_node: The goal node.
        get_neighbors: A function that returns a list of neighboring nodes.
        heuristic: A function that estimates the cost from a node to the goal.

    Returns:
        A list of nodes representing the path, or None if no path is found.
    """

    priority_queue = [(heuristic(start_node, goal_node), start_node, [])]  # (heuristic, node, path)
    visited = set()

    while priority_queue:
        h, current_node, path = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == goal_node:
            return path + [current_node]

        for neighbor in get_neighbors(current_node):
            priority = heuristic(neighbor, goal_node)
            heapq.heappush(priority_queue, (priority, neighbor, path + [current_node]))

    return None #No path found

def magical_energy_heuristic(node, goal_node):
    """
    Estimates the distance to the Philosopher's Stone based on magical energy.
    """
    # Replace with actual logic based on magical energy readings
    energy_level = get_magical_energy(node)
    goal_energy = get_magical_energy(goal_node)
    distance = goal_energy - energy_level
    return distance
def get_magical_energy(node):
  #Dummy function to get magical energy
  return 1

def get_neighbors_example_GBFS(node):
  """
  Example function for gbfs to return list of neighbouring nodes
  """
  neighbours = []

  if node == "Entrance Hall":
      neighbours.append("Chamber 1")
      neighbours.append("Great Hall")
  elif node == "Chamber 1":
      neighbours.append("Entrance Hall")

  return neighbours
# Example Usage

start = "Entrance Hall"
goal = "Philosopher's Stone Chamber"

path = greedy_best_first_search(start, goal, get_neighbors_example_GBFS, magical_energy_heuristic)
if path:
  print("Path found:", path)
else:
  print("No path found.")
