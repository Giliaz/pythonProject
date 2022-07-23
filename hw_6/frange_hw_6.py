class frange:
    def __init__(self, *args):
        self.step = None
        self.end = None
        self.start = None
        self.list_ = []
        self.set_params(args)

    def set_params(self, args):
        if len([*args]) == 1:
            self.end = args[0]
            if type(self.end) is float:
                self.end = int(self.end) + 1
            self.list_ = [num for num in range(self.end)]
        elif len([*args]) == 2:
            self.start, self.end = args
            if type(self.start) is int:
                if (type(self.end)) is float:
                    self.end = int(self.end) + 1
                self.list_ = [num for num in range(self.start, self.end)]
            else:
                if self.end > self.start:
                    around = len(str(float(self.start)).split('.')[1])
                    self.list_ = [float(self.start)]
                    while self.end > self.start + 1:
                        self.start = round(self.start + 1, around)
                        self.list_.append(self.start)
        elif len([*args]) == 3:
            self.start, self.end, self.step = args
            if type(self.start) == int and type(self.end) == int and type(self.step) == int:
                self.list_ = [num for num in range(self.start, self.end, self.step)]
            else:
                if len(str(float(self.step)).split('.')[1]) > len(str(float(self.start)).split('.')[1]):
                    around = len(str(float(self.step)).split('.')[1])
                else:
                    around = len(str(float(self.start)).split('.')[1])
                if self.start < self.end and self.step > 0:
                    self.list_ = [float(self.start)]
                    while self.end > self.start + self.step:
                        self.start = round(self.start + self.step, around)
                        self.list_.append(self.start)
                if self.start > self.end and self.step < 0:
                    self.list_ = [float(self.start)]
                    while self.end < self.start + self.step:
                        self.start = round(self.start + self.step, around)
                        self.list_.append(self.start)

        else:
            raise TypeError(f"frange() params expected at least from 1 to 3 argument, got {len(args)}")

    def __iter__(self):
        return iter(self.list_)


a = frange(12.367, 5.121, -0.121)
for i in a:
    print(i)
