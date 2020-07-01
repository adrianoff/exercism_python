from typing import List

my_students = [
    'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry'
]

flowers = {
    'G': 'Grass',
    'C': 'Clover',
    'R': 'Radishes',
    'V': 'Violets'
}


class Garden:
    def __init__(self, diagram: str, students: List = None):
        self.diagram = [c for c in [line for line in diagram.split()]]
        if students is None:
            self.students = my_students
        else:
            self.students = students

        self.students.sort()

    def plants(self, name: str) -> List:
        ind = self.students.index(name)

        plants = []
        for line in self.diagram:
            plants.append(flowers[line[ind * 2]])
            plants.append(flowers[line[(ind * 2) + 1]])

        return plants
