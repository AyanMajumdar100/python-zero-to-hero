# Conditional Branching (Nested Logic Design)
# Python uses if, elif, and else. 
# There are no parentheses required around the conditions, 
# and indentation (whitespace) defines the scope.


# The Ternary Operator : For simple assignments, Python has a one-line conditional expression:
# Syntax: [value_if_true] if [condition] else [value_if_false]
age = 13
status = "Adult" if age >= 18 else "Minor"

# EXAMPLE 1
age = 20
category = "Child" if age < 13 else "Teen" if age < 18 else "Adult"
print(category)             # Output: 'Adult'

# EXAMPLE 2
inventory_count = 1
message = f"You have {inventory_count} item{'s' if inventory_count != 1 else ''} in your cart."
print(message)              # Output: 'You have 1 item in your cart.'

# EXAMPLE 3
def start_engine(): return "Vroom!"
def sound_alarm(): return "BEEP BEEP BEEP!"
is_authorized = False
action_result = (start_engine if is_authorized else sound_alarm)()
print(action_result)        # Output: 'BEEP BEEP BEEP!'


# Guard Clauses - Deeply nested if statements are hard to read. 
# Good Python code uses "guard clauses"—checking for failure conditions 
# first and returning/breaking early.
user_exists = 1
password_correct = 1
has_permissions = 0

def execute_action(): print("User authenticated!")

# Bad: Deeply nested
if user_exists:
    if password_correct:
        if has_permissions:
            execute_action()

# Good: Guard clauses (Flatter logic)
def attempt_login():
    if not user_exists: 
        return "Failed: User does not exist"
    if not password_correct: 
        return "Failed: Wrong password"
    if not has_permissions: 
        return "Failed: No permissions"
    execute_action()
attempt_login()
