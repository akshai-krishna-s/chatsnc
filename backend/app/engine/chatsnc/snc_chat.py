import chromadb
from llama_index.indices import VectorStoreIndex
from llama_index.vector_stores import ChromaVectorStore
from llama_index.storage.storage_context import StorageContext
from llama_index import ServiceContext, set_global_service_context
from llama_index.llms import Cohere
from llama_index.embeddings import OpenAIEmbedding

from llama_index.llms import Ollama

from ...config import settings
import os

# cohere_api = "GeoiOsqlGvTtzriJfqHg1310n9F9gDnXcq7k5ge5"

os.environ["OPENAI_API_KEY"] = settings.openai_api_key
# llm = Ollama(model="mistral:instruct", request_timeout=30.0)

# llm = Cohere(api_key=cohere_api)


# service_context = ServiceContext.from_defaults(
#     llm=llm, embed_model="local:BAAI/bge-large-en"
# )

# set_global_service_context(service_context)
# embed_model = OpenAIEmbedding(model="text-embedding-3-small")

# service_context = ServiceContext.from_defaults(embed_model=embed_model)

# set_global_service_context(service_context)

db = chromadb.PersistentClient(path="./app/engine/chatsnc/chroma_db")

# get collection
chroma_collection = db.get_collection("college_laws")


# assign chroma as the vector_store to the context
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)


# load your index from stored vectors
index = VectorStoreIndex.from_vector_store(
    vector_store,
    storage_context=storage_context,
)


def chat(query, chat_history):
    global index
    chat_engine = index.as_chat_engine(streaming=True)

    return chat_engine.stream_chat(query, chat_history=chat_history)
