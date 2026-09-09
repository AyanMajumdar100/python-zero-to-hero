# dataclass: A dataclass is a Python feature designed to make classes that primarily store data much easier to write.
# Without dataclasses, we often have to manually create an __init__() method and assign many attributes ourselves.

from dataclasses import dataclass, field
@dataclass
class Document:
    filename: str
    pages: int = 0
    tags: list[str] = field(default_factory=list)

doc1 = Document("policy.pdf")
doc2 = Document("manual.pdf", 50, ["hr", "internal"])
doc1.tags.append("company")

print(doc1) # Document(filename='policy.pdf', pages=0, tags=['company'])
print(doc2) # Document(filename='manual.pdf', pages=50, tags=['hr', 'internal'])

# NORMAL CLASSES WHEN PRINTED GIVE UGLY OUTPUTS
# UGLY OUTPUT : normal class object
# employee_policy.pdf | ID=doc-001 | Source=HR | Pages=42
# <__main__.Document object at 0x00000238A8524830>



# DATACLASS WITH RAG CHUNK EXAMPLE
from dataclasses import dataclass, field, asdict, replace

# The @dataclass decorator automatically generates __init__, __repr__, and __eq__ methods
@dataclass
class Chunk:
    # Define fields and their expected data types (type hinting)
    chunk_id: str
    document_id: str
    page_number: int
    text: str
    
    # field(default_factory=dict) prevents a mutable default argument error
    # It ensures every new object gets its own fresh, empty dictionary
    metadata: dict[str, str] = field(default_factory=dict)

    # __post_init__ runs automatically right after the generated __init__ finishes
    def __post_init__(self):
        # Clean up input data by removing leading/trailing spaces
        self.text = self.text.strip()

        # Add validation to catch bad data immediately upon creation
        if not self.chunk_id:
            raise ValueError("chunk_id cannot be empty")

        if self.page_number < 1:
            raise ValueError("page_number must be >= 1")

    # A regular instance method to perform actions using the object's data
    def word_count(self):
        return len(self.text.split())

# Initialize a new Chunk object (arguments are automatically mapped to fields)
chunk = Chunk(
    chunk_id="chunk-001",
    document_id="doc-001",
    page_number=4,
    text="  Employees receive 18 days of annual leave.  ",
    metadata={"department": "HR"}
)

# Dataclasses print out beautifully formatted readable strings by default
print(chunk)  # Chunk(chunk_id='chunk-001', document_id='doc-001', page_number=4, text='Employees receive 18 days of annual leave.', metadata={'department': 'HR'})

print(chunk.word_count()) # 7

# Convert the dataclass object into a standard Python dictionary (great for JSON/API payloads)
chunk_dict = asdict(chunk)
print(chunk_dict)    # {'chunk_id': 'chunk-001', 'document_id': 'doc-001', 'page_number': 4, 'text': 'Employees receive 18 days of annual leave.', 'metadata': {'department': 'HR'}}

# Create a brand new, independent copy of the object while changing specific values
updated_chunk = replace(chunk, page_number=10)
print(updated_chunk)    # Chunk(chunk_id='chunk-001', document_id='doc-001', page_number=5, text='Employees receive 18 days of annual leave.', metadata={'department': 'HR'})

updated_chunk = replace(chunk, page_number=-5)  # OUTPUT: ValueError: page_number must be >= 1
print(updated_chunk)



chunk2 = Chunk(
    chunk_id="chunk-002",
    document_id="doc-002",
    page_number=4,
    text="  Employees receive 18K Rs of annual bonus.  ",
    metadata={"department": "DEV HR"}
)

chunk2.page_number = -10    # NO ERROR WILL BE RAISED BUT!
# 'page_number': -10 -> this will bypass the __post_int__() validation we have created
print(asdict(chunk2))