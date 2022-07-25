class frange:
    def __init__(self, *args):
        if len([*args]) == 1:
            self.end = args[0]
            self.start = 0
            self.step = 1
            self.around = 0
            self.flag = True
        elif len([*args]) == 2:
            self.start, self.end = args
            self.step = 1
            self.flag = True
            if type(self.start) == float:
                self.around = len(str(self.start).split('.')[1])
            else:
                self.around = 0
        elif len([*args]) == 3:
            self.start, self.end, self.step = args
            if self.start <= self.end:
                self.flag = True
            else:
                self.flag = False
            if type(self.start) == float:
                self.around = len(str(self.start).split('.')[1])
            else:
                self.around = 0
            if type(self.step) == float:
                if self.around < len(str(self.step).split('.')[1]):
                    self.around = len(str(self.step).split('.')[1])
        else:
            raise TypeError(f"frange() params expected at least from 1 to 3 argument, got {len(args)}")

    def __next__(self):
        if self.flag and self.step > 0:
            if self.start >= self.end:
                raise StopIteration('Stop')
            else:
                result = round(self.start, self.around)
                self.start += self.step
                return result
        elif self.flag is False and self.step < 0:
            if self.start <= self.end:
                raise StopIteration('Stop')
            else:
                result = round(self.start, self.around)
                self.start += self.step
                return result
        else:
            raise StopIteration('Stop')

    def __iter__(self):
        return self


for i in frange(1.33, 0.7, -0.025):
    print(i)


