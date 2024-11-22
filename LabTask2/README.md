# Pygame AI Grid Simulation

This project is a **Pygame-based AI simulation** where an agent navigates a grid environment to complete tasks using different pathfinding algorithms: **Uniform Cost Search (UCS)** and **A***. It includes barriers, task locations, and a toggleable user interface for controlling the simulation and switching algorithms.

---

## Features

- **Grid-based environment**: The agent operates on a grid with tasks and barriers.
- **Pathfinding algorithms**:  
  - **Uniform Cost Search (UCS)**  
  - **A*  Search**  
- **Interactive UI**:  
  - Start/Restart simulation.
  - Toggle between UCS and A* algorithms.
  - Visual feedback of the agent’s current position, completed tasks, and total path cost.
- **Dynamic environment**: Randomized task and barrier placements at the start or reset.

---

## How to Run

### Prerequisites
- **Python 3.6+**
- **Pygame**: Install it using `pip install pygame`

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/pygame-ai-simulation.git
   cd pygame-ai-simulation
   ```
2. Run the simulation:
   ```bash
   python run.py
   ```

---

## How It Works

### Simulation Overview
- The environment is a grid divided into cells.  
- Barriers block paths, and tasks are randomly placed on the grid.  
- The agent starts at the top-left corner (0, 0).  

### Controls
- **Start Button**: Begins the simulation and lets the agent navigate to tasks.
- **Toggle Button**: Switches between UCS and A* algorithms, resetting the environment.
  
### Agent Behavior
- Finds the nearest task using the selected algorithm.  
- Automatically moves towards the task while avoiding barriers.  
- Updates the total path cost and task completion status upon task arrival.

---

## Code Structure

- **`agent.py`**: Implements the agent with pathfinding algorithms (UCS and A*).  
- **`environment.py`**: Defines the environment, including grid properties, tasks, and barriers.  
- **`run.py`**: Main script to initialize and run the simulation, handling UI and interactions.  

---

## Customization

### Modify the Environment
- **Number of Tasks**: Change `num_tasks` in `run.py`.  
- **Number of Barriers**: Adjust `num_barriers` in `run.py`.  

### Adjust Grid Size
- Change the `GRID_SIZE` constant in `run.py` to make cells larger or smaller.

---

## Contributions
Contributions are welcome!  
- Fork the repository.  
- Create a new branch for your feature/bugfix.  
- Submit a pull request.

Happy coding! 🎉