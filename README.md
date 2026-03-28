# Langchain-and-Ollama

A hands-on LangChain and Ollama learning repository which demonstrates practical applications of modern conversational AI, prompt engineering, document loading, retrieval-augmented generation (RAG), tool calling, and agent orchestration.

## Why this repo matters

- Real-world LangChain workflows using `langchain`, `langchain-core`, `langchain-ollama`, and `langchain-community`
- Full pipeline coverage: prompt templates, chains, output parsing, memory, document loaders, vector retrieval, RAG, agents, and tool calling
- Practical demos in notebooks and production-ready Python scripts
- Integration with Ollama for local LLM hosting and Streamlit for a chat UI
- Search/QA tooling with external data sources and a DuckDuckGo agent implementation

## Key components

### Python code examples
- `07. Build Your Own Chatbot/chat_stream.py`
  - Streamlit chatbot using `langchain_ollama.ChatOllama`
  - Message history persistence via `SQLChatMessageHistory`
  - Streamed responses and a reusable chat prompt chain

- `12. Agents/tools.py`
  - LangChain tool wrapper for web search
  - Uses `ddgs` to gather search results and return formatted output
  - Demonstrates tool integration for agent workflows

- `08. Document Loaders/scripts/llm.py`
  - Custom QA chain using Ollama and LangChain prompt templates
  - Context-driven answer generation with a strict "I don't know" fallback

### Notebook curriculum
- `00 Project Setup/setup.md` — environment setup and requirements
- `01. Ollama Setup/ollama commands.md` — Ollama CLI and API guide
- `02. Langchain Getting Started/Langchain Getting Started.ipynb`
- `03. Prompt Templates/Prompt Templates.ipynb`
- `04. Chains/Chains.ipynb`
- `05. Output Parsing/Output Parsing.ipynb`
- `06. Chat Message Memory/Chat Message Memory.ipynb`
- `07. Build Your Own Chatbot/chat_stream.py` (app example)
- `08. Document Loaders/` — PDF, webpage, Office, Markdown, and Docling loaders
- `09. Vector Stores and Retrievals/Vector Stores and Retrievals.ipynb`
- `10. RAG - Chat with Your Own Documents/RAG - Chat with Your Own Documents.ipynb`
- `11. Tool Calling/Tool Calling.ipynb`
- `12. Agents/Agents.ipynb`
- `13. Agentic RAG/Agentic RAG.ipynb`
- `14. Text to MySQL Agent/Text to MySQL Agent.ipynb`

## Project highlights

- Document ingestion and loader demos for PDF, web, office files, markdown, and custom document formats
- Vector store exploration with FAISS and retrieval-based QA
- RAG workflows for document-based chatbot experiences
- Agent tooling for external search and automation
- Streamlit chat interface for live interaction and session history

## Setup and usage

1. Create and activate a Python environment

```bash
conda create -n ml python=3.12 -y
conda activate ml
pip install -r requirements.txt
```

2. Start Ollama locally

```bash
ollama serve
```

3. Run the Streamlit chatbot example

```bash
streamlit run "07. Build Your Own Chatbot/chat_stream.py"
```

4. Explore notebooks in VS Code or Jupyter for each topic area

## Technical stack

- Python 3.12
- LangChain ecosystem (`langchain`, `langchain-core`, `langchain-ollama`, `langchain-community`)
- Ollama local LLM hosting
- Streamlit UI
- FAISS vector store
- Document parsing with `PyMuPDF`, `PyPDF2`, `python-pptx`, `openpyxl`, `docx2txt`, and `unstructured`
- Web search integration via `ddgs`
- SQL-backed chat history

## Note

This repository is designed to showcase learning and applied experience with conversational AI systems, from model interaction and prompt engineering to retrieval workflows and agent-based tooling. It is a strong demonstration of both conceptual understanding and implementation ability in modern AI application development.
