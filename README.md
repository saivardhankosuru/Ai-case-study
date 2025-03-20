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
