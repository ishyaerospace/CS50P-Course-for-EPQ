class Student:
    def __init__(self, name, house): # self is used to access object
        self.name = name 
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("name: ")
        house = input("house: ")
        return cls(name, house)

def main():
    student = Student.get() # does not create a new object but gets the object value.
    print(student)



if __name__ == "__main__":
    main()
