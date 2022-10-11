class Student:

    def __init__(self, name, surname, book_number, grades):
        self.name = name
        self.surname = surname
        self.book_number = book_number
        self.grades = grades

    def average(self):
        average = sum(self.grades) / len(self.grades)
        return average

    def __str__(self):
        return f'{self.name} {self.surname} {self.book_number} {self.grades}    {self.average()}\n'

class Group:

    def __init__(self, group, max = 20):
        if not isinstance(max, int):
            raise TypeError()
        if len(group) > max:
            raise Exception("Group is full")
        self.__group = group
        self.__max = max

    def add_student(self, student):
        if len(self.__group) < self.__max and isinstance(student, Student):
            for i in self.__group:
                if student.name == i.name or student.surname == i.surname:
                    return i
            self.__group.append(student)
        else:
            return f'{student} can not be added to group'

    def top_students(self):
        self.__group.sort(reverse=True, key=lambda st: st.average())
        self.__group = self.__group[0:5]

    def __str__(self):
        string = '\n'
        for i in self.__group:
            string += i.__str__()
        return f'{string}'


stud = []
stud.append(Student("Alex", "Smith", 1222, [10, 5, 7, 10, 12]))
stud.append(Student("Kate", "Miller", 1223, [10, 10, 9, 10, 12]))
stud.append(Student("Lucy", "Cupper", 1224, [8, 6, 7, 10, 4]))
stud.append(Student("David", "Jones", 1225, [10, 12, 10, 10, 12]))
stud.append(Student("Harry", "Wilson", 1226, [2, 5, 7, 12, 12]))

group = Group(stud)
print(group)

group.add_student(Student("Will", "Brown", 1227, [4, 5, 6, 10, 12]))
group.add_student(Student("Sam", "Davies", 1228, [6, 5, 6, 6, 8]))
print(group)

group.top_students()

print(group)
