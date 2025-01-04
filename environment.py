import random

class Environment:
    def __init__(self, num_slots, num_students, num_classes):
        self.num_slots = num_slots
        self.num_students = num_students
        self.num_classes = num_classes
        self.classes = self.generate_classes()
        self.students = self.generate_students()

    def generate_classes(self):
        """Generate classes with random durations and priorities."""
        return [
            {
                "id": f"P{i+1}",
                "duration": random.choice([1, 2]),
                "priority": random.randint(1, 5),
            }
            for i in range(self.num_classes)
        ]

    def generate_students(self):
        """Generate students with random availability and preferences."""
        return [
            {
                "id": f"S{i+1}",
                "availability": [random.choice([True, False]) for _ in range(self.num_slots)],
                "preferences": [random.uniform(0.5, 1.5) for _ in range(self.num_slots)],
            }
            for i in range(self.num_students)
        ]

    def generate_random_schedule(self):
        """Generate a random schedule assigning classes to time slots and students."""
        schedule = []
        for cls in self.classes:
            assigned = False
            while not assigned:
                slot = random.randint(0, self.num_slots - 1)
                student = random.randint(0, self.num_students - 1)
                if self.students[student]["availability"][slot]:
                    schedule.append({"class": cls, "slot": slot, "student": student})
                    assigned = True
        return schedule
