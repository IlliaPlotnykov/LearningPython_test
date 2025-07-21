class Animal:
    def __init__(self, paws, hooves, name, sound, horns):
        self.paws = paws
        self.hooves = hooves
        self.name = name
        self.sound = sound
        self.horns = horns

    def make_sound(self):
        return f"{self.name} says {self.sound}"


class Paws(Animal):
    def __init__(self, name, sound):
        super().__init__(paws=4, hooves=0, name=name, sound=sound, horns=0)


class Hooves(Animal):
    def __init__(self, name, sound):
        super().__init__(paws=0, hooves=4, name=name, sound=sound, horns=1)


# Створення об'єктів
dog = Paws(name="Dog", sound="Woof")
cat = Paws(name="Cat", sound="Meow")
cow = Hooves(name="Cow", sound="Moo")

# Виклик методу make_sound
print(dog.make_sound())   # Output: Dog says Woof
print(cat.make_sound())   # Output: Cat says Meow
print(cow.make_sound())   # Output: Cow says Moo
