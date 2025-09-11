from .fetcher import UCSDFetcher
from .parsers import UCSDParsers
from .exceptions import *
from .models import *

class UCSDClassScheduleAPI:
    """Main API for accessing UCSD class schedule data."""
    
    def __init__(self, enable_session: bool = True, preload_terms: bool = True):
        self.fetcher = UCSDFetcher(enable_session)
        self.terms: dict[str, str] | None = None
        if preload_terms:
            self.load_terms()

    def load_terms(self) -> None:
        """Load available terms on initialization."""
        html = self.fetcher.fetch_menu_page()
        self.terms = UCSDParsers.parse_terms(html)

    def get_terms(self) -> dict[str, str]:
        """Get available terms."""
        if self.terms is None:
            raise InitializationError("Terms were not loaded during initialization")
        return self.terms

    def get_departments(self, term: str) -> dict[DeptCode, DeptName]:
        """Get departments for a specific term."""
        if self.terms is None or term not in self.terms:
            raise InvalidTermError(term)
        json_data: list[dict[DeptCode, DeptName]] = self.fetcher.fetch_departments_json(term)
        departments: dict[DeptCode, DeptName] = {}
        for data in json_data:
            departments[data["code"].strip()] = data["value"].strip()
        return departments
    
    def get_subjects(self, term: str) -> list[dict[str, str]]:
        """Get subjects for a specific term."""
        if self.terms is None or term not in self.terms:
            raise InvalidTermError(term)
        subjects: list[dict[str, str]] = self.fetcher.fetch_subjects_json(term)
        for subject in subjects:
            subject["code"] = subject["code"].strip()
            subject["value"] = subject["value"][subject["value"].find("-")+1:].strip()
        return subjects

    def _get_schedule_form_inputs(self) -> list[tuple[str, str]]:
        """Get form inputs needed for schedule search."""
        html = self.fetcher.fetch_menu_page()
        return UCSDParsers.parse_form_inputs(html)


    def get_schedule_page_by_term_subject(self, term: str, subjects: list[str]) -> str:
        """Get schedule page HTML for specific term and subjects."""
        if not self.terms or term not in self.terms:
            raise InvalidTermError(term)
            
        # Get form inputs and prepare payload
        form_inputs = self._get_schedule_form_inputs()
        payload = self._prepare_schedule_payload(form_inputs, term, subjects)
        # Fetch the schedule page
        html = self.fetcher.fetch_schedule_results(payload)

        return html
    
    def _prepare_schedule_payload(self, form_inputs: list[tuple[str, str]], 
                                term: str, subjects: list[str]) -> list[tuple[str, str]]:
        """Prepare form payload for schedule search."""
        # Remove existing term/subject fields to avoid duplicates
        fields_to_remove = ["selectedTerm", "_selectedSubjects", "selectedSubjects"]
        filtered_inputs = [
            (name, value) for name, value in form_inputs 
            if name not in fields_to_remove
        ]
        
        # Add our specific search parameters
        filtered_inputs.extend([
            ("selectedTerm", term),
            ("_selectedSubjects", str(len(subjects))),
            ("selectedSubjects", ",".join(subjects))
        ])
        
        return filtered_inputs
