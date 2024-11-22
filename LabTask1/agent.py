class Agent:
    def __init__(self, environment):
        self.environment = environment
        self.position = [0, 0] 
    def move(self, direction): 
        if direction == "up":
            self.position[1] += 10
        elif direction == "down":
            self.position[1] -= 10
        elif direction == "left":
            self.position[0] -= 10
        elif direction == "right":
            self.position[0] += 10

        self.position = self.environment.limit_position(self.position)
    def status(self):
        return self.position