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

## **Example Output**

The final output will display the traits of a newly generated student along with the house they have been sorted into using the optimized sorting rule. For example:








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

## **Usage Example**

### **1. Create a Hogwarts Map**

```python
# Initialize a map of Hogwarts with 10 locations
hogwarts_map = HogwartsMap(num_locations=10)

# Display the graph and secret passages
hogwarts_map.display_graph()
