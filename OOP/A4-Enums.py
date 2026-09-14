# An Enum represents a fixed set of named choices.
# Instead of passing arbitrary strings such as "pending", "completed", and "failed" 
# throughout an application, we can define those valid states once.

# Example 1
from enum import Enum

class Status(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
status = Status.PENDING

print(status)
print(status.value)

# Example 2
from enum import Enum, auto

class ProcessingStage(Enum):
    EXTRACTING = auto()
    CHUNKING = auto()
    EMBEDDING = auto()
    INDEXING = auto()

current_stage = ProcessingStage.EMBEDDING

print(current_stage.name)
print(current_stage.value)

for stage in ProcessingStage:
    print(stage.name, stage.value)

# Example 3
from enum import Enum

class SearchStrategy(Enum):
    VECTOR = "vector"
    KEYWORD = "keyword"
    HYBRID = "hybrid"

class EvaluationStatus(Enum):
    PASSED = "passed"
    FAILED = "failed"

def describe_strategy(strategy: SearchStrategy):
    if strategy == SearchStrategy.VECTOR:
        return "Semantic vector search"
    elif strategy == SearchStrategy.KEYWORD:
        return "Keyword search"
    else:
        return "Combination of vector and keyword search"

strategy = SearchStrategy.HYBRID
status = EvaluationStatus.PASSED

print(describe_strategy(strategy))
print("Evaluation:", status.value)