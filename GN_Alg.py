import random
def fitness(state):
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:
                conflicts += 1
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts
def generate_individual(n):
    return [random.randint(0, n - 1) for _ in range(n)]
def crossover(parent1, parent2):
    n = len(parent1)
    point = random.randint(1, n - 2)
    child = parent1[:point] + parent2[point:]
    return child
def mutate(individual, mutation_rate=0.1):
    n = len(individual)
    if random.random() < mutation_rate:
        col = random.randint(0, n - 1)
        individual[col] = random.randint(0, n - 1)
    return individual
def selection(population, k=3):
    selected = random.sample(population, k)
    selected.sort(key=lambda x: fitness(x))
    return selected[0]
def genetic_algorithm(n, population_size=100, generations=1000):
    population = [generate_individual(n) for _ in range(population_size)]

    for gen in range(generations):
        population.sort(key=lambda x: fitness(x))
        if fitness(population[0]) == 0:
            print(f"Solution found at generation {gen}")
            return population[0]

        new_generation = []
        elite = population[:10]
        new_generation.extend(elite)
        while len(new_generation) < population_size:
            parent1 = selection(population)
            parent2 = selection(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_generation.append(child)

        population = new_generation

    print("No perfect solution found.")
    return population[0]
if __name__ == "__main__":
    N = 8  
    solution = genetic_algorithm(N)

    print("Best Solution:", solution)
    print("Conflicts:", fitness(solution))
