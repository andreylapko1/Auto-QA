import requests

class EmployeeApi:
    def __init__(self, url):
        self.url = url

    def get_token(self):
        response = requests.post(self.url + '/auth/login', json={
            "username": "harrypotter",
            "password": "expelliarmus"
        })
        token = response.json().get('user_token')
        if token:
            return token
        else:
            return None

    def create_user(self, first_name, last_name, middle_name, company_id, email, phone, birthdate, is_active: bool):
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'middle_name': middle_name,
            'company_id': company_id,
            'email': email,
            'phone': phone,
            'birthdate': birthdate,
            'is_active': is_active,
        }
        response = requests.post(self.url + '/employee/create', json=data)
        assert response.status_code == 200
        return response.json()


    def get_employee_by_id(self, employee_id):
        response = requests.get(self.url + '/employee/info/' + str(employee_id))
        assert response.status_code == 200
        return response.json()

    def update_employee_by_id(self, employee_id, **kwargs):
        token = self.get_token()
        data = {}
        for key, value in kwargs.items():
            data[key] = value

        if token is not None:
            token_update_url = f'{self.url}/employee/change/{employee_id}/?client_token={token}'
            print(token_update_url)
            print(data, 'DO UPDATE')
            response = requests.patch(token_update_url, json=data)
            print(response.json())
            assert response.status_code == 200
            return response.json()

