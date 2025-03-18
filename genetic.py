¸import random

# Define houses and their ideal trait profiles
houses = {
    "Gryffindor": {"bravery": 9, "intelligence": 5, "ambition": 6, "loyalty": 7},
    "Ravenclaw": {"bravery": 5, "intelligence": 9, "ambition": 6, "loyalty": 6},
    "Slytherin": {"bravery": 6, "intelligence": 6, "ambition": 9, "loyalty": 5},
    "Hufflepuff": {"bravery": 6, "intelligence": 5, "ambition": 4, "loyalty": 9},
}

# Generate random students with traits
def generate_student():
    return {
        "bravery": random.randint(1, 10),
        "intelligence": random.randint(1, 10),
        "ambition": random.randint(1, 10),
        "loyalty": random.randint(1, 10),
    }

# Fitness function: measures how well a sorting rule sorts students correctly
def fitness_function(sorting_rule):
    score = 0
    for _ in range(20):  # Test with 20 random students
        student = generate_student()
        assigned_house = sort_student(student, sorting_rule)
        best_match = get_best_house(student)
        if assigned_house == best_match:
            score += 1
    return score

# Determines the best house for a student based on trait matching
def get_best_house(student):
    best_house = None
    best_score = float('-inf')
    for house, traits in houses.items():
        score = sum(student[trait] * traits[trait] for trait in student)
        if score > best_score:
            best_score = score
            best_house = house
    return best_house

# Sorts a student based on a given rule set
def sort_student(student, rule):
    best_house = None
    best_score = float('-inf')
    for house, weight in rule.items():
        score = sum(student[trait] * weight[trait] for trait in student)
        if score > best_score:
            best_score = score
            best_house = house
    return best_house

# Generate an initial population of sorting rules
def generate_population(size=10):
    population = []
    for _ in range(size):
        rule = {house: {trait: random.uniform(0, 10) for trait in houses["Gryffindor"]} for house in houses}
        population.append(rule)
    return population

# Crossover function: combines two sorting rules
def crossover(parent1, parent2):
    child = {}
    for house in houses:
        child[house] = {trait: random.choice([parent1[house][trait], parent2[house][trait]]) for trait in houses[house]}
    return child

# Mutation function: randomly changes some values in the rule
def mutate(rule, mutation_rate=0.1):
    for house in houses:
        for trait in houses[house]:
            if random.random() < mutation_rate:
                rule[house][trait] += random.uniform(-1, 1)  # Small change
    return rule

# Genetic Algorithm
def genetic_algorithm(generations=100, population_size=10):
    population = generate_population(population_size)
    
    for gen in range(generations):
        # Evaluate fitness
        scored_population = [(rule, fitness_function(rule)) for rule in population]
        scored_population.sort(key=lambda x: x[1], reverse=True)  # Sort by fitness

        # Keep the top half
        top_half = [rule for rule, _ in scored_population[:population_size // 2]]

        # Generate new population using crossover and mutation
        new_population = top_half.copy()
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(top_half, 2)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population
        print(f"Generation {gen+1}: Best fitness = {scored_population[0][1]}")

    # Return the best sorting rule
    return scored_population[0][0]

# Run the genetic algorithm
best_sorting_rule = genetic_algorithm()

# Test it with a new student
new_student = generate_student()
assigned_house = sort_student(new_student, best_sorting_rule)
print("\nNew Student Traits:", new_student)
print("Sorted into:", assigned_house)

