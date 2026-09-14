def split_text(text, size=100):
    return [text[i:i + size] for i in range(0, len(text), size)]

def select_top_k(results, k=3):
    return results[:k]