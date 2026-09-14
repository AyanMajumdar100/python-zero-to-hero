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



