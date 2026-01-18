# MCP Jira–Confluence Server

A personal implementation of a Model Context Protocol (MCP) server that exposes
tools for interacting with Jira and Confluence.

## Features
- MCP tool discovery
- Fetch Jira ticket details
- Generate Confluence pages from Jira context
- FastAPI + FastMCP architecture

## Tools
- fetch_jira_ticket(issue_key)
- generate_confluence_page_from_jira(issue_key)

## Setup
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload

## Create a .env file
JIRA_BASE_URL=https://example.atlassian.net
JIRA_EMAIL=your_email@example.com
JIRA_API_TOKEN=your_jira_api_token

CONFLUENCE_BASE_URL=https://example.atlassian.net/wiki
CONFLUENCE_EMAIL=your_email@example.com
CONFLUENCE_API_TOKEN=your_confluence_api_token
CONFLUENCE_SPACE_KEY=SPACE
