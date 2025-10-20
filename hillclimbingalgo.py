import random
import numpy as np
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, node, neighbor):
        if node not in self.adj_list:
            self.adj_list[node] = []
        self.adj_list[node].append(neighbor)

    def get_neighbors(self, node):
        return self.adj_list.get(node, [])

# Objective Function
def objective_function(x):
    return -x**3+ x  # Quadratic function to maximize

# Heuristic Function
def heuristic(x):
    return 2**3*x  # Derivative (gradient)

# Hill Climbing with Iteration Printing
def hill_climb(start_x, step_size=0.1, max_iterations=1500):
    current_x = start_x
    current_value = objective_function(current_x)
    x_history = [current_x]
    y_history = [current_value]
    heuristic_values = [heuristic(current_x)]
    graph = Graph()

    print("\nStarting Hill Climbing...\n")
    print(f"Initial x = {current_x:.4f}, f(x) = {current_value:.4f}\n")

    for iteration in range(1, max_iterations + 1):
        neighbors = [current_x + step_size, current_x - step_size]
        best_neighbor = current_x
        best_value = current_value

        print(f"Iteration {iteration}:")
        print(f"  Current x = {current_x:.4f}, f(x) = {current_value:.4f}")
        print(f"  Possible Neighbors: {', '.join([f'{n:.4f}' for n in neighbors])}")

        for next_x in neighbors:
            next_value = objective_function(next_x)
            graph.add_edge(current_x, next_x)
            print(f"    → Neighbor x = {next_x:.4f}, f(x) = {next_value:.4f}")
            if next_value > best_value:
                best_neighbor, best_value = next_x, next_value

        if best_value > current_value:
            print(f"   Moving to better neighbor: x = {best_neighbor:.4f}, f(x) = {best_value:.4f}\n")
            current_x, current_value = best_neighbor, best_value
            x_history.append(current_x)
            y_history.append(current_value)
            heuristic_values.append(heuristic(current_x))
        else:
            print("   No better neighbor found. Reached a peak.\n")
            break

    print(" Hill Climbing Completed!")
    print(f"Best x = {current_x:.4f}, Best f(x) = {current_value:.4f}\n")
    return current_x, current_value, x_history, y_history, heuristic_values, graph


# RUN HILL CLIMBING
start_x = random.uniform(-7, 4)  # Start at random point
best_x, best_value, x_hist, y_hist, h_values, graph = hill_climb(start_x)

# Plotting the function and path
x_vals = np.linspace(-2, 4, 100)
y_vals = objective_function(x_vals)

plt.figure(figsize=(10, 5))
plt.plot(x_vals, y_vals, label='Objective Function')
plt.scatter(x_hist, y_hist, color='red', label='Path Taken', zorder=3)
plt.scatter(best_x, best_value, color='green', marker='X', s=100, label='Best Solution', zorder=4)
plt.xlabel('x')
plt.ylabel('Objective Value')
plt.title('Hill Climbing Optimization')
plt.legend()
plt.grid()
plt.axis("off")
plt.show()

print(f"Best x: {best_x:.4f}, Best value: {best_value:.4f}")
