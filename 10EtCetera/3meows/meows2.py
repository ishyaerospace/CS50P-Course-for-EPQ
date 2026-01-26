#OOP version

class Cat:
    MEOWS = 3 # by convention this is a constant, although not inforced

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meows")


cat = Cat()
cat.meow()
