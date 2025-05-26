
import numpy as np
from typing import List, Dict, Any

class VectorMemory:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.memory_store = {}
        
    async def store_vector(self, vector_id: str, vector: List[float], metadata: Dict[str, Any]) -> bool:
        """Store vector in memory"""
        self.memory_store[vector_id] = {
            'vector': vector,
            'metadata': metadata,
            'timestamp': time.time()
        }
        return True
        
    async def retrieve_similar(self, query_vector: List[float], top_k: int = 10) -> List[Dict[str, Any]]:
        """Retrieve similar vectors"""
        # Simplified similarity search
        results = []
        for vid, data in self.memory_store.items():
            similarity = np.dot(query_vector, data['vector'])
            results.append({
                'id': vid,
                'similarity': similarity,
                'metadata': data['metadata']
            })
        
        return sorted(results, key=lambda x: x['similarity'], reverse=True)[:top_k]
