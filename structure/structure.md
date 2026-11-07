rag-from-scratch/
│
├── data/
│   ├── documents/
│   │   └── sample.txt
│   └── processed/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   │
│   ├── ingestion/
│   │   ├── __init__.py
│   │   └── loader.py
│   │
│   ├── processing/
│   │   ├── __init__.py
│   │   └── chunker.py
│   │
│   ├── embeddings/
│   │   ├── __init__.py
│   │   └── embedder.py
│   │
│   ├── vector_store/
│   │   ├── __init__.py
│   │   └── store.py
│   │
│   ├── retrieval/
│   │   ├── __init__.py
│   │   └── retriever.py
│   │
│   └── generation/
│       ├── __init__.py
│       └── generator.py
│
├── storage/
│   ├── embeddings.npy
│   └── chunks.json
│
├── main.py
├── requirements.txt
├── .env
└── .gitignore