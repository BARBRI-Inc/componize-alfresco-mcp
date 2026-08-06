# Python Alfresco MCP Server v1.2 🚀

[![PyPI version](https://img.shields.io/pypi/v/python-alfresco-mcp-server)](https://pypi.org/project/python-alfresco-mcp-server/)
[![PyPI downloads](https://pepy.tech/badge/python-alfresco-mcp-server)](https://pepy.tech/project/python-alfresco-mcp-server)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://pypi.org/project/python-alfresco-mcp-server/)
[![License](https://img.shields.io/github/license/stevereiner/python-alfresco-mcp-server)](https://github.com/stevereiner/python-alfresco-mcp-server/blob/main/LICENSE)

**Model Context Protocol Server for Alfresco Content Services**

A full featured MCP server for Alfresco in search and content management areas. It provides the following tools: full text search (content and properties), advanced search, metadata search, CMIS SQL like search, upload, download,
checkin, checkout, cancel checkout, create folder, folder browse, delete node, and get/set properties. Also has a  tool for getting repository status/config (also a resource). Has one prompt example.
Built with [FastMCP 3](https://github.com/PrefectHQ/fastmcp). 
Features complete documentation, examples, and 
config for various MCP clients (Claude Desktop, MCP Inspector, references to configuring others).

## 🌟 What's New in v1.2

- **Alfresco authentication methods**: connect via **basic**, **ticket**, or **OAuth2/OIDC** (`ALFRESCO_AUTH_METHOD` + `ALFRESCO_OAUTH2_*`, backed by `python-alfresco-api` 1.2.1) — see [Authentication](#-authentication).
- **Optional MCP transport authentication**: secure the MCP server itself with an OAuth2 bearer token (`MCP_TRANSPORT_AUTH=true`), validated against your IdP's JWKS (HTTP/SSE transports; stdio unaffected).
- **FastMCP 3**: upgraded to `fastmcp>=3.4.5,<4` (transport auth uses `JWTVerifier`).
- **`download_document` custom folder**: optional `destination_dir` (default `~/Downloads`) — thanks [@jeremie-lesage](https://github.com/jeremie-lesage) ([#1](https://github.com/stevereiner/python-alfresco-mcp-server/pull/1)).
- **Packaging**: switched to the hatchling build backend.
- Requires **python-alfresco-api ≥ 1.2.1** (OAuth2/OIDC auth + OAuth2 service-account `displayName` fix).

## 🌟 What's New in v1.1

### **Modular Architecture & Enhanced Testing**
- **FastMCP**: v1.0 had FastMCP 2.0 implementation that had all tools implementations in the fastmcp_server.py file
- **Code Modularization in v1.1**: Split monolithic single file into organized modular structure with separate files
- **Directory Organization**: Organized into `tools/search/`, `tools/core/`, `resources/`, `prompts/`, `utils/` directories
- **Enhanced Testing**: Complete test suite transformation - 143 tests with 100% pass rate
- **Client Configuration Files**: Added dedicated Claude Desktop and MCP Inspector configuration files
- **Live Integration Testing**: 21 Alfresco server validation tests for real-world functionality
- **Python-Alfresco-API**: python-alfresco-mcp-server v1.2.0 requires python-alfresco-api >= 1.2.1

## 📚 Complete Documentation

### **Documentation & Examples**
- **📚 Complete Documentation**: 10 guides covering setup to deployment
- **💡 Examples**: 6 practical examples from quick start to implementation patterns  
- **🔧 Configuration Management**: Environment variables, .env files, and command-line configuration
- **🏗️ Setup instruction for use with MCP client

### **Learning Resources**
- **🚀 [Quick Start Guide](./docs/quick_start_guide.md)**: 5-minute setup and first operations
- **🤖 [Claude Desktop Setup](./docs/claude_desktop_setup.md)**: Complete Claude Desktop configuration for users and developers
- **🔧 [Client Configurations](./docs/client_configurations.md)**: Setup guide for Cursor, Claude Code, and other MCP clients
- **📖 [Examples Library](./examples/README.md)**: Implementation patterns and examples

### 📖 Guides covering setup, deployment, and usage:

- **[📚 Documentation Hub](./docs/README.md)** - Complete navigation and overview
- **[🚀 Quick Start Guide](./docs/quick_start_guide.md)** - 5-minute setup and first operations
- **[📦 Installation with pip and pipx](./docs/install_with_pip_pipx.md)** - Traditional Python package installation methods
- **[🤖 Claude Desktop Setup](./docs/claude_desktop_setup.md)** - Complete Claude Desktop configuration for users and developers
- **[🔧 Client Configurations](./docs/client_configurations.md)** - Setup guide for Cursor, Claude Code, and other MCP clients
- **[🔍 MCP Inspector Setup](./docs/mcp_inspector_setup.md)** - Development and testing with MCP Inspector
- **[🔍 API Reference](./docs/api_reference.md)** - Complete tool and resource documentation
- **[⚙️ Configuration Guide](./docs/configuration_guide.md)** - Development to deployment
- **[🧪 Testing Guide](./docs/testing_guide.md)** - Quality assurance and test development
- **[🛠️ Troubleshooting Guide](./docs/troubleshooting.md)** - Problem diagnosis and resolution

## 🚀 Features

### Content Management and Search Tools
- **Search Tools**: 
  - **Full Text Search**: Basic content search with wildcard support (search_content)
  - **Advanced Search**: AFTS query language with date filters, sorting, and field targeting
  - **Metadata Search**: Property-based queries with operators (equals, contains, date ranges)
  - **CMIS Search**: SQL like queries for complex content discovery
- **Document Lifecycle**: Upload, download, check-in, checkout, cancel checkout
- **Version Management**: Create major/minor versions with comments
- **Folder Operations**: Create folders, delete folder nodes
- **Property Management**: Get and set document/folder properties and names
- **Node Operations**: Delete nodes (documents and folders) (trash or permanent)
- **Repository Info**: (Tool and Resource) Returns repository status, version and whether Community or Enterprise, and module configuration

### MCP Architecture
- **FastMCP 3 Framework**: Modern, high-performance MCP server implementation
- **Multiple Transports**: 
  - **STDIO** (direct MCP protocol) - Default and fastest
  - **HTTP** (RESTful API) - Web services and testing
  - **SSE** (Server-Sent Events) - Real-time streaming updates
- **Authentication**: Basic, ticket, or OAuth2/OIDC to Alfresco, plus optional OAuth2 bearer to secure the MCP transport itself — see [Authentication](#-authentication)
- **Type Safety**: Full Pydantic v2 models
- **In-Memory Testing**: Client testing with faster execution
- **Configuration**: Environment variables, .env files

### Alfresco Integration 
Works with Alfresco Community (tested) and Enterprise editions


## 📋 Requirements

- Python 3.10+
- Alfresco Content Services (Community or Enterprise)

> **Note**: The `python-alfresco-api >= 1.2.1` dependency is automatically installed with `python-alfresco-mcp-server`

## 🛠️ Installation

### Install Python

You need to have Python 3.10+ installed for the sections below. If not, download the latest 3.13.x version from:

[Python.org Downloads](https://www.python.org/downloads/)

### UV/UVX Setup (Recommended)

**UV** is a modern Python package manager written in **Rust** that provides both `uv` (package manager) and `uvx` (tool runner). **Much faster than pip** due to its compiled nature and optimized dependency resolution.

```bash
# Install UV (provides both uv and uvx commands)
# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux  
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or via pip if you prefer
pip install uv

# Verify installation (both commands should work)
uv --version
uvx --version
```

**UV Reference Links:**
- **[UV Installation Guide](https://docs.astral.sh/uv/getting-started/installation/)** - Official installation instructions and platform-specific options
- **[UV Documentation](https://docs.astral.sh/uv/)** - Complete UV documentation, guides, and advanced usage

### Option A: UVX - Modern Tool Runner (Recommended for Users)

**UVX** is UV's tool runner - similar to pipx but faster and more modern. Automatically handles isolation and global availability:

```bash
# Install python-alfresco-mcp-server with uvx (after UV/UVX setup above)
uvx python-alfresco-mcp-server --help

# This tests that installation worked - UVX automatically installs packages on first use!
```

**Why UVX?** UVX combines the benefits of pipx (isolated environments + global availability) with UV's Rust-based speed and modern dependency resolution. It automatically installs packages on first use.

### Option B: UV - Modern Package Manager (Recommended for Development)

**UV** is a modern Python package manager written in **Rust** that handles everything automatically. **Much faster than pip** due to its compiled nature and optimized dependency resolution.

```bash
# Install and run from PyPI (fastest for users)
uv tool install python-alfresco-mcp-server
uv tool run python-alfresco-mcp-server --help  # Tests that installation worked

# Or install from source (for development)
git clone https://github.com/stevereiner/python-alfresco-mcp-server.git
cd python-alfresco-mcp-server
uv run python-alfresco-mcp-server --help  # Tests that installation worked
```

### Option C: Traditional Methods (pip and pipx)

For traditional Python package management approaches, see the **[Installation with pip and pipx](./docs/install_with_pip_pipx.md)**.

**Note**: You still need to configure your MCP client (Claude Desktop, MCP Inspector, etc.) with the appropriate configuration. See the [MCP Client Setup and Use](#mcp-client-setup-and-use) section below for client configuration details.

### Source Installation (For Development)

For development or access to latest features:

```bash
# 1. Clone the repository
git clone https://github.com/stevereiner/python-alfresco-mcp-server.git
cd python-alfresco-mcp-server

# 2. UV handles everything automatically - run immediately!
uv run python-alfresco-mcp-server --help  # Tests that installation worked

# Or install dependencies explicitly for development:
uv sync                    # Basic dependencies
uv sync --extra dev        # With development tools  
uv sync --extra test       # With testing tools
uv sync --extra all        # Everything

# Or an editable install into the active virtual environment (pip-style):
uv pip install -e .
```

### 4. Configure Alfresco Connection

> The examples below use HTTP **Basic** auth. Alfresco also supports **ticket** and **OAuth2/OIDC** (`ALFRESCO_AUTH_METHOD` + `ALFRESCO_OAUTH2_*`), and you can optionally secure the MCP transport with an OAuth2 bearer (`MCP_TRANSPORT_AUTH`) — see the [Authentication](#-authentication) section for all methods.

**Option 1: Environment Variables**
```bash
# Linux/Mac
export ALFRESCO_URL="http://localhost:8080"
export ALFRESCO_USERNAME="admin"
export ALFRESCO_PASSWORD="admin"
export ALFRESCO_VERIFY_SSL="false"

# Windows PowerShell
$env:ALFRESCO_URL="http://localhost:8080"
$env:ALFRESCO_USERNAME="admin"
$env:ALFRESCO_PASSWORD="admin"
$env:ALFRESCO_VERIFY_SSL="false"

# Windows Command Prompt
set ALFRESCO_URL=http://localhost:8080
set ALFRESCO_USERNAME=admin
set ALFRESCO_PASSWORD=admin
set ALFRESCO_VERIFY_SSL=false
```

**Option 2: .env file** (recommended - cross-platform):
```bash
# Copy sample-dot-env.txt to .env and customize
# Linux/macOS
cp sample-dot-env.txt .env

# Windows
copy sample-dot-env.txt .env

# Edit .env file with your settings
ALFRESCO_URL=http://localhost:8080
ALFRESCO_USERNAME=admin
ALFRESCO_PASSWORD=admin
ALFRESCO_VERIFY_SSL=false
```
> **Note**: The `.env` file is not checked into git for security. Use `sample-dot-env.txt` as a template.

📖 **See [Configuration Guide](./docs/configuration_guide.md) for complete setup options**

## Alfresco Installation 

If you don't have an Alfresco server installed you can get a docker for the 
Community version from Github

```bash
git clone https://github.com/Alfresco/acs-deployment.git
```

**Move to Docker Compose directory**

```bash
cd acs-deployment/docker-compose
```

**Edit community-compose.yaml**
- Note: you will likely need to comment out activemq ports other than 8161

```bash   
   ports:
   - "8161:8161" # Web Console
   #- "5672:5672" # AMQP
   #- "61616:61616" # OpenWire
   #- "61613:61613" # STOMP
```      

**Start Alfresco with Docker Compose**

```bash
docker-compose -f community-compose.yaml up
```

## 🚀 Usage

### MCP Server Startup

**With UVX (Recommended - Automatic isolation and global availability):**

```bash
# Run MCP server with STDIO transport (default)
uvx python-alfresco-mcp-server

# HTTP transport for web services (matches MCP Inspector)
uvx python-alfresco-mcp-server --transport http --host 127.0.0.1 --port 8003

# SSE transport for real-time streaming  
uvx python-alfresco-mcp-server --transport sse --host 127.0.0.1 --port 8001
```

**With UV (For development or source installations):**

```bash
# Run MCP server with STDIO transport (default)
uv run python-alfresco-mcp-server

# HTTP transport for web services (matches MCP Inspector)
uv run python-alfresco-mcp-server --transport http --host 127.0.0.1 --port 8003

# SSE transport for real-time streaming  
uv run python-alfresco-mcp-server --transport sse --host 127.0.0.1 --port 8001
```

**With Traditional Methods (pip/pipx):**

See the **[Installation with pip and pipx](./docs/install_with_pip_pipx.md)** for pip and pipx usage instructions.

### MCP Client Setup and Use

Python-Alfresco-MCP-Server was tested with Claude Desktop which is recommended as an end user MCP client. Python-Alfresco-MCP-Server was also tested with MCP Inspector which is recommended for developers to test tools with argument values.

#### 🤖 **Claude Desktop** for Windows (tested) and MacOS (not tested)

📖 **Complete Setup Guide**: **[Claude Desktop Setup Guide](./docs/claude_desktop_setup.md)**

**📥 Download Claude Desktop (Free and Pro versions):**
- **[Download Claude Desktop](https://claude.ai/download)** - Official Anthropic download page
- Available for **Windows** and **macOS** only (no Linux version)
- **Free tier** includes full MCP support and Claude Sonnet 4 access with limits, older Claude models
(Claude Opus 4 only in Pro)


**🔧 Claude Desktop Configuration by Installation Method:**

The Claude Desktop configuration differs based on how you installed the MCP server:

**1. UVX (Recommended - Modern tool runner):**
```json
{
  "command": "uvx",
  "args": ["python-alfresco-mcp-server", "--transport", "stdio"]
}
```
- **Sample Config Files** (in [`claude-desktop-configs/`](./claude-desktop-configs/)):
  - Windows: [`claude-desktop-config-uvx-windows.json`](./claude-desktop-configs/claude-desktop-config-uvx-windows.json)
  - macOS: [`claude-desktop-config-uvx-macos.json`](./claude-desktop-configs/claude-desktop-config-uvx-macos.json)
- UVX automatically handles isolation and global availability
- Fastest and most modern approach

**2. UV (Development or source installations):**
```json
{
  "command": "uv",
  "args": ["run", "python-alfresco-mcp-server", "--transport", "stdio"],
  "cwd": "C:\\path\\to\\python-alfresco-mcp-server"
}
```
- **Sample Config Files** (in [`claude-desktop-configs/`](./claude-desktop-configs/)):
  - Windows: [`claude-desktop-config-uv-windows.json`](./claude-desktop-configs/claude-desktop-config-uv-windows.json)
  - macOS: [`claude-desktop-config-uv-macos.json`](./claude-desktop-configs/claude-desktop-config-uv-macos.json)
- Uses `uv run` with `cwd` pointing to your **project directory**
- UV automatically finds and uses the `.venv` from the project directory
- Works for both source installations and after `uv tool install`

**3. Traditional Methods (pipx/pip):**

For traditional installation methods, see the **[Installation with pip and pipx](./docs/install_with_pip_pipx.md)** which covers:
- **pipx**: [`claude-desktop-config-pipx-windows.json`](./claude-desktop-configs/claude-desktop-config-pipx-windows.json) / [`claude-desktop-config-pipx-macos.json`](./claude-desktop-configs/claude-desktop-config-pipx-macos.json)
- **pip**: Manual venv path configuration

**🔐 Tool-by-Tool Permission System:**
Claude Desktop will prompt you **individually for each tool** on first use. Since this MCP server has 15 tools, you may see up to 15 permission prompts if you use all features. For each tool, you can choose:
- **"Allow once"** - Approve this single tool use only
- **"Always allow"** - Approve all future uses of this specific tool automatically (recommended for regular use)

This tool-by-tool security feature ensures you maintain granular control over which external tools can be executed.

> **🛡️ Virus Scanner Note**: If you have virus checkers like Norton 360, don't worry if you get a "checking" message once for pip, pipx, uv, uvx, or python-alfresco-mcp-server.exe - this is normal security scanning behavior.

**Using the Tools:**

- **Chat naturally** about what you want to do with documents and search
- **Mention "Alfresco"** to ensure the MCP server is used (e.g., "In Alfresco...")
- **Use tool-related keywords** - mention something close to the tool name 
- **Follow-up prompts** will know the document from previous context

**Example 1: Document Management**

1. Upload a simple text document: "Please create a file called 'claude_test_doc-25 07 25 101 0 AM.txt' in the repository shared folder with this content: 'This is a test document created by Claude via MCP.' description 'Test document uploaded via Claude MCP'"
2. Update properties: "Set the description property of this document to 'my desc'"
3. Check out the document
4. Cancel checkout
5. Check out again  
6. Check in as a major version
7. Download the document
8. Upload a second document from "C:\1 sample files\cmispress.pdf"

> **Note**: Claude will figure out to use base64 encoding for the first upload on a second try

**Example 2: Search Operations**

"With Alfresco please test all 3 search methods and CMIS query:"
- Basic search for "txt" documents, return max 10
- Advanced search for documents created after 2024-01-01, return max 25
- Metadata search for documents where cm:title contains "test", limit to 50  
- CMIS search to find all txt documents, limit to 50

**More Examples: Create Folder, Browse Folders, Get Repository Info**

- "Create a folder called '25 07 25 01 18 am' in shared folder"
- "List docs and folders in shared folder" *(will use -shared-)*
- "Can you show me what's in my Alfresco home directory?" *(will use browse_repository -my-)*
- "Get info on Alfresco" *(will use repository_info tool)*

**Chat Box Buttons**

- Use **Search and tools button** (two horizontal lines with circles icon) in the chat box and choose "python-alfresco-mcp-server" - this allows you to enable/disable all tools or individual tools

- Click the **+ Button** → "Add from alfresco" for quick access to resources and prompts

**Search and Analyze Prompt:**
- Provides a form with query field for full-text search
- Analysis types: **summary**, **detailed**, **trends**, or **compliance**
- **Generates template text** to copy/paste into chat for editing

**Repository Info Resource (and Tool):**
- Provides status information in text format for viewing or copying

**Examples:**
- See [`prompts-for-claude.md`](./prompts-for-claude.md) for examples testing the tools


#### 🔍 **MCP Inspector** (Development/Testing)

> 📖 **Setup Guide**: Complete MCP Inspector setup and connection instructions in [MCP Inspector Setup Guide](./docs/mcp_inspector_setup.md)

**📥 Install MCP Inspector:**
- **Prerequisites**: Requires **Node.js 18+** - Download from **[nodejs.org](https://nodejs.org/)**
- **Install Command**: `npm install -g @modelcontextprotocol/inspector`
- **Or run directly**: `npx @modelcontextprotocol/inspector` (no global install needed)
- **Purpose**: Web-based tool for testing MCP servers and individual tools with custom parameters

**Working Method (Recommended):**

**1. Start MCP Server with HTTP transport:**

   ```bash
   # With UVX (recommended)
   uvx python-alfresco-mcp-server --transport http --port 8003

   # With UV (development)
   uv run python-alfresco-mcp-server --transport http --port 8003

   # Traditional methods - see Traditional Installation Guide
   ```

**2. Start MCP Inspector with config:**

   **UVX Installation (Recommended)** — configs in [`mcp-inspector-configs/`](./mcp-inspector-configs/):
   ```bash
   # Start with stdio transport
   npx @modelcontextprotocol/inspector --config mcp-inspector-configs/mcp-inspector-stdio-uvx-config.json --server python-alfresco-mcp-server

   # Start with http transport  
   npx @modelcontextprotocol/inspector --config mcp-inspector-configs/mcp-inspector-http-uvx-config.json --server python-alfresco-mcp-server
   ```

   **UV Installation (Development):**
   ```bash
   # From project directory
   npx @modelcontextprotocol/inspector --config mcp-inspector-configs/mcp-inspector-stdio-uv-config.json --server python-alfresco-mcp-server  # stdio transport
   npx @modelcontextprotocol/inspector --config mcp-inspector-configs/mcp-inspector-http-uv-config.json --server python-alfresco-mcp-server   # http transport
   ```

   **Traditional Methods (pipx/pip):**

   See the **[Installation with pip and pipx](./docs/install_with_pip_pipx.md)** for pipx and pip configuration options.

**3. Open browser with pre-filled token:**

   - Use the URL provided in the output (includes authentication token)
   - Example: `http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=<token>`
   - This step applies to **all installation methods** (uv, uvx, pip, pipx)

This approach avoids proxy connection errors and provides direct authentication.


#### 🔧 **Other MCP Clients**

For Cursor, Claude Code, and other MCP clients:

📖 **Complete Setup Guide**: **[Client Configuration Guide](./docs/client_configurations.md)**


## 🛠️ Available Tools (15 Total)

### 🔍 Search Tools (4)
| Tool | Description | Parameters |
|------|-------------|------------|
| `search_content` | Search documents and folders | `query` (str), `max_results` (int), `node_type` (str) |
| `advanced_search` | Advanced search with filters | `query` (str), `content_type` (str), `created_after` (str), etc. |
| `search_by_metadata` | Search by metadata properties | `property_name` (str), `property_value` (str), `comparison` (str) |
| `cmis_search` | CMIS SQL queries | `cmis_query` (str), `preset` (str), `max_results` (int) |

### 🛠️ Core Tools (11)
| Tool | Description | Parameters |
|------|-------------|------------|
| `browse_repository` | Browse repository folders | `node_id` (str) |
| `repository_info` | Get repository information | None |
| `upload_document` | Upload new document | `filename` (str), `content_base64` (str), `parent_id` (str), `description` (str) |
| `download_document` | Download document content | `node_id` (str), `save_to_disk` (bool), `attachment` (bool), `destination_dir` (str, optional) |
| `create_folder` | Create new folder | `folder_name` (str), `parent_id` (str), `description` (str) |
| `get_node_properties` | Get node metadata | `node_id` (str) |
| `update_node_properties` | Update node metadata | `node_id` (str), `name` (str), `title` (str), `description` (str), `author` (str) |
| `delete_node` | Delete document/folder | `node_id` (str), `permanent` (bool) |
| `checkout_document` | Check out for editing | `node_id` (str), `download_for_editing` (bool) |
| `checkin_document` | Check in after editing | `node_id` (str), `comment` (str), `major_version` (bool), `file_path` (str) |
| `cancel_checkout` | Cancel checkout/unlock | `node_id` (str) |

📖 **See [API Reference](./docs/api_reference.md) for detailed tool documentation**

## 📊 Available Resources

### Repository Information
| Resource | Description | Access Method |
|----------|-------------|---------------|
| `repository_info` | Get comprehensive repository information including version, edition, license details, installed modules, and system status | Available as both MCP resource and tool |

The `repository_info` resource provides:
- **Repository Details**: ID, edition (Community/Enterprise), version information
- **License Information**: Issued/expires dates, remaining days, license holder, entitlements
- **System Status**: Read-only mode, audit enabled, quick share, thumbnail generation
- **Installed Modules**: Up to 10 modules with ID, title, version, and installation state

📖 **See [API Reference](./docs/api_reference.md) for detailed resource documentation**

## 🎯 Available Prompts

### Search and Analyze Prompt
| Prompt | Description | Parameters |
|--------|-------------|------------|
| `search_and_analyze` | Interactive form for guided content search and analysis | `query` (search terms), `analysis_type` (summary/detailed/trends/compliance) |

The Search and Analyze Prompt provides:
- **Interactive Form**: User-friendly interface with query input field
- **Analysis Options**: Choose from summary, detailed analysis, trends, or compliance reporting
- **Template Generation**: Creates copyable template text for chat conversations
- **Query Assistance**: Helps users structure effective search queries
- **Multiple Search Types**: Integrates with all 4 search tools (content, advanced, metadata, CMIS)

📖 **See [API Reference](./docs/api_reference.md) for detailed prompt documentation**

## 🔐 Authentication

Set `ALFRESCO_AUTH_METHOD` to one of **`basic`** (default), **`ticket`**, or **`oauth2`**. All three
are handled by the [`python-alfresco-api`](https://github.com/stevereiner/python-alfresco-api) auth
utilities and passed to `ClientFactory`.

**Basic** — HTTP Basic with username/password (simplest; fine for local/testing over HTTPS):
```env
ALFRESCO_AUTH_METHOD=basic
ALFRESCO_USERNAME=admin
ALFRESCO_PASSWORD=admin
```

**Ticket** — logs in once to `/authentication/versions/1/tickets`, then sends the ticket as
`Authorization: Basic base64(<ticket>)` so the password isn't transmitted on every request (the
ticket can expire/be revoked):
```env
ALFRESCO_AUTH_METHOD=ticket
ALFRESCO_USERNAME=admin
ALFRESCO_PASSWORD=admin
```

**OAuth2 (Bearer / OIDC)** — presents a Bearer token to Alfresco's REST API. **Requires Alfresco's
built-in `identity-service` subsystem configured against an OIDC IdP (e.g. Keycloak / Alfresco
Identity Service).** Alfresco Community 23.2+ ships this subsystem — it's config-only in
`alfresco-global.properties` (no Acosix/AMP needed). Two modes:

*client_credentials* (service account — the MCP server fetches + refreshes the token):
```env
ALFRESCO_AUTH_METHOD=oauth2
ALFRESCO_OAUTH2_CLIENT_ID=<client-id>
ALFRESCO_OAUTH2_CLIENT_SECRET=<client-secret>
ALFRESCO_OAUTH2_TOKEN_ENDPOINT=https://<keycloak>/realms/<realm>/protocol/openid-connect/token
ALFRESCO_OAUTH2_GRANT_TYPE=client_credentials
```

*pre-obtained token* (e.g. a specific user's token — content access follows that user's ACLs):
```env
ALFRESCO_AUTH_METHOD=oauth2
ALFRESCO_OAUTH2_CLIENT_ID=<client-id>
ALFRESCO_OAUTH2_ACCESS_TOKEN=<access-token>
ALFRESCO_OAUTH2_REFRESH_TOKEN=<refresh-token>   # optional; enables auto-refresh
```

> ⚠️ **Prefer a user token for content operations.** `client_credentials` authenticates as the
> Keycloak *service account* (e.g. `service-account-<client-id>`) — a JIT Alfresco user with **no
> display name** and only default ACLs. Alfresco then returns `createdByUser`/`modifiedByUser`
> without the (spec-required) `displayName`, which can break clients that parse node responses. For
> real content work, use the **pre-obtained token** mode above with a *user's* token — obtain one
> with a password grant and paste it into `ALFRESCO_OAUTH2_ACCESS_TOKEN`/`ALFRESCO_OAUTH2_REFRESH_TOKEN`:
> ```bash
> curl -X POST <token-endpoint> \
>   -d grant_type=password -d client_id=<id> -d client_secret=<secret> \
>   -d username=admin -d password=admin
> ```
> That way responses carry the real display name and the user's actual permissions. (As of
> python-alfresco-api ≥ 1.2.x the client also defaults a missing `displayName` to the user id, so the
> service-account path no longer crashes — but a user token still gives correct names and ACLs.)

> Note: this is **data-source** auth (how the MCP server authenticates *to Alfresco*), separate from
> securing the MCP transport itself. On the Alfresco side, configure `identity-service` (see the
> Alfresco docs for `identity-service.auth-server-url` / `.realm` / `.resource` / `.credentials.secret`);
> `client_credentials` authenticates as the service account, while a user's token scopes to that user.

### Securing the MCP transport (OAuth2 bearer)

Separately from data-source auth, you can require **callers of the MCP server** to present an OAuth2
bearer token. This uses FastMCP's JWT verifier and applies to the **HTTP/SSE** transports only
(stdio ignores it). Set `MCP_TRANSPORT_AUTH=true`; RS256 tokens are validated against your OIDC IdP's
JWKS, so only genuine IdP-signed tokens are accepted:

```env
MCP_TRANSPORT_AUTH=true
MCP_AUTH_JWKS_URI=http://host.docker.internal:8091/realms/alfresco/protocol/openid-connect/certs
# MCP_AUTH_ISSUER=https://<your-idp>/realms/<realm>   # optional; the MCP SDK requires HTTPS here
# MCP_AUTH_AUDIENCE=<aud>                              # optional
```

Run it and the endpoint rejects unauthenticated calls:

```bash
MCP_TRANSPORT_AUTH=true python -m alfresco_mcp_server.fastmcp_server --transport http --port 8009
# no token           -> 401
# Authorization: Bearer <valid-keycloak-token>  -> 200
```

**MCP Inspector:** run the HTTP inspector config, set the server URL to `http://localhost:8009/mcp/`,
and add an `Authorization: Bearer <token>` header (obtain the token out-of-band from your IdP — e.g.
`curl -X POST .../token -d grant_type=client_credentials -d client_id=... -d client_secret=...`).
Clients must acquire the token themselves; FastMCP validates it but does not issue tokens.

> The MCP SDK requires the issuer URL to be **HTTPS** (localhost excepted). With a local http Keycloak,
> leave `MCP_AUTH_ISSUER` unset — the JWKS signature check still gates access; add a strict issuer in
> production behind HTTPS.

## 🔧 Configuration Options

| Environment Variable | Default | Description |
|---------------------|---------|-------------|
| `ALFRESCO_URL` | `http://localhost:8080` | Alfresco server URL |
| `ALFRESCO_AUTH_METHOD` | `basic` | Auth method: `basic` \| `ticket` \| `oauth2` (see [Authentication](#-authentication)) |
| `ALFRESCO_USERNAME` | `admin` | Username (basic/ticket) |
| `ALFRESCO_PASSWORD` | `admin` | Password (basic/ticket) |
| `ALFRESCO_OAUTH2_CLIENT_ID` | – | OAuth2 client id (oauth2) |
| `ALFRESCO_OAUTH2_CLIENT_SECRET` | – | OAuth2 client secret (oauth2) |
| `ALFRESCO_OAUTH2_TOKEN_ENDPOINT` | – | OAuth2 token endpoint (oauth2) |
| `ALFRESCO_OAUTH2_GRANT_TYPE` | `client_credentials` | `client_credentials` \| `refresh_token` |
| `ALFRESCO_OAUTH2_ACCESS_TOKEN` | – | Pre-obtained access token (optional, oauth2) |
| `ALFRESCO_OAUTH2_REFRESH_TOKEN` | – | Refresh token (optional, oauth2) |
| `ALFRESCO_VERIFY_SSL` | `false` | Verify SSL certificates |
| `ALFRESCO_TIMEOUT` | `30` | Request timeout (seconds) |
| `FASTAPI_HOST` | `localhost` | FastAPI host |
| `FASTAPI_PORT` | `8000` | FastAPI port |
| `MCP_TRANSPORT_AUTH` | `false` | Require OAuth2 bearer to call the MCP server (HTTP/SSE only) — see [Securing the MCP transport](#securing-the-mcp-transport-oauth2-bearer) |
| `MCP_AUTH_JWKS_URI` | Keycloak certs | IdP JWKS endpoint used to validate bearer tokens |
| `MCP_AUTH_ISSUER` | – | Optional strict issuer check (must be HTTPS) |
| `MCP_AUTH_AUDIENCE` | – | Optional audience check |
| `LOG_LEVEL` | `INFO` | Logging level |
| `MAX_FILE_SIZE` | `100000000` | Max upload size (bytes) |

⚙️ **See [Configuration Guide](./docs/configuration_guide.md) for deployment options**

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                   MCP Clients                       │
│  Claude Desktop │ MCP Inspector │ Cursor │ Claude   │
│     Code │ n8n │ LangFlow │ Custom MCP Client App   │
└─────────────────┬───────────────────────────────────┘
                  │ stdio/HTTP/SSE
┌─────────────────▼───────────────────────────────────┐
│             FastMCP 2.0 MCP Server                  │
│  ┌─────────────┬─────────────┬─────────────────┐    │
│  │ MCP Tools   │ MCP         │ HTTP/SSE API    │    │
│  │ (15 total)  │ Resources   │                 │    │
│  │             │ MCP Prompts │                 │    │
│  └─────────────┴─────────────┴─────────────────┘    │
└─────────────────┬───────────────────────────────────┘
                  │ python-alfresco-api
┌─────────────────▼───────────────────────────────────┐
│            Alfresco Content Services                │
│         (Community/Enterprise Edition)              │
└─────────────────────────────────────────────────────┘
```

## 🧪 Testing & Quality

### Test Suite Overview
- **143 Total Tests**: **100% passed** - Coverage of all functionality
- **122 Unit Tests**: **100% passed** - Core functionality validated with mocking (FastMCP 2.0, tools, coverage)
- **21 Integration Tests**: **100% passed** - Live server testing (search, upload, download, document lifecycle)
- **Integration Tests**: Automated end-to-end testing covering all core document lifecycle scenarios
- **Performance Validated**: Search <1s, concurrent operations, resource access

### Coverage Report (Post-Cleanup)
- **Overall Coverage**: 51% (1,829 statements tested)
- **FastMCP 2.0 Core**: Well tested with comprehensive unit coverage
- **Configuration Module**: 93% coverage - Fully tested
- **Package Initialization**: 100% coverage (5/5 lines) - Complete
- **Overall Project**: 51% coverage of comprehensive codebase

### Run Tests

```bash
# Run full test suite
pytest

# Run with coverage report
pytest --cov=alfresco_mcp_server --cov-report=term-missing

# Run specific test categories
pytest -m "unit"           # Unit tests only
pytest -m "fastmcp"        # FastMCP 2.0 tests
pytest -m "integration"    # Integration tests (requires Alfresco)
```

🧪 **See [Testing Guide](./docs/testing_guide.md) for detailed testing strategies**

### 🧪 Test Categories and Execution

The project includes **4 levels of testing**:

1. **📋 Unit Tests** (122 tests) - Fast, mocked, isolated component testing
2. **🔗 Integration Tests** (21 tests) - Live Alfresco server testing  
3. **📝 Comprehensive Tests** - Automated core document lifecycle scenarios
4. **📊 Coverage Tests** - Edge cases and error path coverage



## 🧪 Development

### Setup Development Environment

```bash
git clone <repository>
cd python-alfresco-mcp-server

# UV handles everything automatically - no manual venv setup needed!
uv sync --extra dev        # Install with development tools
uv sync --extra test       # With testing tools
uv sync --extra all        # Everything

# Run immediately to test that installation worked
uv run python-alfresco-mcp-server --help

# Install python-alfresco-api for local development (if needed)
uv add --editable ../python-alfresco-api
```

**Traditional Development Setup:**

See the **[Installation with pip and pipx](./docs/install_with_pip_pipx.md)** for pip-based development setup.

## 💡 Examples

### Real-world implementation patterns from beginner to enterprise:

- **[💡 Examples Library](./examples/README.md)** - Complete navigation and learning paths
- **[🏃 Quick Start](./examples/quick_start.py)** - 5-minute introduction and basic operations
- **[📋 Document Lifecycle](./examples/document_lifecycle.py)** - Complete process demonstration
- **[🚀 Transport Examples](./examples/transport_examples.py)** - STDIO, HTTP, and SSE protocols
- **[⚡ Batch Operations](./examples/batch_operations.py)** - High-performance bulk processing
- **[🛡️ Error Handling](./examples/error_handling.py)** - Resilience patterns
- **[📊 Examples Summary](./examples/examples_summary.md)** - Overview and statistics

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Projects and References

- **[Hyland Alfresco](https://www.hyland.com/en/solutions/products/alfresco-platform)** - Content management platform (Enterprise and Community editions)
- **[python-alfresco-api](https://github.com/stevereiner/python-alfresco-api)** - The underlying Alfresco API library
- **[FastMCP 3](https://github.com/PrefectHQ/fastmcp)** - Modern framework for building MCP servers
- **[FastMCP Documentation](https://gofastmcp.com/)** - Complete FastMCP framework documentation and guides
- **[Model Context Protocol](https://modelcontextprotocol.io)** - Official MCP specification and documentation
- **[Playbooks.com MCP List](https://playbooks.com/mcp/stevereiner-alfresco-content-services)** - Python Alfresco MCP Server listing
- **[PulseMCP.com MCP List](https://www.pulsemcp.com/servers/stevereiner-alfresco-content-services)** - Python Alfresco MCP Server listing
- **[Glama.ai MCP List](https://glama.ai/mcp/servers?query=alfresco)** - Glama Alfresco list including Python Alfresco MCP Server listing
- **[MCPMarket.com MCP List](https://mcpmarket.com/server/alfresco)** - Python Alfresco MCP Server listing

## 🙋‍♂️ Support

- 📚 **Documentation**: Complete guides in [`./docs/`](./docs/README.md)
- 💡 **Examples**: Implementation patterns in [`./examples/`](./examples/README.md)
- 🧪 **Testing**: Quality assurance in [`./docs/testing_guide.md`](./docs/testing_guide.md)
- 🔍 **MCP Inspector**: Development testing in [`./docs/mcp_inspector_setup.md`](./docs/mcp_inspector_setup.md)
- 🛠️ **Troubleshooting**: Problem solving in [`./docs/troubleshooting.md`](./docs/troubleshooting.md)
- 🐛 **Issues**: [GitHub Issues](https://github.com/stevereiner/python-alfresco-mcp-server/issues)

---

**🚀 MCP server built with [python-alfresco-api](https://github.com/stevereiner/python-alfresco-api) and [FastMCP 2.0](https://github.com/paulinephelan/FastMCP)**
