def all_vacancies(data):
    """печатать все вакансии"""
    if data:
        for vacancy in data:
            print("name:", vacancy.get('name'))
            print("city:", vacancy.get('city'))
            print("salary_from:", vacancy.get('salary_from'))
            print("salary_to:", vacancy.get('salary_to'))
            print("experience:", vacancy.get('experience'))
            print("url:", vacancy.get('url'))
            print("---")
    else:
        print('Вакансии не найдены')


def filter_and_sort_vacancies(data, city, minimum_salary, num_vacancies, sort_order):
    filtered_vacancies = list(filter(
        lambda vacancy: city in vacancy['city'].lower() and vacancy['salary_from'] > 0 and vacancy[
            'salary_from'] >= minimum_salary, data))

    if sort_order == '1':
        filtered_vacancies.sort(key=lambda vacancy: vacancy['salary_from'])
    elif sort_order == '2':
        filtered_vacancies.sort(key=lambda vacancy: vacancy['salary_to'], reverse=True)

    all_vacancies(filtered_vacancies[:num_vacancies])

