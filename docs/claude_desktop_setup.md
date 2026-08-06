# Claude Desktop Setup Guide

This guide covers Claude Desktop configuration for both users (PyPI installation) and developers (source installation).

## 🤖 Claude Desktop Overview

Claude Desktop is Anthropic's desktop application with native MCP (Model Context Protocol) support. It's the recommended client for most users.

> 📖 **External Setup Guide**: Detailed Claude Desktop configuration also available at [playbooks.com](https://playbooks.com/mcp/stevereiner-alfresco-content-services#claude-desktop-setup)

## 📍 Configuration File Location

First, locate your Claude Desktop configuration file:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: Not supported by Claude Desktop

## 👤 User Installation (PyPI)

For users who installed the package from PyPI, choose the installation method that works best for your system:

### Option 1: pipx (Recommended)

**Installation:**
```bash
pipx install python-alfresco-mcp-server
```

**Configuration:**

**Windows** (use [claude-desktop-config-pipx-windows.json](../claude-desktop-configs/claude-desktop-config-pipx-windows.json)):
```json
{
  "mcpServers": {
    "python-alfresco-mcp-server": {
      "command": "python-alfresco-mcp-server",
      "args": ["--transport", "stdio"],
      "env": {
        "ALFRESCO_URL": "http://localhost:8080",
        "ALFRESCO_USERNAME": "admin",
        "ALFRESCO_PASSWORD": "admin",
        "PYTHONIOENCODING": "utf-8",
        "PYTHONLEGACYWINDOWSSTDIO": "1"
      }
    }
  }
}
```

**macOS** (use [claude-desktop-config-pipx-macos.json](../claude-desktop-configs/claude-desktop-config-pipx-macos.json)):
```json
{
  "mcpServers": {
    "python-alfresco-mcp-server": {
      "command": "python-alfresco-mcp-server",
      "args": ["--transport", "stdio"],
      "env": {
        "ALFRESCO_URL": "http://localhost:8080",
        "ALFRESCO_USERNAME": "admin",
        "ALFRESCO_PASSWORD": "admin"
      }
    }
  }
}
```

### Option 2: Manual Virtual Environment

**Installation:**
```bash
# Create and activate venv
python -m venv alfresco-mcp-env
source alfresco-mcp-env/bin/activate  # Linux/macOS
# or
alfresco-mcp-env\Scripts\activate     # Windows

# Install the package
pip install python-alfresco-mcp-server
```

**Configuration:**

You'll need the **full path** to the executable in your virtual environment:

**Windows:**
```json
{
  "mcpServers": {
    "python-alfresco-mcp-server": {
      "command": "C:\\path\\to\\alfresco-mcp-env\\Scripts\\python-alfresco-mcp-server.exe",
      "args": ["--transport", "stdio"],
      "env": {
        "ALFRESCO_URL": "http://localhost:8080",
        "ALFRESCO_USERNAME": "admin",
        "ALFRESCO_PASSWORD": "admin",
        "PYTHONIOENCODING": "utf-8",
        "PYTHONLEGACYWINDOWSSTDIO": "1"
      }
    }
  }
}
```

**macOS/Linux:**
```json
{
  "mcpServers": {
    "python-alfresco-mcp-server": {
      "command": "/path/to/alfresco-mcp-env/bin/python-alfresco-mcp-server",
      "args": ["--transport", "stdio"],
      "env": {
        "ALFRESCO_URL": "http://localhost:8080",
        "ALFRESCO_USERNAME": "admin",
        "ALFRESCO_PASSWORD": "admin"
      }
    }
  }
}
```

### Option 3: UV (Modern Package Manager)

**Installation:**
```bash
# Install UV first
pip install uv

# Add the package
uv add python-alfresco-mcp-server
```

**Configuration:**
```json
{
  "mcpServers": {
    "python-alfresco-mcp-server": {
      "command": "uv",
      "args": ["run", "python-alfresco-mcp-server", "--transport", "stdio"],
      "env": {
        "ALFRESCO_URL": "http://localhost:8080",
        "ALFRESCO_USERNAME": "admin",
        "ALFRESCO_PASSWORD": "admin"
      }
    }
  }
}
```

**Windows (with encoding fixes):**
```json
{
  "mcpServers": {
    "python-alfresco-mcp-server": {
      "command": "uv",
      "args": ["run", "python-alfresco-mcp-server", "--transport", "stdio"],
      "env": {
        "ALFRESCO_URL": "http://localhost:8080",
        "ALFRESCO_USERNAME": "admin",
        "ALFRESCO_PASSWORD": "admin",
        "PYTHONIOENCODING": "utf-8",
        "PYTHONLEGACYWINDOWSSTDIO": "1"
      }
    }
  }
}
```

## 👨‍💻 Developer Installation (Source Code)

For developers using the source code repository:

### Configuration Files

Use the included configuration files:

**Windows** (use [claude-desktop-config-uv-windows.json](../claude-desktop-configs/claude-desktop-config-uv-windows.json)):
```json
{
  "mcpServers": {
    "python-alfresco-mcp-server": {
      "command": "uv",
      "args": ["run", "python-alfresco-mcp-server", "--transport", "stdio"],
      "cwd": "C:\\path\\to\\python-alfresco-mcp-server",
      "env": {
        "ALFRESCO_URL": "http://localhost:8080",
        "ALFRESCO_USERNAME": "admin",
        "ALFRESCO_PASSWORD": "admin",
        "PYTHONIOENCODING": "utf-8",
        "PYTHONLEGACYWINDOWSSTDIO": "1"
      }
    }
  }
}
```

**macOS** (use [claude-desktop-config-uv-macos.json](../claude-desktop-configs/claude-desktop-config-uv-macos.json)):
```json
{
  "mcpServers": {
    "python-alfresco-mcp-server": {
      "command": "uv",
      "args": ["run", "python-alfresco-mcp-server", "--transport", "stdio"],
      "cwd": "/path/to/python-alfresco-mcp-server",
      "env": {
        "ALFRESCO_URL": "http://localhost:8080",
        "ALFRESCO_USERNAME": "admin",
        "ALFRESCO_PASSWORD": "admin"
      }
    }
  }
}
```

### Traditional Development Setup

If using traditional pip with virtual environment:

```json
{
  "mcpServers": {
    "python-alfresco-mcp-server": {
      "command": "/path/to/venv/bin/python",
      "args": ["-m", "alfresco_mcp_server.fastmcp_server", "--transport", "stdio"],
      "cwd": "/path/to/python-alfresco-mcp-server",
      "env": {
        "ALFRESCO_URL": "http://localhost:8080",
        "ALFRESCO_USERNAME": "admin",
        "ALFRESCO_PASSWORD": "admin"
      }
    }
  }
}
```

## 🔧 Configuration Steps

1. **Locate Configuration File**: Find your platform-specific Claude Desktop config file
2. **Choose Installation Method**: Select the appropriate configuration based on how you installed the package
3. **Copy Configuration**: Use one of the configurations above or the provided files
4. **Customize Settings**: Update paths, URLs, and credentials for your environment
5. **Restart Claude Desktop**: Close and reopen Claude Desktop for changes to take effect

## ✅ Verification

After configuration:

1. **Check Connection Status**:
   - Go to **File → Settings → Developer**
   - Look for "python-alfresco-mcp-server" in the list
   - Status should show as "running"

2. **Test Basic Functionality**:
   - Start a new chat
   - Try asking about your Alfresco repository
   - Use the repository_info tool to verify connection

## 🛠️ Using the Tools

Once connected, you can:

### Chat Naturally
Just describe what you want to do with documents:
- "Search for PDFs about project planning"
- "Upload this document to the Sales folder"
- "Show me recent documents modified by John"

### Use Search Tools
Access 4 different search capabilities:
- **search_content** - Full text search
- **advanced_search** - AFTS query language
- **search_by_metadata** - Property-based queries  
- **cmis_search** - SQL-like queries

### Quick Access
- Click **"Search and tools"** button in chat for tool access
- Click **"+" → "Add from alfresco"** for resources
- Use the **Search and Analyze Prompt** for guided searches

## 🔧 Environment Variables

Customize these variables for your Alfresco server:

| Variable | Default | Description |
|----------|---------|-------------|
| `ALFRESCO_URL` | `http://localhost:8080` | Your Alfresco server URL |
| `ALFRESCO_USERNAME` | `admin` | Username for authentication |
| `ALFRESCO_PASSWORD` | `admin` | Password for authentication |
| `ALFRESCO_VERIFY_SSL` | `false` | Verify SSL certificates |
| `ALFRESCO_TIMEOUT` | `30` | Request timeout (seconds) |

### Windows-Specific Variables

For Windows systems experiencing character encoding issues:

- `PYTHONIOENCODING`: `"utf-8"`
- `PYTHONLEGACYWINDOWSSTDIO`: `"1"`

## 🚀 Transport Options

The server supports three transport protocols:

- **STDIO** (default): Fastest, direct MCP protocol
- **HTTP**: Add `"--port", "8001"` to args for web services
- **SSE**: Add `"--port", "8003"` to args for real-time streaming

## 🛠️ Troubleshooting

### Common Issues

1. **"Command not found" error**:
   - For pipx: Run `pipx list` to verify installation
   - For venv: Check the full path to executable
   - For UV: Ensure UV is installed and working directory is correct

2. **Connection failures**:
   - Verify Alfresco server is running: `curl http://localhost:8080/alfresco`
   - Check username/password are correct
   - Confirm environment variables are set properly

3. **Character encoding issues (Windows)**:
   - Ensure `PYTHONIOENCODING` and `PYTHONLEGACYWINDOWSSTDIO` are set
   - Try restarting Claude Desktop after adding these variables

4. **Tools not appearing**:
   - Check that server status shows "running" in Developer settings
   - Verify no error messages in Claude Desktop logs
   - Try restarting Claude Desktop

### Getting Help

- 📚 **Documentation**: [Documentation Hub](./README.md)
- 🛠️ **Troubleshooting**: [Troubleshooting Guide](./troubleshooting.md)
- 🐛 **Issues**: [GitHub Issues](https://github.com/stevereiner/python-alfresco-mcp-server/issues)

## ⚠️ Security Best Practices

- **Never commit real credentials** to version control
- **Use environment variables** for production deployments  
- **Use strong passwords** for production Alfresco servers
- **Consider SSL/TLS** for production environments
- **Review permissions** - ensure MCP user has appropriate access levels 