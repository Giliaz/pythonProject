
class сolorized:
    def __init__(self, key):
        self.key = key
        self.colors = {'WHITE': '\033[97m',
                       'GRAY': '\033[90m',
                       'RED': '\033[91m',
                       'GREEN': '\033[92m',
                       'YELLOW': '\033[93m',
                       'ORANGE': '\033[94m',
                       'BLUE': '\033[95m',
                       'CYAN': '\033[96m'}

    def __enter__(self):
        print(self.colors[self.key])
        return self.key

    def __exit__(self, exc_type, exc_val, exc_tb):
        Exception(exc_type)
        self.key = 'WHITE'
        print(self.colors[self.key])


with сolorized('RED') as key:
    print(f'Printed in {key} colors')
print("Printed default color")





