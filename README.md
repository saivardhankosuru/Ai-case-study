## Case Study: Hogwarts School of Witchcraft and Wizardry

Hogwarts is a complex environment filled with magical obstacles and dynamic elements. This case study applies Artificial Intelligence (AI) search algorithms to solve problems within Hogwarts, such as navigating the castle, traversing a Triwizard Maze, and customizing a magic wand.

### Algorithm: Greedy Best-First Search (GBFS) - Finding the Philosopher's Stone

**[Link to program: `[Your_GitHub_Link_Here]`]**  (Replace with the actual link to your GBFS code file in the repository)

**Narrative:**

The Philosopher's Stone is hidden deep within Hogwarts, protected by a series of magical challenges and chambers. To find it, a student must navigate through these obstacles, using clues that indicate proximity to the stone. The search is guided by the belief that the magical energy emanating from the Stone increases as the student gets closer.

**Task:**

Implement Greedy Best-First Search (GBFS) to guide the student through the castle and chambers.  The search should prioritize locations with higher readings of magical energy, with the goal of quickly finding the Philosopher's Stone.

**Challenges:**

*   **Designing the Heuristic:** The success of GBFS depends on a well-designed heuristic function that accurately estimates the distance to the Stone. The heuristic should consider the magical energy levels, proximity to known challenges, and other relevant factors.
*   **Magical Hazards:**  The path may be blocked by magical creatures or spells guarding the chamber, requiring the student to bypass them or find alternative routes.
*   **False Leads:**  Decoy rooms may contain similar magical energy, requiring the student to evaluate their options and avoid unnecessary detours.

**Extension:**

*   **Multi-Objective Navigation:** Introduce secondary objectives, such as collecting protective charms or solving riddles along the way, to make the search more complex.

**Algorithm Flowchart:**

