"""
UCSD Schedule of Classes Scraper API
"""

__version__ = "0.1.0"
__author__ = "David Kim"
__email__ = "dck003@ucsd.edu"

from .core import UCSDClassScheduleAPI
from .exceptions import UCSDScheduleAPIError, InvalidTermError

__all__ = ["UCSDClassScheduleAPI", "UCSDScheduleAPIError", "InvalidTermError"]
