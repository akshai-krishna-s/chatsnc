import chromadb
from llama_index import VectorStoreIndex, SimpleDirectoryReader, download_loader
from llama_index.vector_stores import ChromaVectorStore
from llama_index.storage.storage_context import StorageContext
from llama_index import ServiceContext, set_global_service_context
from llama_index.embeddings import OpenAIEmbedding
import os
import getpass

os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")

embed_model = OpenAIEmbedding(model="text-embedding-3-small")

service_context = ServiceContext.from_defaults(embed_model=embed_model)

set_global_service_context(service_context)

# load some documents
UnstructuredReader = download_loader("UnstructuredReader")
dir_reader = SimpleDirectoryReader(
    "./data",
    file_extractor={
        ".pdf": UnstructuredReader(),
        ".html": UnstructuredReader(),
        ".eml": UnstructuredReader(),
    },
)
documents = dir_reader.load_data()

# initialize client, setting path to save data
db = chromadb.PersistentClient(path="./chroma_db")

# create collection
chroma_collection = db.get_or_create_collection("college_laws")

# assign chroma as the vector_store to the context
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# create your index
index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)
