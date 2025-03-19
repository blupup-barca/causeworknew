import pytest

from src.file_processing import JSON_Processing


@pytest.fixture
def sample_vacancy():
    '''Пример вакансии для тестов'''
    return {
        "name": "Python Developer",
        "company": "TechCorp",
        "url": "https://example.com/job123",
        "salary": 100000
    }

@pytest.fixture
def sample_vacancies():
    return [
        {"name": "Переводчик",
         "company": "TechCorp",
         "url": "https://example.com/job1234",
         "salary": {"from": 50000, "to": 60000}},
        {"name": "Управляющий",
         "company": "TechCorp",
         "url": "https://example.com/job1214",
         "salary": {"from": 70000, "to": 80000}},
        {"name": "переводчик",
         "company": "TechCorp",
         "url": "https://example.com/job214",
         "salary": {"from": 60000, "to": 70000}}
    ]
