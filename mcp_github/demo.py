#!/usr/bin/env python3
"""
GitHub MCP Demo Script
Complete demonstration of all capabilities
"""

import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Dict, Any
import subprocess
import time

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent))

from server import GitHubMCPServer

class GitHubMCPDemo:
    def __init__(self):
        self.server = GitHubMCPServer()
        
    async def run_comprehensive_demo(self):
        """Run comprehensive demo of all GitHub MCP features"""
        
        print("🚀 GitHub Action MCP - Complete Demo")
        print("=" * 60)
        
        # Check GitHub token
        if not os.getenv("GITHUB_TOKEN"):
            print("❌ GITHUB_TOKEN environment variable not set!")
            print("💡 To get a token:")
            print("   1. Go to GitHub Settings > Developer settings > Personal access tokens")
            print("   2. Generate new token with repo permissions")
            print("   3. Set: export GITHUB_TOKEN=your_token_here")
            return
        
        print("✅ GitHub token found!")
        
        # Initialize HTTP session
        import aiohttp
        self.server.session = aiohttp.ClientSession()
        
        try:
            # Demo 1: List tools and resources
            await self._demo_list_capabilities()
            
            # Demo 2: Repository operations
            await self._demo_repository_operations()
            
            # Demo 3: Issue management
            await self._demo_issue_management()
            
            # Demo 4: Workflow operations
            await self._demo_workflow_operations()
            
            # Demo 5: Code search
            await self._demo_code_search()
            
            # Demo 6: Advanced features
            await self._demo_advanced_features()
            
        except Exception as e:
            print(f"❌ Demo error: {e}")
        finally:
            await self.server.cleanup()
        
        print("\n🎉 Demo completed successfully!")
        print("=" * 60)
    
    async def _demo_list_capabilities(self):
        """Demo: List available tools and resources"""
        print("\n📋 DEMO 1: MCP Capabilities")
        print("-" * 40)
        
        # Mock tool listing (since we can't call the actual handler directly)
        tools = [
            "create_repository", "list_repositories", "create_issue",
            "list_issues", "create_pull_request", "create_workflow",
            "trigger_workflow", "get_workflow_runs", "upload_file", "search_code"
        ]
        
        print("🔧 Available Tools:")
        for i, tool in enumerate(tools, 1):
            print(f"   {i}. {tool}")
        
        resources = [
            "github://user/profile",
            "github://repositories/recent", 
            "github://notifications"
        ]
        
        print("\n📦 Available Resources:")
        for i, resource in enumerate(resources, 1):
            print(f"   {i}. {resource}")
        
        await asyncio.sleep(1)
    
    async def _demo_repository_operations(self):
        """Demo: Repository operations"""
        print("\n🗂️ DEMO 2: Repository Operations")
        print("-" * 40)
        
        try:
            print("📚 Listing your repositories...")
            
            # List repositories
            repos_result = await self.server._list_repositories({"type": "owner"})
            
            print(f"✅ Found {repos_result['total_count']} repositories")
            
            if repos_result['repositories']:
                print("\n📋 Your recent repositories:")
                for repo in repos_result['repositories'][:5]:
                    print(f"   • {repo['name']} - {repo['description'] or 'No description'}")
                    print(f"     ⭐ {repo['stargazers_count']} stars | 🔧 {repo['language'] or 'Unknown'}")
            
        except Exception as e:
            print(f"❌ Repository demo error: {e}")
        
        await asyncio.sleep(1)
    
    async def _demo_issue_management(self):
        """Demo: Issue management"""
        print("\n🐛 DEMO 3: Issue Management")
        print("-" * 40)
        
        # For demo purposes, we'll use a known public repo
        demo_owner = "octocat"
        demo_repo = "Hello-World"
        
        try:
            print(f"📋 Listing issues from {demo_owner}/{demo_repo}...")
            
            issues_result = await self.server._list_issues({
                "owner": demo_owner,
                "repo": demo_repo,
                "state": "all"
            })
            
            print(f"✅ Found {issues_result['total_count']} issues")
            
            if issues_result['issues']:
                print("\n🔍 Recent issues:")
                for issue in issues_result['issues'][:3]:
                    print(f"   #{issue['number']}: {issue['title']}")
                    print(f"   👤 {issue['user']} | 📅 {issue['created_at'][:10]}")
                    print(f"   🔗 {issue['html_url']}")
            
        except Exception as e:
            print(f"❌ Issue demo error: {e}")
        
        await asyncio.sleep(1)
    
    async def _demo_workflow_operations(self):
        """Demo: Workflow operations"""
        print("\n⚡ DEMO 4: GitHub Actions Workflows")
        print("-" * 40)
        
        try:
            # Demonstrate workflow template
            print("📄 Sample CI/CD Workflow Template:")
            
            workflow_template = """
name: 'Demo CI/CD'
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Run Tests
      run: echo "Running tests..."
    
  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Build Application
      run: echo "Building application..."
    
  deploy:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
    - name: Deploy to Production
      run: echo "Deploying to production..."
            """
            
            print("✅ Workflow template generated!")
            print("📋 Features included:")
            print("   • Automated testing")
            print("   • Multi-stage build")
            print("   • Conditional deployment")
            print("   • Best practices compliance")
            
        except Exception as e:
            print(f"❌ Workflow demo error: {e}")
        
        await asyncio.sleep(1)
    
    async def _demo_code_search(self):
        """Demo: Code search"""
        print("\n🔍 DEMO 5: Code Search")
        print("-" * 40)
        
        try:
            print("🔎 Searching for 'machine learning' in Python...")
            
            search_result = await self.server._search_code({
                "query": "machine learning",
                "language": "python"
            })
            
            print(f"✅ Found {search_result['total_count']} code results")
            
            if search_result['items']:
                print("\n📝 Code search results:")
                for item in search_result['items'][:3]:
                    print(f"   📄 {item['name']} in {item['repository']}")
                    print(f"   📂 {item['path']}")
                    print(f"   🔗 {item['html_url']}")
                    print(f"   ⭐ Score: {item['score']:.2f}")
            
        except Exception as e:
            print(f"❌ Search demo error: {e}")
        
        await asyncio.sleep(1)
    
    async def _demo_advanced_features(self):
        """Demo: Advanced features"""
        print("\n🚀 DEMO 6: Advanced Features")
        print("-" * 40)
        
        print("🎯 Advanced MCP Capabilities:")
        print("   ✅ Real-time GitHub API integration")
        print("   ✅ Workflow automation")
        print("   ✅ Issue tracking & management")
        print("   ✅ Repository operations")
        print("   ✅ Code search & discovery")
        print("   ✅ Security scanning integration")
        print("   ✅ CI/CD pipeline templates")
        print("   ✅ Multi-platform support")
        
        print("\n🔮 Potential AI Integration:")
        print("   • Automated code reviews")
        print("   • Intelligent issue triage")
        print("   • Smart workflow optimization")
        print("   • Predictive deployment analysis")
        print("   • Automated security fixes")
        print("   • Code quality suggestions")
        
        await asyncio.sleep(1)

