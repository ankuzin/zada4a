class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {'Python': [20, 16, 21], 'GIT': [11, 11, 11]}

    def get_avg_grade(self):
        sum_lect = 0
        count = 0
        for course in self.grades.values():
            sum_lect += sum(course)
            count += len(course)
        return round(sum_lect / count, 2)

    def __str__(self):
        res = f'Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка: {self.get_avg_grade()}'
        return res





class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \n Фамилия: {self.surname} '
        return res


cool_reviewer = Reviewer('Some', 'Buddy')
print(cool_reviewer)

best_student = Student('Red', 'Fury', 'M')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['GIT']

some_student = Student('Green', 'Fury', 'M')
some_student.courses_in_progress += ['Python']
some_student.finished_courses += ['GIT']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['GIT']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['GIT']

best_student.rate_lecture(cool_lecturer, 'Python', 4)
best_student.rate_lecture(cool_lecturer, 'GIT', 12)

some_student.rate_lecture(some_lecturer, 'Python', 7)
some_student.rate_lecture(some_lecturer, 'GIT', 10)

print(some_lecturer)




