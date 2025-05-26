#!/usr/bin/env python3
"""
MojoMosaic Demo v0 - Fractal Network Demonstration
"""

import asyncio
import json
import time
from datetime import datetime

class FractalNode:
    def __init__(self, node_id: str, dimension: int):
        self.node_id = node_id
        self.dimension = dimension
        self.spawn_count = 0
        
    async def spawn_child(self) -> 'FractalNode':
        """Spawn a child fractal node"""
        child_id = f"{self.node_id}.{self.spawn_count}"
        child = FractalNode(child_id, self.dimension + 1)
        self.spawn_count += 1
        return child
        
    async def process_request(self, request: dict) -> dict:
        """Process a fractal request"""
        start_time = time.time()
        
        # Simulate fractal processing
        await asyncio.sleep(0.1)  # Simulated work
        
        response = {
            'node_id': self.node_id,
            'dimension': self.dimension,
            'processed_at': datetime.now().isoformat(),
            'tcpr': time.time() - start_time,
            'status': 'success'
        }
        
        return response

class MojoMosaicOrchestrator:
    def __init__(self):
        self.nodes = {}
        self.metrics = []
        
    async def initialize_network(self, max_dimension: int = 9):
        """Initialize fractal network up to max_dimension"""
        print(f"Initializing MojoMosaic network up to dimension {max_dimension}")
        
        for dim in range(1, max_dimension + 1):
            node_id = f"node_dim_{dim}"
            self.nodes[node_id] = FractalNode(node_id, dim)
            
        print(f"Network initialized with {len(self.nodes)} nodes")
        
    async def run_demo(self):
        """Run fractal network demonstration"""
        print("Starting MojoMosaic Demo v0...")
        
        await self.initialize_network(9)
        
        # Process sample requests
        for i in range(10):
            node = list(self.nodes.values())[i % len(self.nodes)]
            request = {'demo_request': i, 'timestamp': time.time()}
            
            response = await node.process_request(request)
            self.metrics.append(response)
            
            print(f"Processed request {i} on {node.node_id}: TCPR={response['tcpr']:.3f}s")
            
        # Calculate average TCPR
        avg_tcpr = sum(m['tcpr'] for m in self.metrics) / len(self.metrics)
        print(f"Average TCPR: {avg_tcpr:.3f}s")
        
        if avg_tcpr <= 2.0:
            print("TCPR target met for Dim 1-9!")
        else:
            print("TCPR target not met")
            
        return avg_tcpr <= 2.0

async def main():
    orchestrator = MojoMosaicOrchestrator()
    success = await orchestrator.run_demo()
    return success

if __name__ == "__main__":
    result = asyncio.run(main())
    exit(0 if result else 1)
