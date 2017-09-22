class Animal:
    def __init__(self, kind ,sound):
        self.kind = kind
        self.sound = sound

    def get_kind(self):
        return self.kind

    def info(self):
        print("Animal")
        print("kind: " + self.kind)


class Mammal(Animal):
    def __init__(self, kind, sound, weight=100, height=100, milk = True):
        super().__init__(kind, sound)
        self.weight = weight
        self.height = height
        self.milk = milk

    def info(self):
        print("Kind: " + self.kind)
        print("Weight: " + str(self.weight))
        print("Height: " + str(self.height))
        if self.milk:
            print('Gives milk')
        else:
            print('Does not give milk')

    def speak(self):
        return self.sound


class Birds(Animal):
    def __init__(self, kind, sound, weight=100, height=100, eggs=True, is_flying=False):
        super().__init__(kind, sound)
        self.weight = weight
        self.height = height
        self.eggs = eggs
        self.is_flying = is_flying

    def info(self):
        print("Kind: " + self.kind)
        print("Weight: " + str(self.weight))
        print("Height: " + str(self.height))
        if self.eggs:
            print('Gives eggs')
        else:
            print('Does not give eggs')
        if self.is_flying:
            print('Can fly')
        else:
            print("Can't fly")

    def speak(self):
        return self.sound


# animals
cow = Mammal('mammal', 'mooo', 240, 145, True)
goat = Mammal('mammal', 'meeeeah', 30, 45, True)
sheep = Mammal('mammal', 'baaaaaah', 31, 42, False)
pig = Mammal('mammal', 'meeeeah', 50, 45, True)

# birds
hen = Birds('bird', 'cococo', 3, 30, True, False)
duck = Birds('bird', 'cococo', 3, 25, True, True)
goose = Birds('bird', 'cococo', 5, 35, True, False)

print(cow.speak())
print(cow.info())
print(hen.info())