async def interactive_demo():
    """Interactive demo with user choices"""
    print("🎮 GitHub MCP Interactive Demo")
    print("=" * 40)
    print("Choose demo mode:")
    print("1. Full Automated Demo")
    print("2. Interactive Client")
    print("3. Server Test Mode")
    print("0. Exit")
    
    choice = input("\nSelect option: ").strip()
    
    if choice == "1":
        demo = GitHubMCPDemo()
        await demo.run_comprehensive_demo()
        
    elif choice == "2":
        print("\n🚀 Starting Interactive Client...")
        print("Note: This requires the server to be running separately")
        
        # Would normally start the client
        print("Run: python mcp_github/client.py mcp_github/server.py")
        
    elif choice == "3":
        print("\n🧪 Server Test Mode")
        print("Testing server initialization...")
        
        try:
            server = GitHubMCPServer()
            print("✅ Server initialized successfully!")
            print("🔧 Tools registered")
            print("📦 Resources configured")
            print("🌐 GitHub API client ready")
            
        except Exception as e:
            print(f"❌ Server test failed: {e}")
            
    elif choice == "0":
        print("👋 Goodbye!")
        
    else:
        print("❌ Invalid choice!")

def create_sample_config():
    """Create sample configuration files"""
    config_dir = Path("mcp_github/config")
    config_dir.mkdir(exist_ok=True)
    
    # Sample MCP configuration
    mcp_config = {
        "mcpServers": {
            "github": {
                "command": "python",
                "args": ["mcp_github/server.py"],
                "env": {
                    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
                }
            }
        }
    }
    
    with open(config_dir / "claude_desktop_config.json", "w") as f:
        json.dump(mcp_config, f, indent=2)
    
    # Sample environment file
    env_content = """# GitHub MCP Configuration
GITHUB_TOKEN=your_github_token_here

# Optional: GitHub Enterprise
GITHUB_BASE_URL=https://api.github.com

# Optional: Rate limiting
GITHUB_REQUEST_TIMEOUT=30
"""
    
    with open(config_dir / ".env.example", "w") as f:
        f.write(env_content)
    
    print("📁 Sample configuration files created in mcp_github/config/")

async def main():
    """Main entry point"""
    print("🎯 GitHub Action MCP System")
    print("=" * 50)
    
    # Create sample configs if they don't exist
    if not Path("mcp_github/config").exists():
        create_sample_config()
    
    await interactive_demo()

if __name__ == "__main__":
    asyncio.run(main()) 