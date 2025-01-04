class Student:
    def __init__(self, student_id, availability, preferences):
        self.id = student_id
        self.availability = availability
        self.preferences = preferences
        self.schedule = []

    def assign_class(self, cls, slot):
        """Assign a class to this student's schedule."""
        if self.availability[slot]:
            self.schedule.append({"class": cls, "slot": slot})
            return True
        return False

    def clear_schedule(self):
        """Clear the student's schedule for a new generation."""
        self.schedule = []
