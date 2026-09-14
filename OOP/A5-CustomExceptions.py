# A custom exception is an error type created by us for a particular problem in our application.
# Python already provides errors such as ValueError, TypeError, and FileNotFoundError, 
# but application-specific failures are often easier to understand with custom exceptions.
# For example, a RAG system might have DocumentProcessingError, EmbeddingError, or RetrievalError.
# Custom exceptions are normally created by inheriting from Exception.

# Example 1
class InvalidAgeError(Exception):
    pass

def register_user(age):
    if age < 18:
        raise InvalidAgeError("User must be at least 18 years old")

try:
    register_user(15)
except InvalidAgeError as error:
    print("Registration failed:", error)


# Example 2
try:
    raise Exception("This is the error message", 404, "Invalid Request")
except Exception as e:
    print(e.args)  # Output: ('This is the error message', 404, 'Invalid Request')
    print(e.args[0])  # Output: This is the error message


# Example 3
class InsufficientFundsError(Exception):
    """Raised when an account balance drops below the transaction amount."""
    def __init__(self, balance, amount, message="Transaction declined: Insufficient funds."):
        self.balance = balance
        self.amount = amount
        self.shortfall = amount - balance
        self.message = message
        # Pass the primary error message to the parent Exception class
        super().__init__(f"{message} (Balance: ${balance}, Attempted: ${amount}, Shortfall: ${self.shortfall})")

# Simulating a transaction
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(balance=50, amount=80)
except InsufficientFundsError as error:
    print(f"Alert: {error}")
    print(f"Alert: {error.message}")
    print(f"Alert: {error.amt}")
    print(f"Alert: {error.balance}")
    print(f"Alert: {error.short}")
    print(f"The user needs ${error.shortfall} more to complete this.")