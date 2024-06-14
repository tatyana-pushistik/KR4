import pytest
from src.vacanci import Vacancy

@pytest.fixture
def vacancy_data():
    return [
        {
            'alternate_url': 'https://example.com',
            'area': {'name': 'City 1'},
            'name': 'Job 1',
            'salary': {'from': 1000, 'to': 2000},
            'experience': {'name': 'Entry Level'}
        },
        {
            'alternate_url': 'https://example.com',
            'area': {'name': 'City 2'},
            'name': 'Job 2',
            'salary': {'from': 2000, 'to': 3000},
            'experience': {'name': 'Mid Level'}
        }
    ]

def test_create_vacancy(vacancy_data):
    vacancies = Vacancy.create_vacancy(vacancy_data)
    assert len(vacancies) == 2
    assert isinstance(vacancies[0], Vacancy)
    assert vacancies[0].url == 'https://example.com'
    assert vacancies[0].city == 'City 1'
    assert vacancies[0].name == 'Job 1'
    assert vacancies[0].salary_from == 1000
    assert vacancies[0].salary_to == 2000
    assert vacancies[0].experience == 'Entry Level'

    assert isinstance(vacancies[1], Vacancy)
    assert vacancies[1].url == 'https://example.com'
    assert vacancies[1].city  == 'City 2'
    assert vacancies[1].name == 'Job 2'
    assert vacancies[1].salary_from == 2000
    assert vacancies[1].salary_to == 3000
    assert vacancies[1].experience == 'Mid Level'

def test_validate_salary():
    vacancy = Vacancy('https://example.com', 'City', 'Job', None, None, 'Experience')
    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 0

    vacancy = Vacancy('https://example.com', 'City', 'Job', 1000, None, 'Experience')
    assert vacancy.salary_from == 1000
    assert vacancy.salary_to == 0

    vacancy = Vacancy('https://example.com', 'City', 'Job', None, 2000, 'Experience')
    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 2000
