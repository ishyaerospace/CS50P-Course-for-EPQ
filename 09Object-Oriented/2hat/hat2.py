import random
class Hat: # this way is to only have 1 hat rather than multiple objects of hats

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in ",random.choice(cls.houses))


Hat.sort("Harry")