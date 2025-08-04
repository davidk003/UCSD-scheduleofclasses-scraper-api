"""
Test scraping using the UCSD Schedule API.
"""

import pprint
from ucsd_schedule_api.core import UCSDClassScheduleAPI
import pytest
from pytest_mock import mocker
import json


@pytest.fixture(autouse=True)
def mock_menu_page(mocker):
    """Mock menu page fetching for all tests."""
    with open("tests/data/menu_page.html", "r") as f:
        mock_html = f.read()
    
    mock_fetch_menu_page = mocker.patch(
        "ucsd_schedule_api.fetcher.UCSDFetcher.fetch_menu_page"
    )
    mock_fetch_menu_page.return_value = mock_html
    return mock_fetch_menu_page


@pytest.fixture(autouse=True) 
def mock_departments_json(mocker):
    """Mock departments JSON fetching for all tests."""
    with open("tests/data/departments.json", "r") as f:
        mock_json = json.load(f)
    
    mock_fetch_departments_json = mocker.patch(
        "ucsd_schedule_api.fetcher.UCSDFetcher.fetch_departments_json"
    )
    mock_fetch_departments_json.return_value = mock_json
    return mock_fetch_departments_json

@pytest.fixture(autouse=True)
def mock_subjects_json(mocker):
    """Mock subjects JSON fetching for all tests."""
    with open("tests/data/subjects.json", "r") as f:
        mock_json = json.load(f)
    
    mock_fetch_subjects_json = mocker.patch(
        "ucsd_schedule_api.fetcher.UCSDFetcher.fetch_subjects_json"
    )
    mock_fetch_subjects_json.return_value = mock_json
    return mock_fetch_subjects_json


def test_get_departments():
    api = UCSDClassScheduleAPI()
    result = api.get_departments("FA25")
    assert len(result) > 0
    result_codes = list(result)
    expected_codes = ["CSE", "ECE", "MATH", "PHYS", "CHEM", "BIOL", "PSYC", "AIP"]
    for code in expected_codes:
        assert code in result_codes


def test_get_terms():
    api = UCSDClassScheduleAPI()
    result = api.get_terms()
    result_codes = list(result.keys())
    expected_codes = [
        "FA25",
        "SA25",
        "SU25",
        "S325",
        "S225",
        "S125",
        "SP25",
        "WI25",
        "FA24",
        "SA24",
        "SU24",
        "S324",
        "S224",
        "S124",
        "SP24",
        "WI24",
        "FA23",
        "SA23",
        "SU23",
        "S323",
    ]
    assert set(result_codes) == set(expected_codes)


def test_get_subjects(mocker):
    api = UCSDClassScheduleAPI()
    result = api.get_subjects("FA25")
    expected_codes = [{"code": "CSE", "value": "Computer Science & Engineering"}]
    for code in expected_codes:
        assert code in result
