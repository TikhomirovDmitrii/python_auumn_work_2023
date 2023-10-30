class Task:
    def init(self, description):
        self.description = description
        self.status = "Не решена"

class Teacher:
    def init(self, name):
        self.name = name
        self.tasks_to_assign = []

    def assign_task(self, task, pupil):
        if task in self.tasks_to_assign:
            pupil.tasks.append(task)
            self.tasks_to_assign.remove(task)
            task.status = "Назначена"
        else:
            print("Задача не найдена в списке задач для назначения.")

    def review_tasks(self, pupil):
        for task in pupil.tasks:
            task.status = "Решена"

class Pupil:
    def init(self, name):
        self.name = name
        self.tasks = []

    def solve_task(self, task):
        if task in self.tasks:
            pass

teacher = Teacher("Mikhail")
pupil1 = Pupil("Pete")
pupil2 = Pupil("Emma")
pupil3 = Pupil("Mark")

task1 = Task("OOP")
task2 = Task("Machine learning")
task3 = Task("Data Analysis")

teacher.tasks_to_assign = [task1, task2, task3]
teacher.assign_task(task1, pupil1)
teacher.assign_task(task2, pupil2)
teacher.assign_task(task3, pupil3)

pupil1.solve_task(task1)
pupil2.solve_task(task2)
pupil3.solve_task(task3)

teacher.review_tasks(pupil1)
teacher.review_tasks(pupil2)
teacher.review_tasks(pupil3)

print(f"{pupil1.name}: {pupil1.tasks[0].status}")
print(f"{pupil2.name}: {pupil2.tasks[0].status}")
print(f"{pupil3.name}: {pupil3.tasks[0].status}")