import pygame
from collections import deque
import heapq

class Agent(pygame.sprite.Sprite):
    def __init__(self, environment, grid_size, algorithm="UCS"):
        super().__init__()
        self.image = pygame.Surface((grid_size, grid_size))
        self.image.fill((0, 0, 255))  # Agent color is blue
        self.rect = self.image.get_rect()
        self.grid_size = grid_size
        self.environment = environment
        self.position = [0, 0]  # Starting at the top-left corner of the grid
        self.rect.topleft = (0, 0)
        self.task_completed = 0
        self.completed_tasks = []
        self.path = []  # List of positions to follow
        self.moving = False  # Flag to indicate if the agent is moving
        self.algorithm = algorithm  # Either "UCS" or "A*"
        self.total_path_cost = 0  # Tracks the total path cost

    def move(self):
        """Move the agent along the path and update the path cost."""
        if self.path:
            next_position = self.path.pop(0)
            self.position = list(next_position)
            self.rect.topleft = (self.position[0] * self.grid_size, self.position[1] * self.grid_size)
            self.total_path_cost += 1  # Increment cost for each move
            self.check_task_completion()
        else:
            self.moving = False  # Stop moving when path is exhausted

    def check_task_completion(self):
        """Check if the agent has reached a task location."""
        position_tuple = tuple(self.position)
        if position_tuple in self.environment.task_locations:
            task_number = self.environment.task_locations.pop(position_tuple)
            self.task_completed += 1
            self.completed_tasks.append(task_number)

    def find_nearest_task(self):
        """Find the nearest task based on the chosen algorithm (UCS or A*)."""
        nearest_task = None
        shortest_path = None
        for task_position in self.environment.task_locations.keys():
            path = self.find_path_to(task_position)
            if path:
                if not shortest_path or len(path) < len(shortest_path):
                    shortest_path = path
                    nearest_task = task_position
        if shortest_path:
            self.path = shortest_path[1:]  # Exclude the current position
            self.moving = True

    def find_path_to(self, target):
        """Find a path to the target position using UCS or A*."""
        if self.algorithm == "UCS":
            return self.ucs_path_to(target)
        elif self.algorithm == "A*":
            return self.astar_path_to(target)
        else:
            raise ValueError("Unsupported algorithm: " + self.algorithm)

    def ucs_path_to(self, target):
        """Use Uniform Cost Search (UCS) to find the shortest path to the target."""
        start = tuple(self.position)
        goal = target
        queue = deque([[start]])
        visited = set()
        visited.add(start)

        while queue:
            path = queue.popleft()
            x, y = path[-1]

            if (x, y) == goal:
                return path

            neighbors = self.get_neighbors(x, y)
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
        return None  # No path found

    def astar_path_to(self, target):
        """Use A* Search to find the shortest path to the target."""
        start = tuple(self.position)
        goal = target
        open_set = []
        heapq.heappush(open_set, (0, [start]))  # Priority queue with (cost, path)
        visited = set()
        visited.add(start)

        while open_set:
            _, path = heapq.heappop(open_set)
            x, y = path[-1]

            if (x, y) == goal:
                return path

            neighbors = self.get_neighbors(x, y)
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    cost = len(new_path) + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (cost, new_path))
        return None  # No path found

    def get_neighbors(self, x, y):
        """Get walkable neighboring positions."""
        neighbors = []
        directions = [("up", (0, -1)), ("down", (0, 1)), ("left", (-1, 0)), ("right", (1, 0))]
        for _, (dx, dy) in directions:
            nx, ny = x + dx, y + dy
            if self.environment.is_within_bounds(nx, ny) and not self.environment.is_barrier(nx, ny):
                neighbors.append((nx, ny))
        return neighbors

    def heuristic(self, position, goal):
        """Calculate the heuristic (Manhattan distance) for A*."""
        px, py = position
        gx, gy = goal
        return abs(px - gx) + abs(py - gy)
