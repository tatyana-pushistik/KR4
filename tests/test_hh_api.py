import pytest
from src.hh_api import HHApi

def test_get_vacancies():
    api = HHApi()
    vacancies = api.get_vacancies('keyword')
    assert isinstance(vacancies, list)