def main():
    student = get_student()    
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)      # tuple -> collection of values which is immutable (cannot change the value)

if __name__ == "__main__":
    main()