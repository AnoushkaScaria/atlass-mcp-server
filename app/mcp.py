from fastmcp import FastMCP
from app.jira import get_jira_ticket
from app.confluence import create_confluence_page

mcp = FastMCP("jira-confluence-mcp")


@mcp.tool()
def fetch_jira_ticket(issue_key: str) -> dict:
    """
    Fetch a Jira ticket and return structured details.
    """
    ticket = get_jira_ticket(issue_key)
    return ticket.dict()


@mcp.tool()
def generate_confluence_page_from_jira(issue_key: str) -> dict:
    """
    Create a Confluence page based on a Jira ticket.
    """
    ticket = get_jira_ticket(issue_key)

    content = f"""
    <h1>{ticket.summary}</h1>
    <p><strong>Status:</strong> {ticket.status}</p>
    <p><strong>Assignee:</strong> {ticket.assignee}</p>

    <h2>Subtasks</h2>
    <ul>
        {''.join(f"<li>{s.key}: {s.summary} ({s.status})</li>" for s in ticket.subtasks)}
    </ul>
    """

    return create_confluence_page(
        title=f"Jira Ticket {ticket.key}",
        content=content,
    )
