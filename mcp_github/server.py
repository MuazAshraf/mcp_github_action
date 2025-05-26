#!/usr/bin/env python3
"""
GitHub Action MCP Server
AI models ke liye GitHub integration
"""

import asyncio
import json
import os
import base64
from pathlib import Path
import logging
from typing import Any, Dict, List, Optional

import aiohttp
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load environment variables from .env file
script_dir = Path(__file__).parent
env_path = script_dir / '.env'
load_dotenv(env_path)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("github-mcp-server")

# GitHub configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN environment variable is required")

# Create FastMCP server
mcp = FastMCP("github-mcp")

async def get_github_session():
    """Get or create GitHub API session"""
    return aiohttp.ClientSession()

async def github_request(method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
    """Make authenticated GitHub API request"""
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "GitHub-MCP-Server"
    }
    
    url = f"https://api.github.com/{endpoint.lstrip('/')}"
    
    async with aiohttp.ClientSession() as session:
        async with session.request(method, url, headers=headers, json=data) as response:
            if response.status >= 400:
                error_text = await response.text()
                raise Exception(f"GitHub API error {response.status}: {error_text}")
            
            return await response.json()

@mcp.tool()
async def create_repository(name: str, description: str = "", private: bool = False, auto_init: bool = True) -> str:
    """Create a new GitHub repository"""
    data = {
        "name": name,
        "description": description,
        "private": private,
        "auto_init": auto_init
    }
    
    result = await github_request("POST", "/user/repos", data)
    return json.dumps(result, indent=2)

@mcp.tool()
async def list_repositories(username: str = "", repo_type: str = "owner") -> str:
    """List user repositories"""
    if username:
        endpoint = f"/users/{username}/repos"
    else:
        endpoint = f"/user/repos?type={repo_type}"
    
    repos = await github_request("GET", endpoint)
    
    result = {
        "total_count": len(repos),
        "repositories": [
            {
                "name": repo["name"],
                "full_name": repo["full_name"],
                "description": repo["description"],
                "private": repo["private"],
                "html_url": repo["html_url"],
                "created_at": repo["created_at"],
                "updated_at": repo["updated_at"],
                "language": repo["language"],
                "stargazers_count": repo["stargazers_count"]
            }
            for repo in repos[:20]  # Limit to 20 for readability
        ]
    }
    
    return json.dumps(result, indent=2)

@mcp.tool()
async def create_issue(owner: str, repo: str, title: str, body: str = "", labels: List[str] = None) -> str:
    """Create an issue in a repository"""
    if labels is None:
        labels = []
        
    data = {
        "title": title,
        "body": body,
        "labels": labels
    }
    
    result = await github_request("POST", f"/repos/{owner}/{repo}/issues", data)
    return json.dumps(result, indent=2)

@mcp.tool()
async def list_issues(owner: str, repo: str, state: str = "open", labels: str = "") -> str:
    """List repository issues"""
    endpoint = f"/repos/{owner}/{repo}/issues?state={state}"
    if labels:
        endpoint += f"&labels={labels}"
    
    issues = await github_request("GET", endpoint)
    
    result = {
        "total_count": len(issues),
        "issues": [
            {
                "number": issue["number"],
                "title": issue["title"],
                "body": issue["body"][:200] + "..." if len(issue["body"]) > 200 else issue["body"],
                "state": issue["state"],
                "user": issue["user"]["login"],
                "created_at": issue["created_at"],
                "html_url": issue["html_url"]
            }
            for issue in issues[:10]
        ]
    }
    
    return json.dumps(result, indent=2)

@mcp.tool()
async def create_pull_request(owner: str, repo: str, title: str, head: str, base: str = "main", body: str = "") -> str:
    """Create a pull request"""
    data = {
        "title": title,
        "body": body,
        "head": head,
        "base": base
    }
    
    result = await github_request("POST", f"/repos/{owner}/{repo}/pulls", data)
    return json.dumps(result, indent=2)

@mcp.tool()
async def upload_file(owner: str, repo: str, path: str, content: str, message: str, branch: str = "main") -> str:
    """Upload or update a file in repository"""
    # Check if file exists to get SHA for update
    try:
        existing = await github_request("GET", f"/repos/{owner}/{repo}/contents/{path}?ref={branch}")
        sha = existing["sha"]
    except:
        sha = None
    
    data = {
        "message": message,
        "content": base64.b64encode(content.encode()).decode(),
        "branch": branch
    }
    
    if sha:
        data["sha"] = sha
    
    result = await github_request("PUT", f"/repos/{owner}/{repo}/contents/{path}", data)
    return json.dumps(result, indent=2)

@mcp.tool()
async def search_code(query: str, language: str = "", repo: str = "") -> str:
    """Search code across GitHub"""
    search_query = query
    if language:
        search_query += f" language:{language}"
    if repo:
        search_query += f" repo:{repo}"
    
    results = await github_request("GET", f"/search/code?q={search_query}")
    
    result = {
        "total_count": results["total_count"],
        "items": [
            {
                "name": item["name"],
                "path": item["path"],
                "repository": item["repository"]["full_name"],
                "html_url": item["html_url"],
                "score": item["score"]
            }
            for item in results["items"][:10]
        ]
    }
    
    return json.dumps(result, indent=2)

@mcp.tool()
async def get_user_info() -> str:
    """Get current GitHub user information"""
    result = await github_request("GET", "/user")
    return json.dumps(result, indent=2)

@mcp.resource("github://user/profile")
async def get_user_profile() -> str:
    """Get current GitHub user profile"""
    result = await github_request("GET", "/user")
    return json.dumps(result, indent=2)

@mcp.resource("github://repositories/recent")
async def get_recent_repositories() -> str:
    """Get recently updated repositories"""
    repos = await github_request("GET", "/user/repos?sort=updated&per_page=10")
    return json.dumps({"repositories": repos}, indent=2)

@mcp.tool()
async def get_issue_comments(owner: str, repo: str, issue_number: int) -> str:
    """Get all comments for a specific issue"""
    comments = await github_request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}/comments")
    
    result = {
        "issue_number": issue_number,
        "total_comments": len(comments),
        "comments": [
            {
                "id": comment["id"],
                "user": comment["user"]["login"],
                "body": comment["body"],
                "created_at": comment["created_at"],
                "updated_at": comment["updated_at"],
                "html_url": comment["html_url"]
            }
            for comment in comments
        ]
    }
    
    return json.dumps(result, indent=2)

@mcp.tool()
async def create_issue_comment(owner: str, repo: str, issue_number: int, body: str) -> str:
    """Add a comment to an issue"""
    data = {
        "body": body
    }
    
    result = await github_request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", data)
    return json.dumps(result, indent=2)

@mcp.tool()
async def get_issue_details(owner: str, repo: str, issue_number: int) -> str:
    """Get detailed information about a specific issue including comments count"""
    issue = await github_request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")
    
    result = {
        "number": issue["number"],
        "title": issue["title"],
        "body": issue["body"],
        "state": issue["state"],
        "user": issue["user"]["login"],
        "assignees": [assignee["login"] for assignee in issue["assignees"]],
        "labels": [label["name"] for label in issue["labels"]],
        "comments_count": issue["comments"],
        "created_at": issue["created_at"],
        "updated_at": issue["updated_at"],
        "html_url": issue["html_url"]
    }
    
    return json.dumps(result, indent=2)

if __name__ == "__main__":
    mcp.run() 