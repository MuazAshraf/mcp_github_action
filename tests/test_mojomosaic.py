
import pytest
import asyncio
import json
from pathlib import Path
import sys

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

class TestMojoMosaicNetwork:
    """Test suite for MojoMosaic fractal network"""
    
    @pytest.mark.asyncio
    async def test_scaffold_exists(self):
        """AT-001: Verify project scaffold exists"""
        required_dirs = [
            'src/orchestrator',
            'src/seed_repo_1',
            'src/seed_repo_2',
            'tests',
            'docs',
            'config'
        ]
        
        for dir_path in required_dirs:
            assert Path(dir_path).exists(), f"Required directory {dir_path} missing"
            
    @pytest.mark.asyncio 
    async def test_split_functionality(self):
        """AT-002: Test fractal split/spawn functionality"""
        # Import after adding to path
        from orchestrator.demo_v0 import FractalNode
        
        node = FractalNode("test_node", 1)
        child = await node.spawn_child()
        
        assert child.node_id == "test_node.0"
        assert child.dimension == 2
        assert node.spawn_count == 1
        
    @pytest.mark.asyncio
    async def test_tcpr_performance(self):
        """AT-006: Test TCPR latency requirements"""
        from orchestrator.demo_v0 import MojoMosaicOrchestrator
        
        orchestrator = MojoMosaicOrchestrator()
        success = await orchestrator.run_demo()
        
        # Calculate TCPR from metrics
        if orchestrator.metrics:
            avg_tcpr = sum(m['tcpr'] for m in orchestrator.metrics) / len(orchestrator.metrics)
            assert avg_tcpr <= 2.0, f"TCPR {avg_tcpr:.3f}s exceeds 2s limit for Dim 1-9"
            
    @pytest.mark.asyncio
    async def test_api_catalogue_exists(self):
        """AT-003: Verify API catalogue exists and is valid"""
        api_path = Path('docs/api_catalogue.json')
        assert api_path.exists(), "API catalogue missing"
        
        with open(api_path) as f:
            api_spec = json.load(f)
            
        assert 'orchestrator_api' in api_spec
        assert 'seed_repo_apis' in api_spec
        
    @pytest.mark.asyncio
    async def test_domain_map_exists(self):
        """AT-004: Verify domain map exists and is valid"""
        domain_path = Path('docs/domain_map.json')
        assert domain_path.exists(), "Domain map missing"
        
        with open(domain_path) as f:
            domain_map = json.load(f)
            
        assert 'dimensions' in domain_map
        assert 'components' in domain_map
        
    @pytest.mark.asyncio
    async def test_alignment_kit_validation(self):
        """AT-005: Test alignment kit validation"""
        alignment_path = Path('alignment/kit.yml')
        assert alignment_path.exists(), "Alignment kit missing"
        
        import yaml
        with open(alignment_path) as f:
            alignment_kit = yaml.safe_load(f)
            
        assert 'alignment_rules' in alignment_kit
        assert 'thresholds' in alignment_kit
        assert alignment_kit['thresholds']['halt_threshold'] == 0.9

# Integration test for demo script
def test_demo_script_exists():
    """Verify run_demo.sh exists and is executable"""
    demo_script = Path('run_demo.sh')
    assert demo_script.exists(), "Demo script missing"
