class User:
    ENGINEER = 1
    MANAGER = 2

    def __init__(self, name, age, user_type, phone_number):
        self.name = name
        self.age = age
        self.user_type = user_type
        self.phone_number = phone_number

    def print_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Type:", self.get_user_type_name())
        print("Phone:", self.phone_number)

    def get_user_type_name(self):
        if self.user_type == User.ENGINEER:
            return "Engineer"
        elif self.user_type == User.MANAGER:
            return "Manager"
        else:
            return "Unknown"

def main():
    user = User("John", 25, User.ENGINEER, "050-9379992")
    user.print_details()

if __name__ == "__main__":
    main()