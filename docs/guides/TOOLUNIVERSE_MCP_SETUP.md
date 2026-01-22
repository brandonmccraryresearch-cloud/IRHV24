# ToolUniverse MCP Server Integration Guide

This guide explains how to integrate the ToolUniverse MCP (Model Context Protocol) server with the IRH repository's AI agents. ToolUniverse provides access to 700+ scientific tools for data analysis, knowledge retrieval, and computational workflows.

## Overview

ToolUniverse is a comprehensive ecosystem for AI scientist systems that standardizes how LLMs identify and call tools. It integrates:
- **700+ Machine Learning Models** for data analysis
- **Scientific APIs** (UniProt, ChEMBL, OpenTargets, FDA, etc.)
- **Mathematical and computational packages**
- **Knowledge retrieval systems**

## Quick Start

### 1. Install ToolUniverse

Add to your environment's pip dependencies:

```yaml
# In environment.yml:
dependencies:
  - pip:
      - tooluniverse>=1.0.15
```

Or install directly:

```bash
pip install tooluniverse
```

### 2. Start the MCP Server

**HTTP Server (recommended for remote access):**

```bash
tooluniverse-smcp --transport http --port 8000 --host 0.0.0.0
```

**STDIO Server (for local agent integration):**

```bash
tooluniverse-smcp-stdio
```

### 3. Configure Categories for Physics/Math Work

For physics and mathematics research, use these relevant categories:

```bash
tooluniverse-smcp-stdio \
  --categories calculation sympy symbolic \
  --include-tool-types "calculation,analysis,visualization"
```

## MCP Server Configuration Options

### Transport Options

| Transport | Use Case | Command |
|-----------|----------|---------|
| HTTP | Web apps, remote access | `tooluniverse-smcp --transport http` |
| STDIO | Local desktop apps | `tooluniverse-smcp-stdio` |
| SSE | Real-time streaming | `tooluniverse-smcp --transport sse` |

### Tool Selection

**By Category:**
```bash
--categories uniprot ChEMBL opentarget calculation
```

**By Tool Name (file-based):**
```bash
--tools-file physics_tools.txt
```

**By Tool Type:**
```bash
--include-tool-types "calculation,analysis,symbolic"
```

### Performance Tuning

```bash
--max-workers 4        # Parallel tool execution
--compact-mode         # Reduce context window usage
```

## Integration with GitHub Actions

Add to your workflow:

```yaml
- name: Start ToolUniverse MCP Server
  run: |
    pip install tooluniverse
    tooluniverse-smcp --transport http --port 8000 &
    echo "Waiting for ToolUniverse server..."
    # Wait up to 60 seconds for the server to become available.
    timeout 60s bash -c 'until curl -s --head --fail http://localhost:8000 >/dev/null 2>&1; do sleep 1; done'
    echo "Server is ready."
```

## Physics & Mathematics Relevant Tools

ToolUniverse includes these categories relevant to IRH research:

### Symbolic Mathematics
- SymPy integration for symbolic computation
- Equation solving and simplification
- Calculus operations

### Numerical Analysis
- NumPy/SciPy integrations
- Data analysis pipelines
- Statistical tools

### Scientific Data Access
- PDB (Protein Data Bank)
- RCSB molecular structure API
- UniProt protein database

### Visualization
- Matplotlib integrations
- 3D molecular visualization
- Plot generation tools

## Agent Integration

### Adding to an Agent Definition

In your `.github/agents/` directory, add the ToolUniverse MCP server to the tools list:

```yaml
tools:
  - bash
  - view
  - create
  - edit
  - tooluniverse-mcp-server  # Add this line
```

### Python API Usage

```python
from tooluniverse import ToolUniverse

# Initialize
tu = ToolUniverse()
tu.load_tools()

# Find relevant tools
tools = tu.run({
    "name": "Tool_Finder_Keyword",
    "arguments": {"description": "symbolic mathematics", "limit": 10}
})

# Execute a tool
result = tu.run({
    "name": "SymPy_solve_equation",
    "arguments": {"equation": "x**2 - 4", "variable": "x"}
})
```

## Security Considerations

1. **API Keys:** Some tools require API keys. Set them as environment variables.
2. **Network Access:** HTTP transport exposes server to network.
3. **Tool Execution:** Review tool permissions before production use.

## Troubleshooting

### Server Not Starting
```bash
# Check installation
pip show tooluniverse

# Verify port availability
lsof -i :8000
```

### Tools Not Loading
```bash
# Enable verbose logging
tooluniverse-smcp --verbose

# Check available categories
tooluniverse-doctor
```

### Performance Issues
- Reduce loaded categories with `--categories`
- Enable `--compact-mode` to reduce context window usage
- Increase `--max-workers` for parallel execution

## External Resources

- [ToolUniverse Documentation](https://zitniklab.hms.harvard.edu/ToolUniverse/)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)
- [ToolUniverse GitHub](https://github.com/mims-harvard/ToolUniverse)
- [Available Tools List](https://zitniklab.hms.harvard.edu/ToolUniverse/tools/tools_config_index.html)

## Related IRH Documentation

- [GEMINI_INTEGRATION.md](./GEMINI_INTEGRATION.md) - Gemini AI integration
- [QUICKSTART.md](./QUICKSTART.md) - Quick start guide
- [../implementation/](../implementation/) - Implementation details
