

# Optimization using Genetic Algorithms

This repository contains a Python-based implementation of a task assignment optimization algorithm using genetic algorithms. The program assigns classes to students based on their availability and preferences, while visualizing the schedules dynamically using Pygame.

---

## Features

- **Class Assignment**: Assigns classes to students based on their availability and preferences.
- **Genetic Algorithm**:
  - Generates an initial random population of schedules.
  - Evaluates fitness based on student preferences.
  - Implements crossover and mutation for schedule evolution.
  - Utilizes roulette wheel selection for parent selection.
- **Visualization**: 
  - Displays student schedules and preferences in a grid.
  - Highlights classes based on priority.
  - Tracks and displays generation statistics and fitness scores.
- **Customizability**: Parameters such as number of students, slots, classes, and mutation rates are easily adjustable.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/task-assignment-genetic-algorithm.git
   cd task-assignment-genetic-algorithm
   ```
2. Install the required dependencies:
   ```bash
   pip install pygame
   ```

---

## Usage

Run the script to start the simulation:
```bash
python main.py
```

The simulation visualizes schedules for each generation, showing improvements in task assignments based on student preferences.

### Parameters

You can modify the following parameters in the `main` function to customize the simulation:
- `num_slots`: Number of time slots available.
- `num_students`: Number of students.
- `num_classes`: Number of classes.
- `population_size`: Size of the genetic algorithm population.
- `mutation_rate`: Probability of mutation in schedules.
- `num_generations`: Number of generations to simulate.

---

## File Structure

- `main.py`: Main script to run the simulation.
- `environment.py`: Defines the `Environment` class for managing students, classes, and schedules.
- `Student` Class: Represents an individual student with attributes like availability, preferences, and schedules.

---

## How It Works

1. **Environment Setup**:
   - Randomly generates classes with priorities and durations.
   - Randomly generates student availability and preferences.

2. **Genetic Algorithm**:
   - Initializes a random population of schedules.
   - Evaluates fitness of schedules based on student preferences.
   - Evolves schedules over generations using selection, crossover, and mutation.

3. **Visualization**:
   - Displays a grid with student preferences and assigned classes.
   - Highlights high-priority classes in blue.
   - Shows generation statistics such as best fitness and maximum fitness achieved.

---

## Example Output

During the simulation, you'll see a visual representation of schedules:
- **Student Preferences**: Displayed as numeric values in grid cells.
- **Assigned Classes**: Highlighted in grid cells with their IDs and durations.
- **Generation Stats**: Shown at the top of the window.

---

## Future Improvements

- Add support for real-world constraints (e.g., max classes per student).
- Enhance visualization with better UI/UX.
- Implement multi-threading for faster simulations.

---

Start exploring task optimization with genetic algorithms today! 🎉
