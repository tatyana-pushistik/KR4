from abc import ABC, abstractmethod
import requests
import json

class BaseAPI(ABC):

    @abstractmethod
    def get_vacancies(self, keyword):
        """Метод для загрузки вакансий с платформы"""
        pass


class HHApi(BaseAPI):
    """Класс для работы с платформой hh.ru, подключается к API и получает вакансии
        по ключевому слову keyword, который принимается как аргумент в абстрактном классе"""

    def __init__(self):
        super().__init__()
        self.__base_url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {
            'per_page': 100,
        }


    @property
    def headers(self):
        '''
        геттер для url
        '''
        return self.__headers

    @property
    def url(self):
        '''
        геттер для url
        '''
        return self.__base_url

    def get_vacancies(self, keyword):
        self.params.update({'text': keyword})
        response = requests.get(self.__base_url, params=self.params)
        return response.json()['items']

#if __name__ == '__main__':
  #  api_requests = HHApi()
    #api_requests.get_vacancies('тестировщик')
