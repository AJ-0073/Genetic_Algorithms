N-Queens Solver using Genetic Algorithm

This project solves the classic N-Queens problem using a Genetic Algorithm (GA).
The algorithm evolves a population of candidate solutions using selection, crossover, mutation, and elitism until a conflict-free queen arrangement is found.

Features

Uses GA components:
✔ Fitness evaluation
✔ Tournament selection
✔ One-point crossover
✔ Mutation
✔ Elitism

Works for any N (default: 8)

Simple and clean Python implementation

Prints best solution and number of conflicts

How It Works

Each solution is represented as a list of queen positions.

Fitness counts row and diagonal conflicts.

GA improves the population across generations until fitness = 0.
