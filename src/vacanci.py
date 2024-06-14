class Vacancy:
    def __init__(self, url, city, name, salary_from, salary_to, experience):
        self.url = url
        self.city = city
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.experience = experience
        self.validate()

    def validate(self):
        if self.salary_from is None:
            self.salary_from = 0
        if self.salary_to is None:
            self.salary_to = 0

    def to_dict(self):
        return {
            'name': self.name,
            'url': self.url,
            'city': self.city,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'experience': self.experience
        }

    @classmethod
    def create_vacancy(cls, data):
        instances = []
        for vac_info in data:
            url = vac_info.get('alternate_url')
            city = vac_info.get('area').get('name')
            name = vac_info.get('name')
            salary = vac_info.get('salary')
            salary_from = salary.get('from') if salary and 'from' in salary else None
            salary_to = salary.get('to') if salary and 'to' in salary else None
            experience = vac_info.get('experience').get('name')
            instances.append(cls(url, city, name, salary_from, salary_to, experience))
        return instances

