# class -> blueprint of data objects
# ... can be used as a placeholder to indicate more code will be added later
class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student() # creating object from the class
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()
