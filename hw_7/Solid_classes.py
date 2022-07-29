class Group:
    def __init__(self):
        self.group_n = list()

    def add_to_group(self, obj):
        self.group_n.append(obj)

    def print_group_len(self):
        return len(self.group_n)

    def return_group(self):
        return self.group_n


class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def __str__(self):
        return self.__class__.__name__

    def can_walk(self):
        print(f'{self}, can walk..')

    def can_run(self):
        print(f'{self}, can run..')

    def can_eat(self):
        print(f'{self}, can eat..')

    def can_sleep(self):
        print(f'{self}, can sleep..')


class Teacher(Person):
    def __init__(self, name=None, age=None, stage=0):
        super().__init__(name, age)
        self.stage = stage

    def can_teach(self):
        print(f'{self}, can teach..')

    def can_sleep(self):
        super().can_sleep()
        print('"Хоть не просыпайся, чтобы их не видеть..."\n')


class Student(Person):
    def __init__(self, name=None, age=None, course=0):
        super().__init__(name, age)
        self.course = course

    def can_study(self):
        print(f'{self},, can study..')

    def can_eat(self):
        super().can_eat()
        print('"Ем как не в себя!"\n')


St_1 = Student('John', 21, 4)
print(St_1.name, St_1.age, St_1.course)
St_1.can_study()
St_1.can_eat()
Tch_1 = Teacher('Ben', 47, 10)
print(Tch_1.name, Tch_1.age, Tch_1.stage)
Tch_1.can_teach()
Tch_1.can_sleep()

group = Group()
group.add_to_group(St_1)
group.add_to_group(Tch_1)
print(f'Group has {group.print_group_len()} persons.')

to_print = group.return_group()
for person in to_print:
    print(person, person.name, person.age, 'years old.')
