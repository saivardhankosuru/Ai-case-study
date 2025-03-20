class HogwartsMap:
    """
    Represents the map of Hogwarts with secret passages.
    """

    def __init__(self, num_locations=10):
        """
        Initializes the Hogwarts map with a given number of locations and generates connections.
        """
        self.num_locations = num_locations
        self.graph = self.generate_hogwarts_graph()  # Graph representation of Hogwarts
        self.secret_passages = self.generate_secret_passages() # Randomly assign secret passages

    def generate_hogwarts_graph(self):
        """
        Generates a simple graph representing the connectivity of Hogwarts locations.
        """
        graph = {i: [] for i in range(self.num_locations)}
        # Add some basic connections to simulate the layout of Hogwarts
        graph[0].extend([1, 2])  # Great Hall connects to Entrance and Kitchen
        graph[1].extend([0, 3, 4])  # Entrance connects to Great Hall, Charms Class, and Library
        graph[2].extend([0, 5])  # Kitchen connects to Great Hall and Dungeons
        graph[3].extend([1, 6])  # Charms Class connects to Entrance and Divination Tower
        graph[4].extend([1, 7])  # Library connects to Entrance and Herbology
        graph[5].extend([2, 8])  # Dungeons connects to Kitchen and Potions Class
        graph[6].extend([3, 9])  # Divination Tower connects to Charms Class and Headmaster's Office
        graph[7].extend([4, 9])  # Herbology connects to Library and Headmaster's Office
        graph[8].extend([5])  # Potions Class connects to Dungeons
        graph[9].extend([6, 7])  # Headmaster's Office connects to Divination and Herbology

        # Ensuring the connections are bidirectional
        for node, connections in graph.items():
            for connection in connections:
                if node not in graph[connection]:
                    graph[connection].append(node)
        return graph

    def generate_secret_passages(self):
        """
        Randomly assigns secret passages in the graph.
        """
        import random
        num_passages = random.randint(1, min(4, len(self.graph)))  # Ensure passages are not too many

        passages = []
        nodes = list(self.graph.keys())
        for _ in range(num_passages):
            start_node = random.choice(nodes)
            end_node = random.choice(nodes)

            # Avoid trivial passages (same start and end) and duplicates
            while start_node == end_node or (start_node, end_node) in passages or (end_node, start_node) in passages:
                start_node = random.choice(nodes)
                end_node = random.choice(nodes)

            passages.append((start_node, end_node))
            # Add the secret passages to the graph as connections
            if end_node not in self.graph[start_node]:  # prevent duplicate edges
                self.graph[start_node].append(end_node)
            if start_node not in self.graph[end_node]:
                self.graph[end_node].append(start_node)
        return passages

    def display_graph(self):
        """Displays the graph for debugging or visualization purposes."""
        print("Hogwarts Graph Connections:")
        for node, connections in self.graph.items():
            print(f"Location {node}: Connected to {connections}")

        print("\nSecret Passages:")
        print(self.secret_passages)


def dfs_secret_passage_discovery(hogwarts_map, start_location, target_location):
    """
    Performs Depth-First Search to find a path from start_location to target_location in Hogwarts,
    considering secret passages.

    Args:
        hogwarts_map (HogwartsMap): The map of Hogwarts.
        start_location (int): The starting location for the search.
        target_location (int): The target location containing a secret passage.

    Returns:
        list: A list of locations representing the path, or None if no path is found.
    """

    visited = set()
    path = []

    def dfs(current_location):
        nonlocal path  # Allows modification of the outer scope 'path'
        visited.add(current_location)
        path.append(current_location)

        if current_location == target_location:
            return True  # Path found

        for neighbor in hogwarts_map.graph[current_location]:
            if neighbor not in visited:
                if dfs(neighbor):  # Recursively explore neighbors
                    return True  # Path found through this neighbor
        # Backtrack: If path doesn't lead to target, remove current node
        path.pop()
        return False

    if dfs(start_location):
        return path  # Return the found path
    else:
        return None
