import requests


class CompanyAPI:
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


    def get_list_company(self):
        resp = requests.get(self.url + '/company/list')
        assert resp.status_code == 200
        return resp.json()



    def create_company(self, name, description):
        data = {
            "name": name,
            "description": description
        }
        resp = requests.post(self.url + '/company/create', json=data)
        assert resp.status_code == 201
        return resp.json()



    def get_company_by_id(self, company_id):
        resp = requests.get(self.url + f'/company/{company_id}')
        assert resp.status_code == 200
        return resp.json()


    def update_company(self, company_id, name, description):
        data = {
            "name": name,
            "description": description,
        }
        token = self.get_token()
        token_update_url = f'{self.url}/company/update/{company_id}/?client_token={token}'
        response = requests.patch(token_update_url, json=data)
        assert response.status_code == 202
        return response.json()


