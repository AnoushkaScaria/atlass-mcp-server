import os
import requests
from dotenv import load_dotenv

load_dotenv()

CONFLUENCE_BASE_URL = os.getenv("CONFLUENCE_BASE_URL")
CONFLUENCE_EMAIL = os.getenv("CONFLUENCE_EMAIL")
CONFLUENCE_API_TOKEN = os.getenv("CONFLUENCE_API_TOKEN")
CONFLUENCE_SPACE_KEY = os.getenv("CONFLUENCE_SPACE_KEY")


def create_confluence_page(title: str, content: str) -> dict:
    url = f"{CONFLUENCE_BASE_URL}/rest/api/content"

    payload = {
        "type": "page",
        "title": title,
        "space": {"key": CONFLUENCE_SPACE_KEY},
        "body": {
            "storage": {
                "value": content,
                "representation": "storage",
            }
        },
    }

    response = requests.post(
        url,
        json=payload,
        auth=(CONFLUENCE_EMAIL, CONFLUENCE_API_TOKEN),
        headers={"Content-Type": "application/json"},
    )
    response.raise_for_status()
    return response.json()
