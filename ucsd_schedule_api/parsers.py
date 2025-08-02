"""
HTML parsers for UCSD schedule data.
"""

from bs4 import BeautifulSoup
from typing import Dict, List, Tuple


class UCSDParsers:
    """Static methods for parsing HTML content from UCSD schedule system."""
    
    @staticmethod
    def parse_terms(html_content: str) -> Dict[str, str]:
        """
        Parse available terms from the menu page.
        
        Args:
            html_content: Raw HTML from the menu page
            
        Returns:
            Dictionary mapping term codes to term names
        """
        soup = BeautifulSoup(html_content, "lxml")
        terms = {}
        
        term_select = soup.find(id="selectedTerm")
        if not term_select:
            raise Exception("Could not find terms dropdown in HTML")
            
        for option in term_select.find_all("option"):
            term_code = option.get("value")
            term_name = option.text
            if term_code and term_name:
                terms[term_code.strip()] = term_name.strip()
                
        return terms
    
    @staticmethod
    def parse_form_inputs(html_content: str) -> List[Tuple[str, str]]:
        """
        Parse form inputs from the schedule search form.
        
        Args:
            html_content: Raw HTML from the menu page
            
        Returns:
            List of (name, value) tuples for form inputs
        """
        soup = BeautifulSoup(html_content, "lxml")
        form_inputs = []
        
        form = soup.find("form", id="socFacSearch")
        if not form:
            raise Exception("Could not find schedule search form")
            
        tabs_sub = form.find(id="tabs-sub")
        if not tabs_sub:
            raise Exception("Could not find form inputs section")
            
        for input_elem in tabs_sub.find_all("input"):
            name = input_elem.get("name")
            value = input_elem.get("value")
            if name is not None and value is not None:
                form_inputs.append((name, value))
                
        return form_inputs
    
    @staticmethod
    def parse_schedule_data(html_content: str) -> Dict:
        """
        Parse schedule data from results page.
        
        Args:
            html_content: Raw HTML from the schedule results page
            
        Returns:
            Parsed schedule data (structure TBD based on future needs)
        """
        # Placeholder for future schedule parsing
        # This is where you'd extract course information, times, etc.
        soup = BeautifulSoup(html_content, "lxml")
        
        # For now, just return basic info
        return {
            "raw_html": html_content,
            "parsed": False,
            "note": "Schedule parsing not yet implemented"
        }