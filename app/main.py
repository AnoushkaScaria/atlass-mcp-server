from fastapi import FastAPI
from app.mcp_tools import mcp

app = FastAPI(title="MCP Jira–Confluence Server")

# Mount MCP under /mcp
app.mount("/mcp", mcp.app)


@app.get("/")
def health_check():
    return {"status": "ok"}
