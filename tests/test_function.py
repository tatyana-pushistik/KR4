import pytest
from src.function import all_vacancies, filter_and_sort_vacancies

@pytest.fixture
def sample_data():
    return [
        {
            'name': 'Job 1',
            'city': 'City 1',
            'salary_from': 50000,
            'salary_to': 70000,
            'experience': '2 years',
            'url': 'https://example.com/job1'
        },
        {
            'name': 'Job 2',
            'city': 'City 2',
            'salary_from': 60000,
            'salary_to': 80000,
            'experience': '3 years',
            'url': 'https://example.com/job2'
        },
        {
            'name': 'Job 3',
            'city': 'City 1',
            'salary_from': 45000,
            'salary_to': 65000,
            'experience': '1 year',
            'url': 'https://example.com/job3'
        }
    ]

def test_all_vacancies_with_data(capsys, sample_data):
    all_vacancies(sample_data)
    captured = capsys.readouterr()
    assert captured.out == '''name: Job 1
city: City 1
salary_from: 50000
salary_to: 70000
experience: 2 years
url: https://example.com/job1
---
name: Job 2
city: City 2
salary_from: 60000
salary_to: 80000
experience: 3 years
url: https://example.com/job2
---
name: Job 3
city: City 1
salary_from: 45000
salary_to: 65000
experience: 1 year
url: https://example.com/job3
---
'''

def test_all_vacancies_without_data(capsys):
    all_vacancies([])
    captured = capsys.readouterr()
    assert captured.out == 'Вакансии не найдены\n'

def test_filter_and_sort_vacancies_without_data(sample_data):
    filtered_vacancies = filter_and_sort_vacancies(sample_data, 'City 3', 50000, 2, '1')
    assert filtered_vacancies == None
