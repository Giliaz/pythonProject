class frange:
    def __init__(self, *args):
        self.step = None
        self.end = None
        self.start = None
        self.list_ = []
        self.set_list(args)

    def set_list(self, args):
        if len([*args]) == 1:
            self.list_ = [i for i in range(args[0])]
        elif len([*args]) == 2:
            self.list_ = [i for i in range(args[0], args[1])]
        elif len([*args]) == 3:
            self.start = args[0]
            self.end = args[1]
            self.step = args[2]
            if self.start < self.end and self.step > 0:
                self.list_ = [self.start]
                while self.end > self.start + self.step:
                    self.start += self.step
                    self.list_.append(self.start)
            if self.start > self.end and self.step < 0:
                self.list_ = [self.start]
                while self.end < self.start + self.step:
                    self.start += self.step
                    self.list_.append(self.start)
        else:
            raise TypeError(f"range expected at least from 1 to 3 argument, got {len(args)}")

    def __iter__(self):
        return iter(self.list_)


for i in frange(10, 100, 2):
    print(i)
