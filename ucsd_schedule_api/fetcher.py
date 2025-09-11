"""
HTTP client for fetching data from UCSD schedule system.
"""

import requests
import urllib.parse
from typing import List, Tuple
from requests.models import *
from ucsd_schedule_api.exceptions import *

class UCSDFetcher:
    """HTTP client for interacting with UCSD's schedule of classes system.
    
    This class provides a unified interface for making HTTP requests to various
    UCSD schedule endpoints. It handles session management and provides methods
    for fetching schedule data, department lists, and subject information.
    
    Args:
        enable_session: If True, uses requests.Session for connection pooling.
                       If False, uses requests module directly. Defaults to True.
    
    Attributes:
        client: The HTTP client (Session or requests module) used for requests.
    
    Example:
        >>> fetcher = UCSDFetcher()
        >>> menu_html = fetcher.fetch_menu_page()
        >>> departments = fetcher.fetch_departments_json("FA25")
        >>> subjects = fetcher.fetch_subjects_json("FA25")
    """
    
    MENU_URL = "https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesStudent.htm"
    RESULTS_URL = "https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesStudentResult.htm"
    DEPARTMENTS_URL = "https://act.ucsd.edu/scheduleOfClasses/department-list.json?selectedTerm="
    SUBJECTS_URL = "https://act.ucsd.edu/scheduleOfClasses/subject-list.json?selectedTerm="
    
    def __init__(self, enable_session: bool = True):
        self.client = requests.Session() if enable_session else requests
    
    def fetch_menu_page(self) -> str:
        """Fetch the main schedule menu page HTML.
        
        Returns:
            Raw HTML content of the schedule menu page.
            
        Raises:
            NetworkError: If the HTTP request fails (connection issues, timeout,
                         SSL errors, etc.) or returns non-200 status code.
            requests.exceptions.JSONDecodeError: If the response contains invalid JSON data.
        """
        try:
            response = self.client.get(self.MENU_URL)
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Failed to fetch menu page: {e}")
        if response.status_code != 200:
            raise NetworkError(f"Failed to fetch menu page: {response.status_code}")
        return response.text
    
    def fetch_departments_json(self, term: str) -> List[dict[str, str]]:
        """Fetch the list of available departments for a given term.
        
        Args:
            term: The term code (e.g., "FA25" for Fall 2025).
            
        Returns:
            List of dictionaries containing department information.
            Each dictionary has 'code' and 'value' keys.
            
        Raises:
            NetworkError: If the HTTP request fails (connection issues, timeout,
                         SSL errors, etc.) or returns non-200 status code.
            requests.exceptions.JSONDecodeError: If the response contains invalid JSON data.

        """
        try:
            response: Response = self.client.get(f"{self.DEPARTMENTS_URL}{term}")
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Failed to get departments: {e}")
        if response.status_code != 200:
            raise NetworkError(f"Failed to get departments: {response.status_code}")
        return response.json()
    
    def fetch_subjects_json(self, term: str) -> List[dict[str, str]]:
        """Fetch the list of available subjects for a given term.
        
        Args:
            term: The term code (e.g., "FA25" for Fall 2025).
            
        Returns:
            List of dictionaries containing subject information.
            Each dictionary has 'code' and 'value' keys.
            
        Raises:
            NetworkError: If the HTTP request fails (connection issues, timeout,
                         SSL errors, etc.) or returns non-200 status code.
            requests.exceptions.JSONDecodeError: If the response contains invalid JSON data.

        """
        try:
            response = self.client.get(f"{self.SUBJECTS_URL}{term}")
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Failed to get subjects: {e}")
        if response.status_code != 200:
            raise NetworkError(f"Failed to get subjects: {response.status_code}")
        return response.json()
    
    def fetch_schedule_results(self, form_data: List[Tuple[str, str]]) -> str:
        """Fetch schedule results page by submitting search form data.
        
        Args:
            form_data: List of (name, value) tuples representing form fields
                      to submit to the schedule search endpoint.
                      
        Returns:
            Raw HTML content of the schedule results page.
            
        Raises:
            NetworkError: If the HTTP request fails (connection issues, timeout,
                         SSL errors, etc.) or returns non-200 status code.
            requests.exceptions.JSONDecodeError: If the response contains invalid JSON data.
        """
        try:
            response = self.client.post(
                self.RESULTS_URL,
                data=urllib.parse.urlencode(form_data),
                headers={'Content-Type': 'application/x-www-form-urlencoded'}
            )
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Failed to fetch schedule results: {e}")
        if response.status_code != 200:
            raise NetworkError(f"Failed to fetch schedule results: {response.status_code}")
        return response.text