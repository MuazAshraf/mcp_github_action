# 🚀 GitHub Action MCP (Model Context Protocol)

A complete **Model Context Protocol** implementation for **GitHub integration** that allows AI models to interact directly with GitHub repositories, issues, workflows, and more.

## 🎯 **Features**

### 🔧 **Tools Available**
- ✅ **Repository Management** - Create, list, and manage repositories
- ✅ **Issue Tracking** - Create, list, and manage issues  
- ✅ **Pull Requests** - Create and manage pull requests
- ✅ **GitHub Actions** - Create, trigger, and monitor workflows
- ✅ **File Operations** - Upload, update, and manage files
- ✅ **Code Search** - Search across GitHub repositories
- ✅ **Workflow Automation** - Complete CI/CD pipeline management

### 📦 **Resources Available**
- ✅ **User Profile** - Current GitHub user information
- ✅ **Recent Repositories** - Recently updated repositories
- ✅ **Notifications** - GitHub notifications and alerts

## 🚀 **Quick Start**

### 1. **Setup Requirements**

```bash
# Install dependencies
pip install -r mcp_github/requirements.txt

# Set GitHub token
export GITHUB_TOKEN="your_github_token_here"
```

### 2. **Get GitHub Token**
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token with `repo` permissions
3. Copy and set as environment variable

### 3. **Run Demo**

```bash
# Interactive demo
python3.13 mcp_github/demo.py

# Direct server test
python3.13 mcp_github/server.py
```

## 🎮 **Usage Examples**

### **Start MCP Server**
```bash
python3.13 mcp_github/server.py
```

### **Interactive Client**
```bash
python3.13 mcp_github/client.py mcp_github/server.py
```

### **Claude Desktop Integration**
Add to your Claude Desktop config:
```json
{
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
```

## 🔧 **Available Tools**

### **Repository Operations**
```python
# Create repository
{
  "name": "my-new-repo",
  "description": "My awesome project",
  "private": false
}

# List repositories
{
  "type": "owner",
  "username": "optional_username"
}
```

### **Issue Management**
```python
# Create issue
{
  "owner": "username",
  "repo": "repository",
  "title": "Bug report",
  "body": "Description of the issue",
  "labels": ["bug", "urgent"]
}

# List issues
{
  "owner": "username",
  "repo": "repository",
  "state": "open",
  "labels": "bug,feature"
}
```

### **Workflow Operations**
```python
# Create workflow
{
  "owner": "username",
  "repo": "repository", 
  "name": "ci-cd",
  "workflow_content": "name: CI\non: [push]\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n    - uses: actions/checkout@v4"
}

# Trigger workflow
{
  "owner": "username",
  "repo": "repository",
  "workflow_id": "ci-cd.yml",
  "ref": "main",
  "inputs": {"environment": "staging"}
}
```

### **Code Search**
```python
# Search code
{
  "query": "machine learning",
  "language": "python",
  "repo": "tensorflow/tensorflow"
}
```

## 📁 **Project Structure**

```
mcp_github/
├── server.py              # Main MCP server
├── client.py              # Interactive client
├── demo.py                # Comprehensive demo
├── requirements.txt       # Dependencies
├── README.md              # This file
├── workflows/
│   └── ci-cd-template.yml # GitHub Actions template
└── config/
    ├── claude_desktop_config.json
    └── .env.example
```

## 🎯 **Workflow Templates**

### **Complete CI/CD Pipeline**
Our GitHub Actions template includes:

- ✅ **Code Quality Checks** - Linting, formatting, security
- ✅ **Automated Testing** - Unit tests with coverage
- ✅ **Docker Build** - Multi-platform container builds  
- ✅ **Security Scanning** - Vulnerability assessment
- ✅ **Staging Deployment** - Automated staging releases
- ✅ **Production Deployment** - Controlled production releases
- ✅ **Rollback Support** - Automatic rollback on failure

