import pygame
import random
from environment import Environment

def initialize_population(env, population_size):
    """Generate an initial population of random schedules."""
    return [env.generate_random_schedule() for _ in range(population_size)]

def evaluate_fitness(env, schedule):
    """Calculate the fitness of a schedule based on student preferences."""
    fitness = 0
    for entry in schedule:
        student = entry["student"]
        slot = entry["slot"]
        fitness += env.students[student]["preferences"][slot]
    return fitness

def select_parents(population, fitness_scores):
    """Select two parents using roulette wheel selection."""
    total_fitness = sum(fitness_scores)
    probabilities = [fitness / total_fitness for fitness in fitness_scores]
    parents = random.choices(population, weights=probabilities, k=2)
    return parents

def crossover(parent1, parent2):
    """Perform crossover between two parents to produce a child."""
    child = []
    crossover_point = len(parent1) // 2
    child.extend(parent1[:crossover_point])
    child.extend(parent2[crossover_point:])
    return child

def mutate(schedule, mutation_rate, env):
    """Mutate a schedule with a given mutation rate."""
    for entry in schedule:
        if random.random() < mutation_rate:
            entry["slot"] = random.randint(0, env.num_slots - 1)
            entry["student"] = random.randint(0, env.num_students - 1)

def visualize_schedule(env, schedule, generation, fitness, max_fitness):
    """Visualize the schedule using Pygame."""
    pygame.init()
    screen = pygame.display.set_mode((1100, 700))
    pygame.display.set_caption("Task Assignment Visualization")

    screen.fill((200, 200, 200))
    font = pygame.font.Font(None, 28)

    # Display generation and fitness
    gen_text = font.render(f"Generation: {generation}", True, (0, 0, 0))
    fitness_text = font.render(f"Best Fitness (Current): {fitness:.2f}", True, (0, 0, 0))
    max_fitness_text = font.render(f"Max Fitness Achieved: {max_fitness:.2f}", True, (0, 0, 0))
    screen.blit(gen_text, (800, 10))
    screen.blit(fitness_text, (800, 40))
    screen.blit(max_fitness_text, (800, 70))

    # Grid setup
    cell_width = 60
    cell_height = 60
    margin = 0
    x_offset = 200
    y_offset = 150

    # Draw slot headers
    for slot in range(env.num_slots):
        header_text = font.render(f"Slot {slot+1}", True, (0, 0, 0))
        screen.blit(header_text, (x_offset + slot * (cell_width + margin), y_offset - 40))

    # Draw grid and preferences
    for student_id, student in enumerate(env.students):
        for slot in range(env.num_slots):
            x = x_offset + slot * (cell_width + margin)
            y = y_offset + student_id * (cell_height + margin)

            rect = pygame.Rect(x, y, cell_width, cell_height)
            pygame.draw.rect(screen, (255, 255, 255), rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

            # Display preferences
            preference = student["preferences"][slot]
            text = font.render(f"{preference:.2f}", True, (0, 0, 0))
            screen.blit(text, (x + 5, y + 5))

    # Fill grid with schedule
    for entry in schedule:
        cls = entry["class"]
        slot = entry["slot"]
        student = entry["student"]

        x = x_offset + slot * (cell_width + margin)
        y = y_offset + student * (cell_height + margin)

        rect = pygame.Rect(x, y, cell_width, cell_height)
        color = (0, 0, 255) if cls["priority"] >= 4 else (180, 180, 180)

        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 2)

        text = font.render(f"{cls['id']} {cls['duration']}h", True, (255, 255, 255))
        screen.blit(text, (x + 5, y + 25))

    pygame.display.flip()
    pygame.time.delay(1000)

def main():
    # Simulation parameters
    num_slots = 8
    num_students = 5
    num_classes = 5
    population_size = 50
    mutation_rate = 0.1
    num_generations = 100
    delay = 1000  # ms

    # Initialize environment
    env = Environment(num_slots, num_students, num_classes)

    # Initialize population
    population = initialize_population(env, population_size)
    max_fitness = 0

    for generation in range(1, num_generations + 1):
        # Evaluate fitness of each individual in the population
        fitness_scores = [evaluate_fitness(env, schedule) for schedule in population]

        # Find the best schedule
        best_fitness = max(fitness_scores)
        max_fitness = max(max_fitness, best_fitness)
        best_schedule = population[fitness_scores.index(best_fitness)]

        # Visualize the best schedule
        visualize_schedule(env, best_schedule, generation, best_fitness, max_fitness)

        # Create a new population
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = select_parents(population, fitness_scores)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate, env)
            new_population.append(child)

        population = new_population

if __name__ == "__main__":
    main()
