
from src.fileworker import JSONVacancySaver
import os


def test_create_json_file():
    saver = JSONVacancySaver('test_file')
    vacancies = [{'title': 'Test Vacancy 1', 'city': 'Test City 1'}, {'title': 'Test Vacancy 2', 'city': 'Test City 2'}]

    saver.create_json_file(vacancies)
    assert os.path.exists(saver.filename)
    os.remove(saver.filename)


def test_read_vacancies():
    saver = JSONVacancySaver('test_file')
    vacancies = [{'title': 'Test Vacancy 5', 'city': 'Test City 5'}, {'title': 'Test Vacancy 6', 'city': 'Test City 6'}]
    saver.create_json_file(vacancies)
    data = saver.read_vacancies()
    assert data == vacancies
    os.remove(saver.filename)
