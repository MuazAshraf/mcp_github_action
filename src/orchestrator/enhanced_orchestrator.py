#!/usr/bin/env python3
"""
Enhanced MojoMosaic Orchestrator with full feature implementation
"""

import asyncio
import json
import logging
import time
import uuid
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict

@dataclass
class NetworkMetrics:
    """Network performance metrics"""
    node_id: str
    dimension: int
    tcpr_seconds: float
    success_rate: float
    request_count: int
    timestamp: str
    parent_id: Optional[str] = None
    child_ids: List[str] = None

class EnhancedFractalNode:
    """Enhanced fractal node with full logging and metrics"""
    
    def __init__(self, node_id: str, dimension: int, parent_id: Optional[str] = None):
        self.node_id = node_id
        self.dimension = dimension
        self.parent_id = parent_id
        self.child_ids = []
        self.spawn_count = 0
        self.request_count = 0
        self.success_count = 0
        self.total_tcpr = 0.0
        self.logger = logging.getLogger(f"FractalNode.{node_id}")
        
    async def spawn_child(self) -> 'EnhancedFractalNode':
        """Spawn child with full tracing"""
        operation_id = str(uuid.uuid4())
        self.logger.info(f"BEGIN spawn_child operation_id={operation_id} parent_id={self.node_id}")
        
        child_id = f"{self.node_id}.{self.spawn_count}"
        child = EnhancedFractalNode(child_id, self.dimension + 1, self.node_id)
        
        self.child_ids.append(child_id)
        self.spawn_count += 1
        
        self.logger.info(f"END spawn_child operation_id={operation_id} child_id={child_id}")
        return child
        
    async def process_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Process request with full logging and metrics"""
        operation_id = str(uuid.uuid4())
        start_time = time.time()
        
        self.logger.info(f"BEGIN process_request operation_id={operation_id} node_id={self.node_id} parent_id={self.parent_id}")
        
        try:
            # Simulate fractal processing based on dimension
            processing_time = 0.05 + (self.dimension * 0.01)
            await asyncio.sleep(processing_time)
            
            tcpr = time.time() - start_time
            self.request_count += 1
            self.success_count += 1
            self.total_tcpr += tcpr
            
            response = {
                'operation_id': operation_id,
                'node_id': self.node_id,
                'dimension': self.dimension,
                'parent_id': self.parent_id,
                'processed_at': datetime.now().isoformat(),
                'tcpr': tcpr,
                'status': 'success',
                'child_count': len(self.child_ids)
            }
            
            self.logger.info(f"END process_request operation_id={operation_id} tcpr={tcpr:.3f}s status=success")
            return response
            
        except Exception as e:
            self.request_count += 1
            tcpr = time.time() - start_time
            
            self.logger.error(f"END process_request operation_id={operation_id} tcpr={tcpr:.3f}s status=error error={str(e)}")
            
            return {
                'operation_id': operation_id,
                'node_id': self.node_id,
                'tcpr': tcpr,
                'status': 'error',
                'error': str(e)
            }
            
    def get_metrics(self) -> NetworkMetrics:
        """Get node performance metrics"""
        avg_tcpr = self.total_tcpr / max(self.request_count, 1)
        success_rate = self.success_count / max(self.request_count, 1)
        
        return NetworkMetrics(
            node_id=self.node_id,
            dimension=self.dimension,
            tcpr_seconds=avg_tcpr,
            success_rate=success_rate,
            request_count=self.request_count,
            timestamp=datetime.now().isoformat(),
            parent_id=self.parent_id,
            child_ids=self.child_ids.copy()
        )

class EnhancedMojoMosaicOrchestrator:
    """Enhanced orchestrator with comprehensive features"""
    
    def __init__(self):
        self.nodes: Dict[str, EnhancedFractalNode] = {}
        self.metrics_history: List[NetworkMetrics] = []
        self.logger = logging.getLogger("MojoMosaicOrchestrator")
        
    async def initialize_network(self, max_dimension: int = 27):
        """Initialize fractal network with enhanced structure"""
        operation_id = str(uuid.uuid4())
        self.logger.info(f"BEGIN initialize_network operation_id={operation_id} max_dimension={max_dimension}")
        
        # Create root node
        root_node = EnhancedFractalNode("root", 0)
        self.nodes["root"] = root_node
        
        # Create fractal tree structure
        for dim in range(1, max_dimension + 1):
            if dim <= 9:
                # Primary dimensions - multiple nodes per dimension
                for i in range(2):
                    node_id = f"dim_{dim}_node_{i}"
                    parent_id = "root" if dim == 1 else f"dim_{dim-1}_node_0"
                    node = EnhancedFractalNode(node_id, dim, parent_id)
                    self.nodes[node_id] = node
            else:
                # Extended dimensions - single node per dimension
                node_id = f"dim_{dim}_node_0"
                parent_id = f"dim_{dim-1}_node_0"
                node = EnhancedFractalNode(node_id, dim, parent_id)
                self.nodes[node_id] = node
                
        self.logger.info(f"END initialize_network operation_id={operation_id} node_count={len(self.nodes)}")
        
    async def run_comprehensive_demo(self) -> Dict[str, Any]:
        """Run comprehensive fractal network demonstration"""
        demo_id = str(uuid.uuid4())
        self.logger.info(f"BEGIN run_comprehensive_demo demo_id={demo_id}")
        
        # Initialize network up to dimension 27
        await self.initialize_network(27)
        
        # Test Dim 1-9 (TCPR <= 2s target)
        dim_1_9_results = await self._test_dimension_range(1, 9, 50)
        
        # Test Dim 10-27 (TCPR <= 10s target)
        dim_10_27_results = await self._test_dimension_range(10, 27, 20)
        
        # Collect comprehensive metrics
        all_metrics = []
        for node in self.nodes.values():
            if node.request_count > 0:
                metrics = node.get_metrics()
                all_metrics.append(metrics)
                self.metrics_history.append(metrics)
                
        demo_results = {
            'demo_id': demo_id,
            'dim_1_9_results': dim_1_9_results,
            'dim_10_27_results': dim_10_27_results,
            'total_nodes': len(self.nodes),
            'total_requests': sum(m.request_count for m in all_metrics),
            'overall_success_rate': sum(m.success_rate * m.request_count for m in all_metrics) / sum(m.request_count for m in all_metrics),
            'timestamp': datetime.now().isoformat()
        }
        
        self.logger.info(f"END run_comprehensive_demo demo_id={demo_id} success={self._evaluate_success(demo_results)}")
        return demo_results
        
    async def _test_dimension_range(self, start_dim: int, end_dim: int, requests_per_node: int) -> Dict[str, Any]:
        """Test specific dimension range"""
        results = []
        
        for dim in range(start_dim, end_dim + 1):
            dim_nodes = [node for node in self.nodes.values() if node.dimension == dim]
            
            for node in dim_nodes:
                for i in range(requests_per_node):
                    request = {
                        'test_id': f"dim_{dim}_req_{i}",
                        'timestamp': time.time()
                    }
                    response = await node.process_request(request)
                    results.append(response)
                    
        # Calculate dimension range metrics
        successful_requests = [r for r in results if r.get('status') == 'success']
        avg_tcpr = sum(r['tcpr'] for r in successful_requests) / len(successful_requests) if successful_requests else 0
        
        return {
            'dimension_range': f"{start_dim}-{end_dim}",
            'total_requests': len(results),
            'successful_requests': len(successful_requests),
            'avg_tcpr': avg_tcpr,
            'max_tcpr': max(r['tcpr'] for r in successful_requests) if successful_requests else 0,
            'success_rate': len(successful_requests) / len(results) if results else 0
        }
        
    def _evaluate_success(self, demo_results: Dict[str, Any]) -> bool:
        """Evaluate if demo meets success criteria"""
        dim_1_9 = demo_results['dim_1_9_results']
        dim_10_27 = demo_results['dim_10_27_results']
        
        # Check TCPR targets
        tcpr_1_9_ok = dim_1_9['avg_tcpr'] <= 2.0
        tcpr_10_27_ok = dim_10_27['avg_tcpr'] <= 10.0
        
        # Check success rates
        success_rate_ok = demo_results['overall_success_rate'] >= 0.95
        
        return tcpr_1_9_ok and tcpr_10_27_ok and success_rate_ok

async def main():
    """Main demo execution"""
    logging.basicConfig(level=logging.INFO)
    
    orchestrator = EnhancedMojoMosaicOrchestrator()
    results = await orchestrator.run_comprehensive_demo()
    
    print("\n" + "="*50)
    print("MojoMosaic Enhanced Demo Results")
    print("="*50)
    print(f"Total Nodes: {results['total_nodes']}")
    print(f"Total Requests: {results['total_requests']}")
    print(f"Overall Success Rate: {results['overall_success_rate']:.2%}")
    print(f"\nDim 1-9 Avg TCPR: {results['dim_1_9_results']['avg_tcpr']:.3f}s (target: <=2.0s)")
    print(f"Dim 10-27 Avg TCPR: {results['dim_10_27_results']['avg_tcpr']:.3f}s (target: <=10.0s)")
    
    # Evaluate success
    dim_1_9_ok = results['dim_1_9_results']['avg_tcpr'] <= 2.0
    dim_10_27_ok = results['dim_10_27_results']['avg_tcpr'] <= 10.0
    
    if dim_1_9_ok and dim_10_27_ok:
        print("\nAll TCPR targets met!")
        return True
    else:
        print("\nTCPR targets not met")
        return False

if __name__ == "__main__":
    success = asyncio.run(main())
    exit(0 if success else 1)
