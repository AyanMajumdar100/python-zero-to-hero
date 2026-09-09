# @classmethod : A class method takes the class itself as its first argument (conventionally named cls) rather than the instance (self). 
# It can access and modify the class state, which applies across all instances of that class.
class User:
    # This is a CLASS VARIABLE. It is shared by all users.
    user_count = 0 
    def __init__(self, username):
        self.username = username  # Instance variable (unique to each user)

    @classmethod
    def register_new_user(cls, username):
        # cls refers to the User class itself
        cls.user_count += 1  # Modifying the CLASS STATE
        return cls(username)
    
user1 = User.register_new_user("Alice")
user2 = User.register_new_user("Bob")

print(user1.user_count)  # Output: 2
print(user2.user_count)  # Output: 2
# Both Alice and Bob see the exact same '2' because they share the class state!


# WITHOUT @CLASSMETHOD
class User:
    user_count = 0 

    def __init__(self, username):
        self.username = username 

    def register_new_user(self):
        self.user_count += 1
        return self.user_count

user1 = User("Alice")
user2 = User("Bob")
user1.register_new_user()
user2.register_new_user()
print(user1.user_count)  # Output: 1
print(user2.user_count)  # Output: 1


# @staticmethod : A static method does not take a first implicit argument (neither self nor cls). It behaves exactly like a normal function but lives inside the class's namespace for organizational purposes. 
# It cannot access or modify the class or instance state.
# BEST FOR : Writing utility or helper functions that perform a task in isolation but belong logically to the class.
from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_birth_year(cls, name, year):
        current_year = date.today().year
        calculated_age = current_year - year
        return cls(name, calculated_age)

    # Static Method: A simple utility function that doesn't need class/instance data
    @staticmethod
    def is_adult(age):
        return age >= 18

person_one = Person.from_birth_year("Alice", 1996)
print(person_one.age) 

# 2. Using the static method independently
print(Person.is_adult(20))  # Output: True
