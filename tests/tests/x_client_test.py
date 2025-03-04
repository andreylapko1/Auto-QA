import requests

from tests.pages.company_api import CompanyAPI

url = 'http://5.101.50.27:8000'
api = CompanyAPI(url)

def test_success_auth():
    credentials = {
        "username": "harrypotter",
        "password": "expelliarmus"
    }
    response = requests.post(url + '/auth/login', json=credentials)
    token = response.json().get('user_token')
    assert response.status_code == 200 and token



def test_get_list_company():
    resp = requests.get(url + '/company/list')
    print(resp.json())
    print(resp.status_code)
    assert resp.headers['content-type'] == 'application/json'
    data = resp.json()
    assert data[0].get('name') == "QA Студия 'ТестировщикЪ'"


def test_heck_active_companies():
    data = requests.get(url + '/company/list').json()
    print(data)
    result = sum(a['is_active'] for a in data) > 3
    assert result


def test_create_company():
    company = {
        "name": "New test company 2",
        "description": "ntc"
    }
    response = requests.post(url + "/company/create", json=company)
    assert response.status_code == 201


def test_empty_body():
    response_data = requests.post(url + "/company/create")
    assert response_data.json()["detail"][0].get("msg") == 'Field required'


def test_create_and_check():
    a_count = len(api.get_list_company())
    api.create_company("New test company 3", "ntc")
    b_count = len(api.get_list_company())
    assert b_count ==  a_count + 1


def test_get_company_by_id():
    company = api.get_company_by_id(1)
    assert company.get('name') == "QA Студия 'ТестировщикЪ'"


def test_create_update_company():
    response = api.create_company('Company test', 'abc')
    company_id = response.get('id')
    updated = api.update_company(company_id, 'New test company 13', 'ntc')
    assert updated.get('name') == "New test company 13"





