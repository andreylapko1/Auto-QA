import requests


class ReqresApi:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_user_by_id(self, user_id):
        resp = requests.get(self.base_url + f"/users/{user_id}")
        assert resp.status_code == 200
        return resp.json()["data"]


    def get_userlist(self):
        resp = requests.get(self.base_url + '/users?page=2')
        assert resp.status_code == 200
        return resp.json()['data']

    def register(self, email, password):
        data = {
            "email": email,
            "password": password,
        }
        resp = requests.post(self.base_url + '/register', json=data)
        # assert resp.status_code == 200
        return resp.json()