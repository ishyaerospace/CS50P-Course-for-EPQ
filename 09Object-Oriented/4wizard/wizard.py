class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("missing Name")
        self.name = name
    ...

class Student(Wizard): # inherits from Wizard class
    def __init__(self, name, house):
        super().__init__(name) # calls the __init__ method of the wizard class
        self.house = house
    
    ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name) # calls the __init__ method of the wizard class
        self.subject = subject

    ...


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "defense Against The Dark Arts")