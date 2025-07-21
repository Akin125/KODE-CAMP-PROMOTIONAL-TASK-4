# student.py
class Student:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects  # Dictionary of subject: score
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()

    def calculate_average(self):
        return sum(self.subjects.values()) / len(self.subjects)

    def calculate_grade(self):
        avg = self.average
        if avg >= 70:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 50:
            return "C"
        elif avg >= 45:
            return "D"
        else:
            return "F"

    def to_dict(self):
        return {
            "name": self.name,
            "subjects": self.subjects,
            "average": self.average,
            "grade": self.grade
        }
