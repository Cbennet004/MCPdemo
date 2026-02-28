# MCPdemo — Build 1 (MCP-Style Tool Call)

This repo is a beginner-friendly, Colab-first demo showing **MCP-style tool access**:
- A clean Python tool module calls an external API (Open-Meteo)
- A Colab notebook runs the tool
- Outputs are saved as JSON and CSV artifacts

## Structure
- `src/tools/open_meteo.py` — tool adapter (API call)
- `notebooks/` — Colab notebooks
- `outputs/` — generated artifacts (JSON/CSV)

## Run (Colab)
1. Open the notebook in `notebooks/`
2. Run cells top-to-bottom
3. Check `outputs/` for artifacts
