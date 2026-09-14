from B1_1_modules import split_text, select_top_k

text = "This is a long document that needs to be divided into smaller pieces."
chunks = split_text(text, size=20)

results = [
    {"id": "1", "score": 0.95},
    {"id": "2", "score": 0.91},
    {"id": "3", "score": 0.85},
    {"id": "4", "score": 0.70},
]

top_results = select_top_k(results, 3)
print(chunks)
print(top_results)

# OUTPUT
# ['This is a long docum', 'ent that needs to be', ' divided into smalle', 'r pieces.']
# [{'id': '1', 'score': 0.95}, {'id': '2', 'score': 0.91}, {'id': '3', 'score': 0.85}]