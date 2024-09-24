from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, PointStruct
import toml

class Qdrant:

    def __init__(self) -> None:
        with open('config.toml') as file:
            config = toml.load(file)
        self.client = QdrantClient(url=config['vectorstore']['url'])

    async def create_collection(self, collection_name: str, vector_size: int, distance_method: str = 'Cosine'):
        self.client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=vector_size, distance=distance_method)
        )
        return
    
    async def insert(self, collection_name: str, vector: list[float], payload): 
        pass

    async def batch_insert(self, collection_name: str, vectors: list[list[float]], payloads): 
        point_structs = [PointStruct(
            id=index,
            vector=embedding,
            payload=payloads[index]
        ) for index, embedding in enumerate(vectors)]
        self.client.upsert(
            collection_name=collection_name,
            wait=True,
            points=point_structs
        )

    async def list_all(self, collection_name: str):
        pass

    async def check_collection(self, collection_name: str):
        is_exist = self.client.collection_exists(collection_name=collection_name)
        return is_exist