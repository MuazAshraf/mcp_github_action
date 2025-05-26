#!/usr/bin/env python3
"""
GitHub MCP Client
Test aur interact karne ke liye
"""

import asyncio
import json
import sys
from typing import Any, Dict, List
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client

class GitHubMCPClient:
    def __init__(self):
        self.session: ClientSession = None
    
    async def connect(self, server_script_path: str):
        """Connect to GitHub MCP server"""
        try:
            # Start server process and connect
            server_params = [sys.executable, server_script_path]
            
            async with stdio_client(server_params) as streams:
                async with ClientSession(streams[0], streams[1]) as session:
                    self.session = session
                    
                    # Initialize connection
                    await session.initialize()
                    
                    print("🎯 Connected to GitHub MCP Server!")
                    await self._interactive_session()
                    
        except Exception as e:
            print(f"❌ Connection failed: {e}")
    
    async def _interactive_session(self):
        """Interactive session with MCP server"""
        while True:
            print("\n" + "="*50)
            print("🚀 GitHub MCP Interactive Client")
            print("="*50)
            print("1. List Available Tools")
            print("2. List Available Resources") 
            print("3. Create Repository")
            print("4. List Repositories")
            print("5. Create Issue")
            print("6. List Issues")
            print("7. Create Workflow")
            print("8. Search Code")
            print("9. Custom Tool Call")
            print("0. Exit")
            print("="*50)
            
            choice = input("Select option: ").strip()
            
            try:
                if choice == "1":
                    await self._list_tools()
                elif choice == "2":
                    await self._list_resources()
                elif choice == "3":
                    await self._create_repository()
                elif choice == "4":
                    await self._list_repositories()
                elif choice == "5":
                    await self._create_issue()
                elif choice == "6":
                    await self._list_issues()
                elif choice == "7":
                    await self._create_workflow()
                elif choice == "8":
                    await self._search_code()
                elif choice == "9":
                    await self._custom_tool_call()
                elif choice == "0":
                    print("👋 Goodbye!")
                    break
                else:
                    print("❌ Invalid choice!")
                    
            except Exception as e:
                print(f"❌ Error: {e}")
            
            input("\nPress Enter to continue...")
    
    async def _list_tools(self):
        """List available tools"""
        print("\n🔧 Available Tools:")
        result = await self.session.list_tools()
        
        for i, tool in enumerate(result.tools, 1):
            print(f"\n{i}. {tool.name}")
            print(f"   📝 {tool.description}")
            if hasattr(tool, 'inputSchema') and tool.inputSchema:
                required = tool.inputSchema.get('required', [])
                if required:
                    print(f"   📋 Required: {', '.join(required)}")
    
    async def _list_resources(self):
        """List available resources"""
        print("\n📦 Available Resources:")
        result = await self.session.list_resources()
        
        for i, resource in enumerate(result.resources, 1):
            print(f"\n{i}. {resource.name}")
            print(f"   🔗 URI: {resource.uri}")
            print(f"   📝 {resource.description}")
    
    async def _create_repository(self):
        """Create new repository"""
        print("\n🆕 Create Repository")
        
        name = input("Repository name: ").strip()
        if not name:
            print("❌ Repository name required!")
            return
        
        description = input("Description (optional): ").strip()
        private = input("Private? (y/n): ").strip().lower() == 'y'
        
        args = {"name": name}
        if description:
            args["description"] = description
        args["private"] = private
        
        result = await self.session.call_tool("create_repository", args)
        self._print_result(result)
    
    async def _list_repositories(self):
        """List repositories"""
        print("\n📚 List Repositories")
        
        username = input("Username (leave empty for your repos): ").strip()
        repo_type = input("Type (all/owner/member) [owner]: ").strip() or "owner"
        
        args = {"type": repo_type}
        if username:
            args["username"] = username
        
        result = await self.session.call_tool("list_repositories", args)
        self._print_result(result)
    
    async def _create_issue(self):
        """Create issue"""
        print("\n🐛 Create Issue")
        
        owner = input("Repository owner: ").strip()
        repo = input("Repository name: ").strip()
        title = input("Issue title: ").strip()
        
        if not all([owner, repo, title]):
            print("❌ Owner, repo, and title are required!")
            return
        
        body = input("Issue body (optional): ").strip()
        labels_input = input("Labels (comma-separated, optional): ").strip()
        
        args = {
            "owner": owner,
            "repo": repo,
            "title": title
        }
        
        if body:
            args["body"] = body
        if labels_input:
            args["labels"] = [label.strip() for label in labels_input.split(",")]
        
        result = await self.session.call_tool("create_issue", args)
        self._print_result(result)
    
    async def _list_issues(self):
        """List issues"""
        print("\n📋 List Issues")
        
        owner = input("Repository owner: ").strip()
        repo = input("Repository name: ").strip()
        
        if not all([owner, repo]):
            print("❌ Owner and repo are required!")
            return
        
        state = input("State (open/closed/all) [open]: ").strip() or "open"
        labels = input("Filter by labels (optional): ").strip()
        
        args = {
            "owner": owner,
            "repo": repo,
            "state": state
        }
        
        if labels:
            args["labels"] = labels
        
        result = await self.session.call_tool("list_issues", args)
        self._print_result(result)
    
    async def _create_workflow(self):
        """Create GitHub Action workflow"""
        print("\n⚡ Create Workflow")
        
        owner = input("Repository owner: ").strip()
        repo = input("Repository name: ").strip()
        name = input("Workflow name: ").strip()
        
        if not all([owner, repo, name]):
            print("❌ Owner, repo, and name are required!")
            return
        
        print("\nEnter workflow YAML (end with '###'):")
        workflow_lines = []
        while True:
            line = input()
            if line.strip() == "###":
                break
            workflow_lines.append(line)
        
        workflow_content = "\n".join(workflow_lines)
        
        if not workflow_content.strip():
            print("❌ Workflow content cannot be empty!")
            return
        
        args = {
            "owner": owner,
            "repo": repo,
            "name": name,
            "workflow_content": workflow_content
        }
        
        result = await self.session.call_tool("create_workflow", args)
        self._print_result(result)
    
    async def _search_code(self):
        """Search code"""
        print("\n🔍 Search Code")
        
        query = input("Search query: ").strip()
        if not query:
            print("❌ Search query required!")
            return
        
        language = input("Language filter (optional): ").strip()
        repo = input("Repository filter (owner/repo, optional): ").strip()
        
        args = {"query": query}
        if language:
            args["language"] = language
        if repo:
            args["repo"] = repo
        
        result = await self.session.call_tool("search_code", args)
        self._print_result(result)
    
    async def _custom_tool_call(self):
        """Custom tool call"""
        print("\n🛠️ Custom Tool Call")
        
        # List available tools first
        tools_result = await self.session.list_tools()
        print("\nAvailable tools:")
        for i, tool in enumerate(tools_result.tools, 1):
            print(f"{i}. {tool.name}")
        
        tool_name = input("\nTool name: ").strip()
        if not tool_name:
            print("❌ Tool name required!")
            return
        
        print("Enter arguments as JSON (or empty for no args):")
        args_input = input().strip()
        
        if args_input:
            try:
                args = json.loads(args_input)
            except json.JSONDecodeError as e:
                print(f"❌ Invalid JSON: {e}")
                return
        else:
            args = {}
        
        result = await self.session.call_tool(tool_name, args)
        self._print_result(result)
    
    def _print_result(self, result):
        """Print tool call result"""
        print("\n📄 Result:")
        print("-" * 40)
        
        if hasattr(result, 'content') and result.content:
            for content in result.content:
                if hasattr(content, 'text'):
                    try:
                        # Try to pretty print JSON
                        data = json.loads(content.text)
                        print(json.dumps(data, indent=2))
                    except json.JSONDecodeError:
                        print(content.text)
        else:
            print("No content returned")
        
        if hasattr(result, 'isError') and result.isError:
            print("⚠️ This was an error result")

async def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Usage: python client.py <server_script_path>")
        print("Example: python client.py mcp_github/server.py")
        return
    
    server_script = sys.argv[1]
    client = GitHubMCPClient()
    await client.connect(server_script)

if __name__ == "__main__":
    asyncio.run(main()) 