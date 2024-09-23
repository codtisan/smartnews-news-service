from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
import toml

class Qdrant:

    def __init__(self) -> None:
        with open('config.toml') as file:
            config = toml.load(file)
        self.client = QdrantClient(url=config['vectorstore']['url'])

    async def create_collection(self, collection_name: str, vector_size: int, distance_method: str = 'Cosine'):
        response = self.client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=vector_size, distance=distance_method)
        )
        return
    
    async def insert(self, collection_name: str, vector: list[float], payload): 
        pass

    async def batch_insert(self, collection_name: str, vectors: list[list[float]], payloads): 
        pass

    async def list_all(self, collection_name: str):
        pass