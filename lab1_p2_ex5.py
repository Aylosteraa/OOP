from collections import OrderedDict


class Student:

    def __init__(self, name, surname, book_number, grades):
        self.name = name
        self.surname = surname
        self.book_number = book_number
        self.grades = grades


class Group:

    def name_surname(self, values):
        for x in values:
            if values.count(x.name) > 1 or values.count(x.surname) > 1:
                values.remove(x)
        num = []
        for i in range(len(values)):
            if i + 1 <= 20:
                num.append(values[i])
        return num

    def average(self, values):
        aver = {}
        for i in values:
            average = sum(i.grades)/len(i.grades)
            print(i.name, i.surname, average, sep=' ')
            aver.update({average: i.surname})
        dict1 = OrderedDict(sorted(aver.items()))
        count = 0
        print("TOP 5")
        for key in dict1:
            count += 1
            for i in values:
                if dict1[key] == i.surname:
                    print(i.name, i.surname, key, sep=' ')
            if count == 5:
                break


stud = []
stud.append(Student("Alex", "Smith", 1222, [10, 5, 7, 10, 12]))
stud.append(Student("Kate", "Miller", 1223, [10, 10, 9, 10, 12]))
stud.append(Student("Lucy", "Cupper", 1224, [8, 6, 7, 10, 4]))
stud.append(Student("David", "Jones", 1225, [10, 12, 10, 10, 12]))
stud.append(Student("Harry", "Wilson", 1226, [2, 5, 7, 12, 12]))
stud.append(Student("Will", "Brown", 1227, [4, 5, 6, 10, 12]))
stud.append(Student("Sam", "Davies", 1228, [6, 5, 6, 6, 8]))

group = Group()
student = group.name_surname(stud)
group.average(student)



