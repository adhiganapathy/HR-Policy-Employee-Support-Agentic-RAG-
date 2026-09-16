# HR-Policy-Employee-Support-Agentic-RAG

This repository contains the implementation of a **production-grade Agentic RAG (Retrieval-Augmented Generation)** system designed for enterprise HR support. Unlike standard RAG implementations, this system features a sophisticated, multi-step decision-making workflow using **LangGraph**.

---

## 🚀 Project Overview
The system acts as an intelligent assistant capable of answering complex HR queries by intelligently routing between:
- Private company documents  
- Real-time web searches  
- Direct LLM responses  

---

## 🛠️ Tech Stack
- **Orchestration:** LangGraph for complex, multi-step agentic workflows and conditional routing  
- **Vector Database:** Pinecone for secure, private knowledge-base vector indexing  
- **Search Capability:** Tavily for intelligent web fallback when internal data is insufficient  
- **Backend:** FastAPI for building high-performance, scalable API services  
- **Observability:** LangSmith for deep tracing and monitoring the agent's decision-making process  
- **Deployment:** Docker containerization hosted on DigitalOcean Cloud  

---

## 💡 Key Features
- **Evidence Grading:** LLM-based graders ensure that retrieved context is relevant and grounded before generating a response  
- **Query Rewriting:** Robust retry mechanisms refine search queries for better accuracy  
- **Auditability:** SQLite-based database integration for tracking chat history, feedback, and system performance  
- **Modular Architecture:** Clean, production-ready codebase separated into logical modules for scalability  

---

## 🏗️ System Architecture
📌 *Architecture Diagram goes here*

---

## 🚀 Deployment
This project is fully dockerized and ready for deployment on cloud platforms like **DigitalOcean**.  
It includes comprehensive logging and observability via **LangSmith** to ensure reliability in an enterprise environment.  

---

## 📜 License
Distributed under the **Apache License 2.0**.  
See the [LICENSE](./LICENSE) file for more information.  
