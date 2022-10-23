class Pets:
    def __init__(self):
        self.hignrun = False
        self.fly = False
        self.highjump = False

class Dog(Pets):
    def __init__(self):
        super().__init__()
        self.hignrun = True
        self.hignjump = False
        self.fly = False

class Parrot(Pets):
    def __init__(self):
        super().__init__()
        self.hignrun = False
        self.hignjump = False
        self.fly = True

class Cat(Pets):
    def __init__(self):
        super().__init__()
        self.hignrun = False
        self.hignjump = True
        self.fly = False