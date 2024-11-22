# Agent-Environment Simulation

This Python project demonstrates a simple **Agent-Environment simulation** using **Pygame**. An agent moves within a predefined environment, interacting with boundaries and displaying its real-time position.

## Features

- **Agent Movement:** The agent can move in four directions: up, down, left, and right.
- **Environment Boundary:** Positions wrap around if the agent crosses the environment's boundaries.
- **Real-time Feedback:** The agent's position is displayed on the screen.
- **Graphical Display:** Visual representation of the environment and the agent.

## How It Works

### Core Classes

1. **`Agent`**
   - Represents the moving entity.
   - Tracks its position and interacts with the environment.

2. **`Environment`**
   - Defines the boundary for the agent.
   - Ensures position values wrap around when crossing boundaries.

### Main Features

- Pygame is used for graphical display and user input.
- The agent's position updates based on arrow key presses (`↑`, `↓`, `←`, `→`).
- The simulation displays the agent as a blue rectangle on a white background.

## Getting Started

### Prerequisites

- Python 3.6+
- Pygame library installed. Install using:
  ```bash
  pip install pygame
  ```

### Running the Simulation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/agent-environment-simulation.git
   cd agent-environment-simulation
   ```
2. Run the simulation:
   ```bash
   python main.py
   ```

3. Use arrow keys to move the agent around the environment.

### Output

- The agent (blue rectangle) moves in response to arrow keys.
- Its position is displayed at the top-left of the screen.
