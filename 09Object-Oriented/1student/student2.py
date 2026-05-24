def main():
    name, house = get_student()    
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house      # tuple -> collection of values which is immutable (cannot change the value)

if __name__ == "__main__":
    main()