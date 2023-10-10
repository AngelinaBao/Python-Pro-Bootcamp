class Animal:
    def __init__(self):
        self.num_eyes = 2
        self.num_mouth = 1

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("But doing it in water.")

    def swim(self):
        print("Moving in water.")


fish = Fish()
fish.breathe()
