class User:
    def __init__(self, first_name, last_name, login):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
    
    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Name:{self.first_name} logged in successful")

elvis = User("Elvis", "Kimani", "login")
elvis.describe_user()

class Student(User):
    def __init__(self, first_name, last_name, login, age):
        super().__init__(first_name, last_name, login)
        self.age = age

    def describe_student(self):
        self.describe_user()
        print(f"Age: {self.age}")

Student = Student("Elvis", "Kimani", "elvis_login", 19)
Student.describe_student()
