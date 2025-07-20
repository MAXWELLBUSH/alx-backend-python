#!/usr/bin/env python3
"""Client module: Interacts with GitHub API"""

from typing import List, Dict
from utils import get_json, memoize


class GithubOrgClient:
    """GitHub Organization client class"""

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str):
        """Initialize client with organization name"""
        self.org_name = org_name

    @memoize
    def org(self) -> Dict:
        """Return the organization details"""
        return get_json(self.ORG_URL.format(org=self.org_name))

    @property
    def _public_repos_url(self) -> str:
        """Get the URL for public repositories"""
        return self.org["repos_url"]

    def public_repos(self, license: str = None) -> List[str]:
        """List public repositories, optionally filter by license"""
        repos = get_json(self._public_repos_url)
        if license is None:
            return [repo["name"] for repo in repos]

        return [
            repo["name"]
            for repo in repos
            if self.has_license(repo, license)
        ]

    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -> bool:
        """Check if a repo has a specific license"""
        return repo.get("license", {}).get("key") == license_key
