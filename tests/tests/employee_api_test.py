import requests
from tests.pages.employee_api import EmployeeApi

api = EmployeeApi('http://5.101.50.27:8000')


def test_success_create_user():
    response = api.create_user('John', 'Doe', 'johndoevich', 1,
                    'johndoevich@gmail.com', '123', '1980-01-01', True)
    assert response['id'] != 0 and isinstance(response['id'], int)


def test_get_employee_by_id():
    response = api.get_employee_by_id(1)
    assert response['id'] == 1

def test_update_employee_by_id():
    response = api.update_employee_by_id(1, first_name='JOHN', last_name='DOE', middle_name='JOHNNNNN',)
    assert response['first_name'] == 'JOHN'