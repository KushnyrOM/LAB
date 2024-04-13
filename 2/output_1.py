class UserProfile:
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def calculate_total_score(self, score1, score2, score3, score4, score5):
        total_score = score1 + score2 + score3 + score4 + score5
        return total_score

    def is_adult(self):
        return self.age >= 18

    def print_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Height:", self.height)
        print("Weight:", self.weight)

def main():
    user_profile = UserProfile("John", 25, "Male", 175, 70)
    total_score = user_profile.calculate_total_score(85, 90, 75, 88, 92)
    is_adult = user_profile.is_adult()
    user_profile.print_details()
    print("Total Score:", total_score)
    print("Adult:", is_adult)

if __name__ == "__main__":
    main()