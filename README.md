# Introduction

This repo is just a simple proof of concept for document retrieval (using FAISS, or hybrid with FAISS + BM25). 

`create_db.ipynb` pulls and parses the Singapore constitution into a vector database. Whereas `read_db.ipynb` tests the retrieval of chunks based on a question. 

More could be done for a complete rag system, e.g. fine-tuning the retrieval, reranking the results, using an LLM to generate a response to the user's question, while also providing the chunk together with the source. 
