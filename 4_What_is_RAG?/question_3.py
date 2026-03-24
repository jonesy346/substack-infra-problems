"""
Question:
(Harder) Build a simple RAG pipeline using LangChain. Your script should:
- Load data from a provided URL
- Split it into chunks (500 chars, 50 overlap)
- Generate embeddings using all-MiniLM-L6-v2
- Store them in a Chroma vector database
- Retrieve the top-3 most relevant chunks for a query
- Generate a response using the retrieved context
- Use the query: "What is this document about?"

Note: This requires an OpenAI API key set as the OPENAI_API_KEY environment variable.
The embedding step uses a free local model; only the generation step calls OpenAI.
"""

import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# 1. Load data from a URL
loader = WebBaseLoader("https://en.wikipedia.org/wiki/Retrieval-augmented_generation")
docs = loader.load()

# 2. Split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(docs)

# 3. Generate embeddings and store in Chroma
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(chunks, embeddings)

# 4. Set up retriever (top-3 chunks)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 5. Define prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer the user's question based on the following context:\n\n{context}"),
    ("human", "{input}"),
])

# 6. Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 7. Build and run the RAG chain
document_chain = create_stuff_documents_chain(llm, prompt)
retrieval_chain = create_retrieval_chain(retriever, document_chain)

response = retrieval_chain.invoke({"input": "What is this document about?"})
print(response["answer"])
