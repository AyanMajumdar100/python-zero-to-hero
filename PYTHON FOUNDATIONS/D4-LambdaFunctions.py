# A lambda function is a small anonymous function that is written in a single expression. 
# It is useful when you need a simple function temporarily, 
# especially when passing a function to another function such as map(), filter(), or sorted().

# lambda AUTOMATICALLY returns the expression's result. (NO MANUAL RETURN)

# SYNTAX
# lambda parameters: expression
square = lambda x: x * x

print(square(5))
print(square(10))
print(square(12))

# 2. Lambda with Multiple Arguments
add = lambda a, b: a + b
print(add(10, 20))

# 3. Lambda Returning Boolean
is_even = lambda number: number % 2 == 0
print(is_even(10))

# 4. Lambda with a Conditional Expression
maximum = lambda a, b: a if a > b else b
print(maximum(10, 20))
print(maximum(50, 30))

# LAMBDA WITH MAP() : map() applies a function to every element of an iterable.
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

# LAMBDA WITH FILTER() : filter() keeps elements for which the supplied function returns True.
numbers = [12, 75, 34, 90, 41, 63, 18]
large_numbers = list(filter(lambda x: x > 50, numbers))
print(large_numbers)

# LAMBDA WITH SORTED() : 
students = [
    ("Ayan", 85),
    ("Sayan", 92),
    ("Gokul", 78),
    ("Vishnu", 88)
]
print(students[1])
students_sorted = sorted(students, key=lambda student: student[1])
print(students_sorted)

 
# COMPLETE EXAMPLE 1
employees = [
    {"name": "Ayan", "salary": 70000},
    {"name": "Sayan", "salary": 85000},
    {"name": "Gokul", "salary": 60000},
    {"name": "Vishnu", "salary": 95000}
]

employees_by_salary = sorted(
    employees,
    key=lambda employee: employee["salary"],
    reverse=True
)

for employee in employees_by_salary:
    print(employee)

# COMPLETE EXAMPLE 2
transactions = [
    {"user": "Ayan", "amount": 1500, "status": "success"},
    {"user": "Sayan", "amount": 500, "status": "failed"},
    {"user": "Gokul", "amount": 2500, "status": "success"},
    {"user": "Vishnu", "amount": 800, "status": "success"}
]
successful = filter(lambda transaction: transaction["status"] == "success", transactions)
amounts = map(lambda transaction: transaction["amount"], successful)

total = sum(amounts)
print(total)