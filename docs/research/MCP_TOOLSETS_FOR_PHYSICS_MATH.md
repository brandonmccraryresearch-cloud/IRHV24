# MCP Toolsets for Physics and Mathematics Research

A curated list of Model Context Protocol (MCP) toolsets ranked by usefulness for theoretical physics and mathematical research.

## Ranking Criteria

1. **Relevance** - Direct applicability to physics/math computations
2. **Capability** - Breadth and depth of available tools
3. **Maturity** - Stability, documentation, and community support
4. **Integration** - Ease of integration with AI agents and workflows

---

## Tier 1: Highly Recommended

### 1. ToolUniverse (Harvard MIMS Lab)
**Repository:** [mims-harvard/ToolUniverse](https://github.com/mims-harvard/ToolUniverse)

**Relevance:** ⭐⭐⭐⭐⭐ | **Capability:** ⭐⭐⭐⭐⭐ | **Maturity:** ⭐⭐⭐⭐⭐

- **700+ Scientific Tools** for AI scientists
- Symbolic mathematics (SymPy integration)
- Numerical analysis (NumPy/SciPy)
- Scientific visualization
- Literature search and knowledge retrieval
- Full MCP protocol support with multiple transports (HTTP, STDIO, SSE)
- Active development and documentation

**Best For:** Comprehensive scientific computing, symbolic math, data analysis, visualization

---

### 2. Wolfram MCP Server
**Repository:** [modelcontextprotocol/servers - Wolfram](https://github.com/modelcontextprotocol/servers/tree/main/src/wolfram)

**Relevance:** ⭐⭐⭐⭐⭐ | **Capability:** ⭐⭐⭐⭐⭐ | **Maturity:** ⭐⭐⭐⭐

- Access to Wolfram|Alpha computational knowledge engine
- Wolfram Language for symbolic computation
- Mathematical problem solving
- Unit conversions and physical constants
- Equation solving and calculus
- Requires Wolfram API key

**Best For:** Symbolic mathematics, equation solving, physical constants lookup

---

### 3. SciPy/NumPy MCP Servers (Community)
**Various implementations available**

**Relevance:** ⭐⭐⭐⭐⭐ | **Capability:** ⭐⭐⭐⭐ | **Maturity:** ⭐⭐⭐

- Direct NumPy/SciPy function access
- Linear algebra operations
- Numerical integration and differentiation
- Statistical functions
- Optimization algorithms

**Best For:** Numerical computations, linear algebra, statistics

---

## Tier 2: Strongly Recommended

### 4. GitHub MCP Server (Official)
**Repository:** [modelcontextprotocol/servers - GitHub](https://github.com/modelcontextprotocol/servers)

**Relevance:** ⭐⭐⭐⭐ | **Capability:** ⭐⭐⭐⭐ | **Maturity:** ⭐⭐⭐⭐⭐

- Repository management and code search
- Issue and PR management
- Workflow integration
- Version control operations
- Essential for collaborative research

**Best For:** Version control, code management, collaboration

---

### 5. Brave Search MCP Server
**Repository:** [modelcontextprotocol/servers - Brave](https://github.com/modelcontextprotocol/servers)

**Relevance:** ⭐⭐⭐⭐ | **Capability:** ⭐⭐⭐ | **Maturity:** ⭐⭐⭐⭐

- Web search for research papers and documentation
- arXiv and research paper discovery
- Technical documentation search
- Current physics/math news and developments

**Best For:** Literature discovery, research updates, documentation search

---

### 6. Filesystem MCP Server
**Repository:** [modelcontextprotocol/servers - Filesystem](https://github.com/modelcontextprotocol/servers)

**Relevance:** ⭐⭐⭐⭐ | **Capability:** ⭐⭐⭐ | **Maturity:** ⭐⭐⭐⭐⭐

- File and directory operations
- Data file reading/writing
- Computational output management
- Essential for any computational workflow

**Best For:** File management, data I/O, output handling

---

## Tier 3: Recommended

### 7. PostgreSQL/SQLite MCP Servers
**Repository:** [modelcontextprotocol/servers - Database](https://github.com/modelcontextprotocol/servers)

**Relevance:** ⭐⭐⭐ | **Capability:** ⭐⭐⭐⭐ | **Maturity:** ⭐⭐⭐⭐

- Store and query computational results
- Experimental data management
- Parameter sweeps and configurations
- Result archiving and retrieval

**Best For:** Data management, result storage, parameter tracking

---

### 8. Jupyter MCP Integration
**Various community implementations**

**Relevance:** ⭐⭐⭐⭐ | **Capability:** ⭐⭐⭐ | **Maturity:** ⭐⭐⭐

- Notebook execution
- Interactive computation
- Visualization within notebooks
- Research documentation

**Best For:** Interactive computation, visualization, documentation

---

### 9. LaTeX/Typst MCP Servers
**Community implementations**

**Relevance:** ⭐⭐⭐⭐ | **Capability:** ⭐⭐⭐ | **Maturity:** ⭐⭐

- Mathematical typesetting
- Paper and document generation
- Equation rendering
- Publication preparation

**Best For:** Documentation, paper writing, equation typesetting

---

## Tier 4: Specialized Use Cases

### 10. Docker MCP Server
**Repository:** [modelcontextprotocol/servers - Docker](https://github.com/modelcontextprotocol/servers)

**Relevance:** ⭐⭐⭐ | **Capability:** ⭐⭐⭐⭐ | **Maturity:** ⭐⭐⭐⭐

- Container management for isolated computations
- Reproducible computing environments
- Complex dependency management

**Best For:** Reproducibility, environment isolation

---

### 11. Memory/Context MCP Servers
**Various implementations**

**Relevance:** ⭐⭐⭐ | **Capability:** ⭐⭐⭐ | **Maturity:** ⭐⭐⭐

- Persistent context across sessions
- Research notes and findings storage
- Long-term memory for agents

**Best For:** Research continuity, knowledge retention

---

### 12. Playwright/Puppeteer MCP Servers
**Repository:** [modelcontextprotocol/servers - Playwright](https://github.com/modelcontextprotocol/servers)

**Relevance:** ⭐⭐ | **Capability:** ⭐⭐⭐⭐ | **Maturity:** ⭐⭐⭐⭐

- Web scraping for research data
- Documentation extraction
- Automated data collection

**Best For:** Data collection, web scraping

---

## Physics/Math Specialized (Emerging)

### 13. CODATA Constants Server
**Community/Custom implementations**

**Relevance:** ⭐⭐⭐⭐⭐ | **Capability:** ⭐⭐ | **Maturity:** ⭐⭐

- CODATA fundamental constants
- Physical constants with uncertainties
- Unit system conversions
- Essential for precision physics

**Best For:** Fundamental constants lookup, validation

---

### 14. arXiv MCP Server
**Community implementations**

**Relevance:** ⭐⭐⭐⭐⭐ | **Capability:** ⭐⭐⭐ | **Maturity:** ⭐⭐

- arXiv paper search and retrieval
- Physics preprint access
- Citation analysis
- Research discovery

**Best For:** Literature review, staying current with research

---

### 15. Sage/Mathematica MCP Bridges
**Custom implementations**

**Relevance:** ⭐⭐⭐⭐⭐ | **Capability:** ⭐⭐⭐⭐ | **Maturity:** ⭐

- Computer algebra system access
- Advanced symbolic computation
- Number theory and algebra
- Group theory calculations

**Best For:** Advanced symbolic computation, number theory

---

## Implementation Priority for IRH

### Immediate (Already Configured)
1. ✅ **ToolUniverse** - Primary scientific tools
2. ✅ **GitHub MCP Server** - Repository management

### Near-Term (Recommended)
3. **Wolfram MCP** - Symbolic math and constants
4. **Brave Search** - Research discovery
5. **Filesystem MCP** - Data management

### Future Consideration
6. **Custom CODATA Server** - Precision constant validation
7. **arXiv MCP** - Literature integration
8. **PostgreSQL** - Result archiving

---

## Summary Comparison Table

| Toolset | Physics | Math | Stability | Integration |
|---------|---------|------|-----------|-------------|
| ToolUniverse | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Wolfram | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| SciPy/NumPy | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| GitHub | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Brave Search | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Filesystem | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| PostgreSQL | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| LaTeX/Typst | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| CODATA | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐ |
| arXiv | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ |

---

## Resources

### Official MCP
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Official MCP Servers Repository](https://github.com/modelcontextprotocol/servers)

### Community Resources
- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers)
- [MCP.so - MCP Server Directory](https://mcp.so/)

### IRH-Specific
- [ToolUniverse Setup Guide](../guides/TOOLUNIVERSE_MCP_SETUP.md)
- [IRH Computational Research Plan](../implementation/GITHUB_ACTIONS_COMPUTATIONAL_RESEARCH_PLAN.md)

---

*Last Updated: January 2025*
*Compiled for IRH Computational Research*
