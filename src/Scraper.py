import re
from dataclasses import dataclass

import requests


@dataclass(frozen=True)
class GetResults:
    http_status: int
    html_content: str


class Scraper:
    def get(self, url: str) -> GetResults:
        """
        Get the HTML content from a URL.
        """
        try:
            response = requests.get(url)
            return GetResults(response.status_code, response.text)
        except Exception as e:
            return GetResults(0, str(e))

    def contains(self, html_content: str, pattern: str) -> bool:
        """
        Check if the HTML content contains a pattern.
        """
        return re.search(pattern, html_content, flags=re.IGNORECASE) is not None
