#!/usr/bin/env python3
""" Client class for Github organization """

from typing import Dict
import requests


class GithubOrgClient:
    """Client for GitHub orgs"""

    ORG_URL = "https://api.github.com/orgs/{}"

    def __init__(self, org_name: str) -> None:
        """Initialize client"""
        self.org_name = org_name

    def org(self) -> Dict:
        """Return org information"""
        url = self.ORG_URL.format(self.org_name)
        return requests.get(url).json()

# client.py
import requests

def fetch_greeting(name):
    response = requests.get(f"http://127.0.0.1:5000/api/greet?name={name}")
    return response.json()
