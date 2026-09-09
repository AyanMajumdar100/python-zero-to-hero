# EXAMPLE 1
class Student:
    def introduce(self):
        print("Hello, I am a student.")
student1 = Student()
student1.introduce()

# EXAMPLE 2
class Document:
    def show_info(self):
        print(f"Document: {self.name}")
        print(f"Pages: {self.pages}")
document1 = Document()
document1.name = "employee_handbook.pdf"
document1.pages = 25
document1.author = "Ayan"
document1.show_info()
print(document1.author)

# EXAMPLE 3: WITH CONSTRUCTOR
class Document:
    def __init__(self, document_id, filename, source, page_count=0):
        self.document_id = document_id
        self.filename = filename
        self.source = source
        self.page_count = page_count

    def describe(self):
        return (
            f"{self.filename} | "
            f"ID={self.document_id} | "
            f"Source={self.source} | "
            f"Pages={self.page_count}"
        )
document = Document(
    document_id="doc-001",
    filename="employee_policy.pdf",
    source="HR",
    page_count=42
)
print(document.describe())
print(document)
# UGLY OUTPUT : 
# employee_policy.pdf | ID=doc-001 | Source=HR | Pages=42
# <__main__.Document object at 0x00000238A8524830>


# INSTANCE VARIABLES: Instance attributes are variables that belong to a specific object.
# They are normally created using self.attribute_name inside __init__() or another method.
class RetrievalResult:
    def __init__(self, chunk_id, text, score, page_number):
        self.chunk_id = chunk_id
        self.text = text
        self.score = score
        self.page_number = page_number

    def is_relevant(self, threshold=0.70):
        return self.score >= threshold

result = RetrievalResult(
    chunk_id="chunk-42",
    text="Employees receive 18 days of annual leave.",
    score=0.86,
    page_number=7
)
print(result.chunk_id)
print(result.score)
print(result.is_relevant())


# METHODS IN CLASSES
class Calculator:
    def add(self, a, b):
        return a + b

calculator = Calculator()
result = calculator.add(10, 20)
print(result)
# Attributes are only created on fly when defined using obj.attr_name = ...
print(calculator.a) # AttributeError: 'Calculator' object has no attribute 'a'

# SAMPLE METHODS IN A CLASS
class DocumentChunk:
    def __init__(self, document_id, page_number, text):
        self.document_id = document_id
        self.page_number = page_number
        self.text = text

    def word_count(self):
        return len(self.text.split())

    def preview(self, length=50):
        return self.text[:length] + "..."

    def to_metadata(self):
        return {
            "document_id": self.document_id,
            "page_number": self.page_number
        }

chunk = DocumentChunk(
    "doc-101",
    12,
    "Employees can claim travel expenses according to the company's reimbursement policy."
)
print(chunk.word_count())
print(chunk.preview())
print(chunk.to_metadata())

