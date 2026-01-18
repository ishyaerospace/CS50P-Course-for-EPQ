class Student:
    def __init__(self, name, house): 
        if not name:
            raise ValueError("Missing name")

        self.name = name # calls the name setter function
        self.house = house # calls the house setter function 

    def __str__(self):
        return f"{self.name} from {self.house}" 
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
            return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")        
        self._house = house



def main():
    student = get_student()
    student.house = "Number Four, Privet Drive" # this will call the setter function (python can tell this by seeing the "=")
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)

    return student

if __name__ == "__main__":
    main()