### **Template Usage**
```python
# Use the built-in CI/CD template
workflow_content = open('mcp_github/workflows/ci-cd-template.yml').read()

# Create workflow in your repo
await create_workflow({
    "owner": "your-username",
    "repo": "your-repo", 
    "name": "ci-cd-pipeline",
    "workflow_content": workflow_content
})
```

## 🔒 **Security Features**

- ✅ **Token-based Authentication** - Secure GitHub API access
- ✅ **Rate Limiting** - Respects GitHub API limits
- ✅ **Error Handling** - Graceful error management
- ✅ **Input Validation** - Secure parameter validation
- ✅ **Audit Logging** - Complete operation logging

## 🚀 **Advanced Usage**

### **Automated Code Reviews**
```python
# Create PR with automated checks
pr_result = await create_pull_request({
    "owner": "username",
    "repo": "repository",
    "title": "Feature: Add new functionality", 
    "body": "## Changes\n- Added new feature\n- Updated tests",
    "head": "feature-branch",
    "base": "main"
})
```

### **Workflow Monitoring**
```python
# Monitor workflow runs
runs = await get_workflow_runs({
    "owner": "username",
    "repo": "repository",
    "status": "in_progress"
})
```

### **Bulk Operations**
```python
# Upload multiple files
for file_path, content in files.items():
    await upload_file({
        "owner": "username",
        "repo": "repository",
        "path": file_path,
        "content": content,
        "message": f"Update {file_path}"
    })
```

## 🎨 **Integration Examples**

### **With Claude/ChatGPT**
The MCP server can be integrated with any AI model that supports MCP:

1. **Code Analysis** - AI can analyze repository code and suggest improvements
2. **Issue Triage** - Automatically categorize and prioritize issues
3. **Workflow Optimization** - AI-powered CI/CD pipeline improvements
4. **Security Reviews** - Automated security vulnerability assessments

### **With Other Tools**
- **Slack Integration** - Notifications and commands via Slack
- **Jira Integration** - Sync issues between GitHub and Jira
- **Monitoring** - Integration with monitoring tools for deployment tracking

## 🏃‍♂️ **Performance**

- ⚡ **Async Operations** - Non-blocking GitHub API calls
- 🔄 **Connection Pooling** - Efficient HTTP connection management
- 📊 **Rate Limiting** - Intelligent API usage optimization
- 💾 **Caching** - Optional response caching for frequently accessed data

## 🐛 **Troubleshooting**

### **Common Issues**

1. **Authentication Failed**
   ```bash
   export GITHUB_TOKEN="your_token_here"
   # Make sure token has correct permissions
   ```

2. **Rate Limit Exceeded**
   ```bash
   # Check rate limit status
   curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/rate_limit
   ```

3. **Import Errors**
   ```bash
   pip install -r mcp_github/requirements.txt
   ```

### **Debug Mode**
```bash
# Run with debug logging
PYTHONPATH=. python3.13 mcp_github/server.py --debug
```

## 🤝 **Contributing**

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Make changes and test
4. Submit pull request

## 📄 **License**

MIT License - feel free to use in your own projects!

## 🌟 **What Makes This Special**

- 🔥 **Complete GitHub Integration** - Full API coverage
- 🎯 **Production Ready** - Error handling, logging, security
- 🚀 **Easy to Use** - Simple setup and intuitive API
- 🔧 **Extensible** - Easy to add new features
- 📚 **Well Documented** - Comprehensive guides and examples
- 🎨 **AI-First Design** - Built specifically for AI model integration

## 🚀 **Get Started Now!**

```bash
# Clone and setup
git clone <your-repo>
cd mcp_github_action
pip install -r mcp_github/requirements.txt
export GITHUB_TOKEN="your_token"

# Run demo
python3.13 mcp_github/demo.py
```

---

**Happy coding! 🎉** Build amazing AI-powered GitHub integrations with this MCP server! 