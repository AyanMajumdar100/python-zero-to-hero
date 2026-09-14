# JSON stands for JavaScript Object Notation and is one of the most common formats 
# for exchanging structured data between applications.
# It represents objects, arrays, strings, numbers, booleans, and null-like values in a text format.

# Python dictionaries and lists map naturally to JSON objects and arrays.

# 1. json.dumps(data) : Dict to JSON

# ACCEPTED PARAMETERS (obj, fp -> are mandatory)
# json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, 
#           allow_nan=True, cls=None, indent=None, separators=None, 
#           default=None, sort_keys=False, **kw)

import json
data = {
    "name": "Ayan",
    "role": "AI Engineer",
    "skills": ["Python", "RAG", "Angular"]
}
json_text = json.dumps(data)    
print(json_text)    # {"name": "Ayan", "role": "AI Engineer", "skills": ["Python", "RAG", "Angular"]}
# or write to a file
with open("output.json","w",encoding="utf-8") as file:
    json.dump(data,file,indent=5)

# 2. json.load(file) : JSON to Dict

# ACCEPTED PARAMTERS
# json.load(fp, *, cls=None, object_hook=None, parse_float=None, 
#           parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)

import json
with open("sample1.json", "r", encoding="utf-8") as file:
    config = json.load(file)
print(config)           # {'top_k': 5, 'chunk_size': 500, 'model': 'example-model'}
print(config["top_k"])  # 5


# Default callback in dump function
import json
from datetime import datetime
# A custom function to convert datetime objects into ISO strings
def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")
data = {
    "event": "Launch",
    "timestamp": datetime(2026, 9, 14, 10, 0, 0)
}
# Serialize to file using the default hook
with open("event.json", "w") as f:
    json.dump(data, f, default=serialize_datetime, indent=4)

# OBJECT_HOOK FUNCTION IN DESERIALIZATION
import json
from datetime import datetime
# A custom function to turn specific string formats back into datetimes
def deserialize_datetime(dct):
    if "timestamp" in dct:
        dct["timestamp"] = datetime.fromisoformat(dct["timestamp"])
    return dct
# Load the file back into Python
with open("event.json", "r") as f:
    loaded_data = json.load(f, object_hook=deserialize_datetime)

print(loaded_data["timestamp"])  # Output: 2026-09-14 10:00:00
print(type(loaded_data["timestamp"]))  # Output: <class 'datetime.datetime'>

# LIST JSON HANDLING
import json
fruits = ["apple", "banana", "cherry"]

# 1. Serialize (List -> JSON String)
json_string = json.dumps(fruits)
print(json_string)  # Output: ["apple", "banana", "cherry"]

# 2. Deserialize (JSON String -> List)
decoded_list = json.loads(json_string)
print(decoded_list[0])  # Output: apple

# STRING JSON HANDLING
import json
message = "Hello, World! Here is a quote: \"Python\"."

# 1. Serialize (String -> JSON Formatted String)
json_string = json.dumps(message)
print(json_string)  # Output: "Hello, World! Here is a quote: \"Python\"."

# 2. Deserialize (JSON Formatted String -> String)
decoded_string = json.loads(json_string)
print(decoded_string)  # Output: Hello, World! Here is a quote: "Python".

# RAG JSON + DATACLASS SERIALIZATION/DESERIALIZATION EXAMPLE
import json
from dataclasses import dataclass, asdict
@dataclass
class EvaluationResult:
    question_id: str
    answer_quality: float
    groundedness: float

result = EvaluationResult(
    question_id="q-001",
    answer_quality=0.91,
    groundedness=0.95
)
# Dataclass -> dictionary
data = asdict(result)

# Dictionary -> JSON
json_text = json.dumps(data, indent=4)
print(json_text)

# JSON -> Python dictionary
restored_data = json.loads(json_text)
print(restored_data["groundedness"])

# json.dumps/loads -> when we are directly storing it in str
# json.dump/load -> when we are storing it to a file object