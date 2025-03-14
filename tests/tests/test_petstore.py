import allure
import requests
from tests.pages.petstore_api import PetstoreAPI

api = PetstoreAPI('https://petstore.swagger.io/v2')


@allure.title("Add image to the pet")
def test_add_image_to_pet():
    image_name = "Image20250312134533.png"
    with allure.step("Create a new pet"):
        pet = api.add_new_pet("Kay", "available", "Dog")
    with allure.step("Add image to the pet"):
        resp = api.add_image_to_the_pet(pet["id"], r"C:\Users\andre\Downloads\\" + image_name)
    with allure.step("Check that 'File uploaded' in response message"):
        assert "File uploaded" in resp["message"]
    with allure.step("Check that image name in response message"):
        assert image_name in resp["message"]

