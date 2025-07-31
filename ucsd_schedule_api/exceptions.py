class UCSDScheduleAPIError(Exception):
    """Base exception for UCSD Schedule API errors"""

    pass


class InvalidTermError(UCSDScheduleAPIError):
    """Raised when an invalid term is provided"""

    def __init__(self, term: str, available_terms: list = None):
        self.term = term
        self.available_terms = available_terms

        if available_terms:
            message = f"Term '{term}' not found. Available terms: {available_terms}"
        else:
            message = f"Term '{term}' not found"

        super().__init__(message)
