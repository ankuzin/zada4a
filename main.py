class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {'Python': [2, 6, 1], 'GIT': [9, 1, 7]}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

<<<<<<< HEAD
    def get_avg_grade(self):
        sum_lec = 0
        count = 0
        for course in self.grades.values():
            sum_lec += sum(course)
            count += len(course)
        return round(sum_lec / count, 2)
=======
    def get_avg_grade1(self):
        avg = 0
        for course in self.grades:
            avg += sum(self.grades[course]) / len(self.grades[course])
        return avg

    def __lt__(self, other):
        if not isinstance(other, Student):
            return f'Нет такого студента!'
        return self.get_avg_grade1() < other.get_avg_grade1()
>>>>>>> origin/master

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нет такого Студента')
            return
        return self.get_avg_grade() < other.get_avg_grade()




    def __str__(self):
        res = f'Имя: {self.name} \n Фамилия: {self.surname} \n   ' \
        f'Средняя  оценка за домашнее задание: {self.get_avg_grade()} \n'  \
        f'Курсы в процессе изучения:{ self.courses_in_progress} \n ' \
        f'Завершенные курсы:{self.finished_courses }'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {'Python': [2, 6, 1], 'GIT': [1, 8, 9]}


    def get_avg_grade(self):
<<<<<<< HEAD
        sum_lec = 0
        count = 0
        for course in self.grades.values():
            sum_lec += sum(course)
            count += len(course)
        return round(sum_lec / count, 2)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет такого лектора')
            return
        return self.get_avg_grade() < other.get_avg_grade()
=======
        avg = 0
        for course in self.grades:
            avg += sum(self.grades[course]) / len(self.grades[course])
        return avg

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return f'Нет такого лектора!'
        return self.get_avg_grade() < other.get_avg_grade()

>>>>>>> origin/master

    def __str__(self):
        res = f'Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за лекции: {self.get_avg_grade()}'
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






best_student = Student('Red', 'Fury', 'M')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['GIT']

some_student = Student('Ruoy', 'Eman', 'M')
some_student.courses_in_progress += ['Python','Git']
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

cool_reviewer = Reviewer('Some', 'Buddy')
some_reviever = Reviewer('Some', 'Buddy')

some_reviever.rate_hw(best_student, 'Python', 4)
some_reviever.rate_hw(best_student, 'GIT', 12)
some_reviever.rate_hw(some_student, 'Python', 4)
some_reviever.rate_hw(some_student, 'GIT', 12)

print(best_student < some_student)
print(cool_lecturer < some_lecturer)
<<<<<<< HEAD
print(cool_reviewer)
print(some_lecturer)
print(some_student)


=======
# print(cool_reviewer)
# print(some_lecturer)
# print(some_student)


>>>>>>> origin/master




