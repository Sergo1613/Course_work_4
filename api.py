from abc import ABC, abstractmethod
import requests

class Api(ABC):
    """Абстрактный класс для работы с АПИ"""
    @abstractmethod
    def get_vacancies(self, text: str):
        pass

class HeadHunterAPI(Api):
    """Абстрактный класс для работы с АПИ hh.ru"""
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies/"

    def get_vacancies(self, text: str):
        params = {
            "text": {text.lower()},
            "area": 1
        }
        vacancies_raw = requests.get(self.url, params=params)
        vacancies = vacancies_raw.json

        vacancies_data = []
        for i in vacancies.get('items', []):
            title = i.get('name', '')
            link = i.get('alternate_url', '')
            salary = i.get('salary')
            description = i.get('snippet', {}).get('responsibility', '')
            vacancies_data.append({'title': title, 'link': link, 'salary': salary, 'description': description})
        return vacancies_data

class SuperJobAPI(Api):
    """Абстрактный класс для работы с АПИ SuperJob"""
    def __init__(self):
        self.url = "https://api.superjob.ru/2.0/vacancies/"

    def get_vacancies(self, text: str):
        headers = {
            "X-Api-App-Id": "	v3.r.137600393.5fb5d8837566b65ab29b06ca1017ef74aac38052.61af120768ae59447d12445bd0561646dca7bd77"
        }
        params = {
            "keyword": {keyword.lower()},
        }

        responce = requests.get(self.url, headers=headers, params=params)
        data = responce.json()

        vacancies_data = []
        for i in data.get('objects', []):
            title = i.get('profession', '')
            link = i.get('link', '')
            salary = i.get('payment_from', 'payment_to')
            description = i.get('description')
            vacancies_data.append({'title': title, 'link': link, 'salary': salary, 'description': description})
        return vacancies_data
