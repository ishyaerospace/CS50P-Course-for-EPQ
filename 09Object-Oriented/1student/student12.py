class Student:
    def __init__(self, name, house, patronus): 
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name 
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}" 
    
    def charm(self):
        match self.patronus:
            case "stag":
                return "horse"
            case "otter":
                return "otter"
            case "Jack Russell terrier":
                return "dog"
            case _:
                return "sizzling wand"



def main():
    student = get_student()
    print(student)
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus")
    student = Student(name, house, patronus)

    return student

if __name__ == "__main__":
    main()
