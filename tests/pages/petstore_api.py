import allure
import requests


class PetstoreAPI:
    def __init__(self, petstore_api_url):
        self.base_url = petstore_api_url


    def add_new_pet(self, pet_name, pet_status, category_name):
        new_pet = {
            "id": 0,
            "category": {
                "id": 0,
                "name": category_name
            },
            "name": pet_name,
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": pet_status
        }
        resp = requests.post(self.base_url + '/pet', json=new_pet)
        return resp.json()

    def add_image_to_the_pet(self, pet_id, image_path):
        print(image_path)
        file = {'file': open(image_path, 'rb')}
        resp = requests.post(self.base_url + f'/pet/{pet_id}/uploadImage', files=file)
        allure.attach.file(image_path, attachment_type=allure.attachment_type.PNG)
        return resp.json()
