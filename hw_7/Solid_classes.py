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
    def __init__(self, *args):
        self.name, self.age, *args = args

    def __str__(self):
        return self.__class__.__name__


class Walker(Person):
    def can_walk(self):
        print(f'{self}, can walk..')


class Runner(Person):
    def can_run(self):
        print(f'{self}, can run..')


class Eater(Person):
    def can_eat(self):
        print(f'{self}, can eat..')


class Sleeper(Person):
    def can_sleep(self):
        print(f'{self}, can sleep..')


class Teacher(Walker, Runner, Eater, Sleeper):
    def __init__(self, name=None, age=None, stage=0):
        super().__init__(name, age)
        self.stage = stage

    def can_teach(self):
        print(f'{self}, can teach..')

    def can_sleep(self):
        super().can_sleep()
        print('"Хоть не просыпайся..."\n')


class Student(Walker, Runner, Eater, Sleeper):
    def __init__(self, name=None, age=None, course=0):
        super().__init__(name, age)
        self.course = course

    def can_study(self):
        print(f'{self}, can study..')

    def can_eat(self):
        super().can_eat()
        print('"Ем как не в себя.."\n')


St_1 = Student('John', 21, 4)
print(f'{St_1} {St_1.name}, age {St_1.age}, course of study {St_1.course}.')
St_1.can_study()
St_1.can_eat()
Tch_1 = Teacher('Ben', 47, 10)
print(f'{Tch_1} {Tch_1.name}, age {Tch_1.age}, teaching experience {Tch_1.stage} years.')
Tch_1.can_teach()
Tch_1.can_sleep()

group = Group()
group.add_to_group(St_1)
group.add_to_group(Tch_1)
print(f'Group has {group.print_group_len()} persons.')

to_print = group.return_group()
for person in to_print:
    print(person, person.name, person.age, 'years old.')