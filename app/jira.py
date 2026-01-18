import os
import requests
from dotenv import load_dotenv
from app.models import JiraTicket, JiraSubtask

load_dotenv()

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")


def get_jira_ticket(issue_key: str) -> JiraTicket:
    url = f"{JIRA_BASE_URL}/rest/api/3/issue/{issue_key}"

    response = requests.get(
        url,
        auth=(JIRA_EMAIL, JIRA_API_TOKEN),
        headers={"Accept": "application/json"},
    )
    response.raise_for_status()

    data = response.json()
    fields = data["fields"]

    subtasks = [
        JiraSubtask(
            key=s["key"],
            summary=s["fields"]["summary"],
            status=s["fields"]["status"]["name"],
        )
        for s in fields.get("subtasks", [])
    ]

    return JiraTicket(
        key=data["key"],
        summary=fields["summary"],
        description=fields.get("description", {}).get("content", None),
        status=fields["status"]["name"],
        assignee=(
            fields["assignee"]["displayName"]
            if fields.get("assignee")
            else None
        ),
        subtasks=subtasks,
    )