1.  **Define Heuristic Function:** Create a function `h(node, goal)` that estimates the distance to the Philosopher's Stone based on magical energy (and potentially other factors).
2.  **Initialize Priority Queue:** Add the starting location to a priority queue, with priority equal to `h(start, goal)`.
3.  **While Priority Queue is not Empty:**
    *   a. **Dequeue Node:** Remove the node with the lowest heuristic value from the priority queue.
    *   b. **Goal Check:** If the node is the goal (Philosopher's Stone location), return the path.
    *   c. **Expand Node:** Find the neighbors of the current node.
    *   d. **Add Neighbors to Queue:** For each neighbor:
        *   Calculate `h(neighbor, goal)`.
        *   Add the neighbor to the priority queue, with priority equal to `h(neighbor, goal)`.
4.  **No Path Found:** If the priority queue is empty and the goal has not been reached, return failure.

### **Expected Output:**
Path found: ['Entrance Hall', 'Chamber 1', 'Secret Passage' ...  'Philosopher's Stone Chamber']  # Actual path depends on implementation


# **Sorting Hat Genetic Algorithm**

## **Introduction**

The goal of this program is to simulate the process of sorting students into Hogwarts houses based on their traits using a genetic algorithm. The houses and their ideal trait profiles (bravery, intelligence, ambition, loyalty) serve as the baseline for sorting. The algorithm evolves over several generations to improve the sorting accuracy by optimizing a sorting rule that matches a student’s traits to the house traits. 

## **Breakdown of the Components**

### **1. Houses and Ideal Trait Profiles**

The four Hogwarts houses are defined with specific traits that represent the ideal qualities of students belonging to that house. Each house is characterized by:
- **Gryffindor**: High bravery, moderate intelligence and ambition, moderate loyalty.
- **Ravenclaw**: High intelligence, moderate bravery, ambition, and loyalty.
- **Slytherin**: High ambition, moderate bravery and intelligence, low loyalty.
- **Hufflepuff**: High loyalty, moderate bravery, low ambition, and intelligence.

Each house's profile is represented as a dictionary, with traits (bravery, intelligence, ambition, loyalty) and associated values ranging from 1 to 10.

### **2. Random Student Generation**

The function `generate_student()` creates random students with trait values (bravery, intelligence, ambition, loyalty), each ranging from 1 to 10. These random traits serve as input for the sorting algorithm, and each student must be assigned to the house that best fits their individual traits.

### **3. Fitness Function**

The fitness function evaluates how well a sorting rule sorts students into their correct houses. It does this by:
- Generating 20 random students.
- Sorting each student using a sorting rule.
- Comparing the assigned house to the "best house" (the house that best matches the student’s traits using a scoring system).
- If the assigned house matches the best house, the sorting rule gets a fitness point. The total number of matches gives the score for the sorting rule.

### **4. Best House Determination**

The function `get_best_house()` calculates which house best suits a student's traits. It does so by computing a weighted score for each house based on the student's trait values and the house's ideal trait profile. The house with the highest score is considered the best match.

### **5. Sorting Function**

The function `sort_student()` applies a given sorting rule to a student’s traits to determine which house they should be assigned to. The sorting rule is a dictionary of weights for each house, dictating how much importance should be given to each trait when evaluating a student’s house.

### **6. Genetic Algorithm**

The core of the program is the genetic algorithm that evolves sorting rules over multiple generations. The steps of the genetic algorithm are as follows:
- **Initial Population**: A random population of sorting rules is generated.
- **Fitness Evaluation**: The fitness of each sorting rule is evaluated based on how well it sorts a set of random students.
- **Selection**: The top-performing sorting rules (the top half) are selected to form the next generation.
- **Crossover**: New sorting rules are created by combining traits from two parent rules. The crossover mixes characteristics of both parents in order to create a new rule.
- **Mutation**: Some values in the sorting rules are mutated by adding small random changes to introduce variation.
- **Evolution**: The process of selection, crossover, and mutation is repeated for multiple generations, improving the sorting rules over time.

### **7. Final Sorting Rule**

After a set number of generations, the best sorting rule is returned, representing the sorting rule that best matches students to their ideal houses.

### **8. Testing the Sorting Rule**

The program tests the final sorting rule by applying it to a new randomly generated student. The traits of the new student are printed, and the house they are sorted into (using the best sorting rule) is displayed.

## **Output**

Generation 1: Best fitness = 10
Generation 2: Best fitness = 12
Generation 3: Best fitness = 13
Generation 4: Best fitness = 14
Generation 5: Best fitness = 15
Generation 6: Best fitness = 15
Generation 7: Best fitness = 15
Generation 8: Best fitness = 16
Generation 9: Best fitness = 16
Generation 10: Best fitness = 16
Generation 11: Best fitness = 16
Generation 12: Best fitness = 16
Generation 13: Best fitness = 16
Generation 14: Best fitness = 16
Generation 15: Best fitness = 16
Generation 16: Best fitness = 16
Generation 17: Best fitness = 16
Generation 18: Best fitness = 16
Generation 19: Best fitness = 16
Generation 20: Best fitness = 16
Generation 21: Best fitness = 16
Generation 22: Best fitness = 16
Generation 23: Best fitness = 16
Generation 24: Best fitness = 16
Generation 25: Best fitness = 16
Generation 26: Best fitness = 16
Generation 27: Best fitness = 16
Generation 28: Best fitness = 16
Generation 29: Best fitness = 16
Generation 30: Best fitness = 16
Generation 31: Best fitness = 16
Generation 32: Best fitness = 16
Generation 33: Best fitness = 16
Generation 34: Best fitness = 16
Generation 35: Best fitness = 16
Generation 36: Best fitness = 16
Generation 37: Best fitness = 16
Generation 38: Best fitness = 16
Generation 39: Best fitness = 16
Generation 40: Best fitness = 16
Generation 41: Best fitness = 16
Generation 42: Best fitness = 16
Generation 43: Best fitness = 16
Generation 44: Best fitness = 16
Generation 45: Best fitness = 16
Generation 46: Best fitness = 16
Generation 47: Best fitness = 16
Generation 48: Best fitness = 16
Generation 49: Best fitness = 16
Generation 50: Best fitness = 16
Generation 51: Best fitness = 16
Generation 52: Best fitness = 16
Generation 53: Best fitness = 16
Generation 54: Best fitness = 16
Generation 55: Best fitness = 16
Generation 56: Best fitness = 16
Generation 57: Best fitness = 16
Generation 58: Best fitness = 16
Generation 59: Best fitness = 16
Generation 60: Best fitness = 16
Generation 61: Best fitness = 16
Generation 62: Best fitness = 16
Generation 63: Best fitness = 16
Generation 64: Best fitness = 16
Generation 65: Best fitness = 16
Generation 66: Best fitness = 16
Generation 67: Best fitness = 16
Generation 68: Best fitness = 16
Generation 69: Best fitness = 16
Generation 70: Best fitness = 16
Generation 71: Best fitness = 16
Generation 72: Best fitness = 16
Generation 73: Best fitness = 16
Generation 74: Best fitness = 16
Generation 75: Best fitness = 16
Generation 76: Best fitness = 16
Generation 77: Best fitness = 16
Generation 78: Best fitness = 16
Generation 79: Best fitness = 16
Generation 80: Best fitness = 16
Generation 81: Best fitness = 16
Generation 82: Best fitness = 16
Generation 83: Best fitness = 16
Generation 84: Best fitness = 16
Generation 85: Best fitness = 16
Generation 86: Best fitness = 16
Generation 87: Best fitness = 16
Generation 88: Best fitness = 16
Generation 89: Best fitness = 16
Generation 90: Best fitness = 16
Generation 91: Best fitness = 16
Generation 92: Best fitness = 16
Generation 93: Best fitness = 16
Generation 94: Best fitness = 16
Generation 95: Best fitness = 16
Generation 96: Best fitness = 16
Generation 97: Best fitness = 16
Generation 98: Best fitness = 16
Generation 99: Best fitness = 16
Generation 100: Best fitness = 16

New Student Traits: {'bravery': 6, 'intelligence': 1, 'ambition': 4, 'loyalty': 6}
Sorted into: Hufflepuff








# **Hogwarts Map with Secret Passages**

## **Overview**

This Python project simulates the layout of Hogwarts, featuring a graph representation of key locations within the magical school. It includes basic connectivity between locations and a system for generating secret passages that allow students to navigate the castle in unexpected ways. Additionally, a **Depth-First Search (DFS)** algorithm is implemented to discover paths between locations, taking into account these secret passages.

## **Features**

- **Graph Representation of Hogwarts Locations**: Locations like the Great Hall, Library, Dungeons, etc., are connected in a way that reflects the Hogwarts layout.
- **Secret Passages**: Random secret passages are created between locations to provide hidden routes for exploration.
- **Depth-First Search (DFS)**: A DFS algorithm is implemented to find paths from one location to another, considering both regular and secret routes.

## **Classes**

### **HogwartsMap**

The `HogwartsMap` class represents the magical school and its locations. It contains methods to:
1. **Generate the Hogwarts graph** - This method creates a set of locations and their connections, simulating the structure of Hogwarts.
2. **Generate secret passages** - Randomly creates secret passages between locations, which are then incorporated into the graph.
3. **Display the graph** - Prints out the locations and their connections, as well as any generated secret passages.

#### **Methods:**
- `__init__(self, num_locations=10)`:
  - Initializes the map with a given number of locations and generates both the graph and secret passages.
  
- `generate_hogwarts_graph(self)`:
  - Generates the basic connectivity between locations, including key areas such as the Great Hall, Library, Charms Class, and more.
  
- `generate_secret_passages(self)`:
  - Randomly creates a set of secret passages and adds them to the graph.
  
- `display_graph(self)`:
  - Displays the graph’s connections and the list of secret passages for debugging and visualization purposes.

### **dfs_secret_passage_discovery**

This function performs **Depth-First Search (DFS)** to find a path between a starting location and a target location, considering the secret passages as valid routes.

#### **Arguments:**
- `hogwarts_map` (HogwartsMap): The map object containing the Hogwarts layout and secret passages.
- `start_location` (int): The starting location for the search.
- `target_location` (int): The target location to find the path to.

#### **Returns:**
- `list`: A list of locations representing the path, or `None` if no path is found.
### **OUTPUT**
Path found: ['Great Hall', 'Potions Classroom']

