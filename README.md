# 🐍 Python Zero to Hero: AI Engineering Roadmap

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

A comprehensive, end-to-end repository tracking my journey from core Python fundamentals to AI Engineering, Deep Learning, and Production System Design. Designed for practical implementation, algorithmic problem-solving, and building real-world AI applications.

---

## 🚀 Key Highlights

- **Structured Learning:** Covers an extensive 9-phase roadmap transitioning from Python basics to production-ready AI systems.
- **Pattern-Based DSA:** Emphasizes pattern recognition (Two Pointers, Monotonic Stack, Dynamic Programming) over solution memorization.
- **Production Focus:** Integrates core Python logic directly with modern API frameworks (FastAPI), vector databases, and containerized deployments.
- **Hands-On Code:** Clean, modular, and documented Python scripts for algorithms, data pipelines, machine learning models, and system design setups.

---

## 🗺️ Roadmap & Topics Covered

### 📍 Phase 1: Python Foundations & Basic DSA Patterns (Weeks 1–3)
- **Core Language:** Execution model, mutability vs immutability, strings & Unicode, truthy/falsy evaluation.
- **Data Structures:** Internal behavior of Lists, Tuples, Sets, and Dictionaries (hash table collisions).
- **Control & Functions:** LEGB scope, first-class functions, recursion stack behavior, file I/O (JSON/CSV).
- **DSA Patterns:** Two Pointers, HashMap / Frequency Counter, Sliding Window, Prefix Sum.

### 📍 Phase 2: Intermediate Python & Core DSA (Weeks 4–7)
- **Advanced Python:** Comprehensions, Iterators vs Generators, Decorators, Context Managers, Custom Exceptions.
- **Object-Oriented Design:** OOP principles, MRO (Method Resolution Order), encapsulation, composition vs inheritance.
- **DSA Patterns:** Binary Search (Answer Space), Fast & Slow Pointers, Monotonic Stack, Backtracking (subsets, permutations, pruning).

### 📍 Phase 3: Advanced Data Structures & Algorithms (Weeks 8–12)
- **Data Structures:** Linked Lists, Stacks, Queues, Heaps/Priority Queues, Trees, and Graphs.
- **Tree & Graph Patterns:** DFS/BFS, Topological Sort, Cycle Detection, Disjoint Set (Union-Find).
- **Dynamic Programming & Optimization:** 1D/2D DP, Knapsack, Subsequence problems, Greedy Algorithms.

### 📍 Phase 4: Python for Data & Math Foundations (Weeks 13–16)
- **Data Tools:** NumPy (broadcasting, vectorization), Pandas (DataFrames, GroupBy, pipelines), Data Visualization.
- **Math Foundations:** Linear Algebra (vectors, matrices, dot products), Probability & Statistics, Gradient Descent.

### 📍 Phase 5: Machine Learning (Weeks 17–22)
- **Core ML:** Supervised/Unsupervised learning, Bias-Variance tradeoff, Cross-Validation.
- **Algorithms:** Linear & Logistic Regression, Decision Trees, Random Forests, Gradient Boosting, SVM, KNN.
- **Evaluation & Feature Engineering:** Precision/Recall, ROC-AUC, Scaling, One-Hot Encoding, Feature Selection.

### 📍 Phase 6: Natural Language Processing (NLP) (Weeks 23–26)
- **Text Processing:** Tokenization, Lemmatization, TF-IDF, N-grams, Word Embeddings (Word2Vec, GloVe).
- **Sequence Models:** Naive Bayes for text, RNNs, LSTM/GRU architectures.

### 📍 Phase 7: Deep Learning & Transformers (Weeks 27–32)
- **Neural Networks:** Perceptrons, Activation Functions, Backpropagation.
- **Transformers & LLMs:** Self-Attention mechanism, Encoder-Decoder models, BERT, GPT, Fine-tuning vs Prompting.
- **LLM Engineering:** RAG (Retrieval-Augmented Generation), Vector Databases, Embeddings.

### 📍 Phase 8: FastAPI & Backend Engineering (Weeks 33–36)
- **FastAPI Core:** Routing, Pydantic validation, Dependency Injection, Async/Await concurrency.
- **Model Deployment:** Serving ML/NLP models via REST APIs, Docker containerization, CI/CD pipelines, Cloud deployment.

### 📍 Phase 9: AI System Design (Weeks 37–40)
- **Architecture:** Data & Model pipelines, Batch vs Real-time Inference, Caching strategies, Load Balancing.
- **MLOps:** Model drift detection, automated retraining pipelines, and monitoring in production.

---

## 💻 Tech Stack & Requirements

- **Language:** Python `3.10+` (Recommended)
- **Core Libraries:** NumPy, Pandas, Scikit-Learn, PyTorch / TensorFlow, NLTK/SpaCy
- **Backend & MLOps:** FastAPI, Uvicorn, Docker, Vector DBs (Chroma/Pinecone)

---

## 🛠️ Setup & Run Instructions

**1. Clone the repository**
```bash
git clone [https://github.com/AyanMajumdar100/python-zero-to-hero.git](https://github.com/AyanMajumdar100/python-zero-to-hero.git)
cd python-zero-to-hero

```

**2. Set up a Virtual Environment (Recommended)**

```bash
# On Linux/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate

```

**3. Install Dependencies**

```bash
pip install -r requirements.txt

```

**4. Run any module or script**

```bash
# Example: Running a script from Phase 1
python phase_1_foundations/01_two_pointers.py

```

---

*Built with ❤️ for mastering Python, DSA, and modern AI Systems.*

```