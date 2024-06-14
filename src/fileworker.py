from abc import ABC, abstractmethod
from src.hh_api import HHApi
from config import ROOT_DIR
import os
import json

# Путь к файлу для сохранения вакансий
file_path = os.path.join(ROOT_DIR, 'data')

class AbstractVacancySaver(ABC):
    @abstractmethod
    def create_json_file(self, vacancies):
        pass

    @abstractmethod
    def read_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass

    # @abstractmethod
    # def get_vacancies_by_criteria(self, criteria):
    #     pass

class JSONVacancySaver(AbstractVacancySaver):
    def __init__(self, filename):
        self.filename = os.path.join(file_path, filename) + '.json'

    def create_json_file(self, vacancies):
        """Создание json файла с вакансиями"""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, indent=4, ensure_ascii=False)
        file_path = os.path.abspath(self.filename)
        return file_path

    def read_vacancies(self):
        """Чтение вакансий из файла"""
        print(f'Чтение вакансий из файла {self.filename}')
        with open(self.filename, 'r', encoding= 'utf-8') as file:
            data = json.load(file)
        return data

    def delete_vacancies(self):
        """Удаление всех вакансий из файла"""
        with open(self.filename, 'w', encoding= 'utf-8') as file:
            json.dump([], file, indent=4, ensure_ascii=False)
        print(f'Файл {self.filename} очищен')


    def delete_file(self):
        """Удаление файла"""
        os.remove(self.filename)





