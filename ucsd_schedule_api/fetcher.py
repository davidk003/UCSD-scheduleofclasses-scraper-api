"""
HTTP client for fetching data from UCSD schedule system.
"""

import requests
import urllib.parse
from typing import List, Tuple


class UCSDFetcher:
    """Handles all HTTP requests to UCSD schedule system."""
    
    MENU_URL = "https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesStudent.htm"
    RESULTS_URL = "https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesStudentResult.htm"
    DEPARTMENTS_URL = "https://act.ucsd.edu/scheduleOfClasses/department-list.json?selectedTerm="
    SUBJECTS_URL = "https://act.ucsd.edu/scheduleOfClasses/subject-list.json?selectedTerm="
    
    def __init__(self, enable_session: bool = True):
        self.client = requests.Session() if enable_session else requests
    
    def fetch_menu_page(self) -> str:
        """Fetch the main schedule menu page."""
        response = self.client.get(self.MENU_URL)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch menu page: {response.status_code}")
        return response.text
    
    def fetch_departments_json(self, term: str) -> List[str]:
        """Fetch departments list as JSON."""
        response = self.client.get(f"{self.DEPARTMENTS_URL}{term}")
        if response.status_code != 200:
            raise Exception(f"Failed to get departments: {response.status_code}")
        return response.json()
    
    def fetch_subjects_json(self, term: str) -> List[str]:
        """Fetch subjects list as JSON."""
        response = self.client.get(f"{self.SUBJECTS_URL}{term}")
        if response.status_code != 200:
            raise Exception(f"Failed to get subjects: {response.status_code}")
        return response.json()
    
    def fetch_schedule_results(self, form_data: List[Tuple[str, str]]) -> str:
        """Fetch schedule results page using form data."""
        response = self.client.post(
            self.RESULTS_URL,
            data=urllib.parse.urlencode(form_data),
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        if response.status_code != 200:
            raise Exception(f"Failed to fetch schedule results: {response.status_code}")
        return response.text