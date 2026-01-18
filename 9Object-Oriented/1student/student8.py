class Student:
    def __init__(self, name, house): 
        if not name:
            raise ValueError("Missing name") # if name wasnt inputed by the user then raise this error
        self.name = name 
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    try:
        student = Student(name, house)
    except ValueError:
        ...
    return student

if __name__ == "__main__":
    main()
