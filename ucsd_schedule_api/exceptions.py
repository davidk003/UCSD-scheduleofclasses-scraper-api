class UCSDScheduleAPIError(Exception):
    """Base exception for UCSD Schedule API errors"""

    pass

class NetworkError(UCSDScheduleAPIError):
    """Raised when network requests fail"""
    pass

class ParseError(UCSDScheduleAPIError):
    """Raised when HTML parsing fails"""
    pass

class InitializationError(UCSDScheduleAPIError):
    """Raised when the API fails to initialize"""

    def __init__(self, message: str = "Failed to initialize UCSD Schedule API"):
        super().__init__(message)


class InvalidTermError(UCSDScheduleAPIError):
    """Raised when an invalid term is provided"""

    def __init__(self, term: str, available_terms: list | None = None):
        self.term = term
        self.available_terms = available_terms

        if available_terms:
            message = f"Term '{term}' not found. Available terms: {available_terms}"
        else:
            message = f"Term '{term}' not found"

        super().__init__(message)
