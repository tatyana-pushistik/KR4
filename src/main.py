from src.hh_api import HHApi
from src.vacanci import Vacancy
import json
from src.fileworker import JSONVacancySaver
from src.function import all_vacancies, filter_and_sort_vacancies

print('Программа для поиска вакансий на hh.ru')
print('Введите ключевое слово для поиска вакансий:\n')
keyword = input().lower()
api_requests = HHApi()
data = api_requests.get_vacancies(keyword)
vacancies = [vacancy.to_dict() for vacancy in Vacancy.create_vacancy(data)]

def user_connect(keyword):
    data = api_requests.get_vacancies(keyword)
    vacancies = [vacancy.to_dict() for vacancy in Vacancy.create_vacancy(data)]
    filename = JSONVacancySaver(keyword)
    file_data = filename.create_json_file(vacancies)
    while True:
        print('1. Показать все вакансии')
        print('2. Фильтрация по городу и зарплате')
        print('3. Начать новый поиск?')
        print('4. Выход')

        print('Выберите действие:')
        choice = input()
        if choice == '1':
            vacancies = JSONVacancySaver(keyword).read_vacancies()
            all_vacancies(vacancies)
        elif choice == '2':
            vacancies = JSONVacancySaver(keyword).read_vacancies()
            print("Укажите название города:")
            city = input().lower()
            print("Введите минимальную зарплату для поиска вакансий:")
            while True:
                try:
                    minimum_salary = int(input())
                    break
                except ValueError:
                    print("Некорректный ввод. Пожалуйста, введите целое число.")
            print("Сколько вакансий показать?")
            while True:
                try:
                    num_vacancies = int(input())
                    break
                except ValueError:
                    print("Некорректный ввод. Пожалуйста, введите целое число.")

            print("Как отсортировать вакансии?\n Введите:\n 1 - для сортировки по возрастанию минимальной зарплаты\n 2 - для сортировки по убыванию максимальной зарплаты:")
            sort_order = input()
            filter_and_sort_vacancies(vacancies, city, minimum_salary, num_vacancies, sort_order)


        elif choice == '3':
            JSONVacancySaver(keyword).delete_file()
            print('Введите ключевое слово для поиска вакансий:\n')
            keyword = input().lower()
            data = api_requests.get_vacancies(keyword)
            vacancies = [vacancy.to_dict() for vacancy in Vacancy.create_vacancy(data)]
            file_data = filename.create_json_file(vacancies)
        elif choice == '4':
            JSONVacancySaver(keyword).delete_file()
            print('Программа завершена')
            break
        else:
            print('Неверный ввод')

if __name__ == '__main__':
    user_connect(keyword)
